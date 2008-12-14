Summary:	Convert HTML documents into PDF or PS format 
Name:		htmldoc
Version:	1.8.27
Release:	%mkrel 3
Source:		%{name}-%{version}-source.tar.bz2 
License:	GPLv2
Group:		File tools
URL:		http://www.htmldoc.org/
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRequires:	openssl-devel
BuildRequires:	libfltk-devel
Requires:	fltk
BuildRoot:	%{_tmppath}/%{name}-buildroot

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

%build
# first build the non gui version
%configure2_5x \
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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
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
MimeType=foo/bar;foo2/bar2;
Categories=FileTools;
EOF

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

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
