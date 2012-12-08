Summary:	Convert HTML documents into PDF or PS format
Name:		htmldoc
Version:	1.8.27
Release:	14
License:	GPLv2
Group:		File tools
URL:		http://www.htmldoc.org/
Source:		%{name}-%{version}-source.tar.bz2 
Patch0:		htmldoc-1.8.27-CVE-2009-3050.diff
Patch1:		htmldoc-fortify-fail.patch
Patch2:		htmldoc-1.8.27-fix-build-against-libpng15.patch
Patch3:		htmldoc-1.8.27-fixdso.patch
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	fltk-devel
Requires:	fltk

%description
HTMLDOC allow you to convert Html documents into PDF or PS format.
Links and somes specific things of PDF format can be used.

%package	nogui
Summary:	Convert HTML documents into PDF or PS format 
Group:		File tools

%description	nogui
This package contains the non-GUI version of %{name}

%prep

%setup -q
%patch0 -p1 -b .CVE-2009-3050
%patch1 -p1
%patch2 -p1 -b .libpng15
%patch3 -p1 -b .dso

%build
# first build the non gui version
%configure2_5x \
    --disable-rpath \
    --disable-localpng \
    --disable-localjpeg \
    --disable-localzlib \
    --without-gui

%make
mv htmldoc/htmldoc htmldoc-nogui
make clean

%configure2_5x \
    --disable-rpath \
    --disable-localpng \
    --disable-localjpeg \
    --disable-localzlib \
    --with-gui \
    --with-openssl-libs \
    --with-openssl-includes

%make

%install
%makeinstall

install -d %{buildroot}%{_bindir}
install -m0755 htmldoc-nogui %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=HTMLDoc
Comment=Convert HTML files to PDF or PostScript
Exec=%{_bindir}/%{name}
Icon=publishing_section
Terminal=false
Type=Application
StartupNotify=true
MimeType=text/html;
Categories=FileTools;Utility;
EOF

%files
%defattr(-,root,root,0755)
%doc CHANGES.txt README.txt COPYING.txt
%{_bindir}/htmldoc
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

%files nogui
%defattr(-,root,root,0755)
%doc CHANGES.txt README.txt COPYING.txt
%{_bindir}/htmldoc-nogui


%changelog
* Mon Sep 12 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.27-13mdv2012.0
+ Revision: 699566
- Patch2: fix build against libpng15
- also rebuild against new fltk

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.27-12
+ Revision: 665485
- mass rebuild

* Tue Dec 21 2010 Funda Wang <fwang@mandriva.org> 1.8.27-11mdv2011.0
+ Revision: 623660
- add gentoo patch to make it build

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Tue Apr 06 2010 Funda Wang <fwang@mandriva.org> 1.8.27-10mdv2010.1
+ Revision: 531984
- rebuild for new openssl

* Wed Mar 31 2010 Funda Wang <fwang@mandriva.org> 1.8.27-9mdv2010.1
+ Revision: 530156
- fix desktop file

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.27-8mdv2010.1
+ Revision: 511575
- rebuilt against openssl-0.9.8m

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.27-7mdv2010.1
+ Revision: 488765
- rebuilt against libjpeg v8

* Fri Jan 08 2010 Frederik Himpe <fhimpe@mandriva.org> 1.8.27-6mdv2010.1
+ Revision: 487720
- rebuild

* Fri Sep 11 2009 Oden Eriksson <oeriksson@mandriva.com> 1.8.27-5mdv2010.0
+ Revision: 438470
- P0: security fix for CVE-2009-3050

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 1.8.27-4mdv2010.0
+ Revision: 416660
- rebuilt against libjpeg v7

* Sun Dec 14 2008 Funda Wang <fwang@mandriva.org> 1.8.27-3mdv2009.1
+ Revision: 314158
- fix br
- use system libs

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.8.27-2mdv2009.0
+ Revision: 218435
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 21 2007 Adam Williamson <awilliamson@mandriva.org> 1.8.27-2mdv2008.1
+ Revision: 136064
- oops, fix file list for real
- fix file lists
- rebuild for new era
- XDG menu
- new license policy
- spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 02 2007 Lenny Cartier <lenny@mandriva.com> 1.8.27-1mdv2007.0
+ Revision: 115892
- Update to 1.8.27 and fix url
- Import htmldoc

* Tue Mar 07 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.8.25-1mdk
- New release 1.8.25
- use mkrel

* Tue Jan 17 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.8.23-9mdk
- rebuild for openssl 0.9.8

* Fri Jul 08 2005 Lenny Cartier <lenny@mandriva.com> 1.8.23-8mdk
- rebuild

* Wed Jun 02 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.8.23-7mdk
- added the htmldoc-nogui sub package
- fix deps
- misc spec file fixes

* Sat May 22 2004 Robert Vojta <robert.vojta@mandrake.cz> 1.8.23-6mdk
- rebuild against cooker

