Summary:	Convert HTML documents into PDF or PS format
Name:		htmldoc
Version:	1.8.27
Release:	19
License:	GPLv2
Group:		File tools
Url:		http://www.htmldoc.org/
Source0:	%{name}-%{version}-source.tar.bz2 
Patch0:		htmldoc-1.8.27-CVE-2009-3050.diff
Patch1:		htmldoc-fortify-fail.patch
Patch2:		htmldoc-1.8.27-fix-build-against-libpng15.patch
Patch3:		htmldoc-1.8.27-fixdso.patch

BuildRequires:	fltk-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
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
%apply_patches

%build
# first build the non gui version
%configure2_5x \
	--disable-localpng \
	--disable-localjpeg \
	--disable-localzlib \
	--without-gui

%make
mv htmldoc/htmldoc htmldoc-nogui
make clean

%configure2_5x \
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
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
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
%doc CHANGES.txt README.txt COPYING.txt
%{_bindir}/htmldoc
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%files nogui
%doc CHANGES.txt README.txt COPYING.txt
%{_bindir}/htmldoc-nogui

