Summary:	Convert HTML documents into PDF or PS format
Name:		htmldoc
Version:	1.9.6
Release:	1
License:	GPLv2
Group:		File tools
Url:		http://www.htmldoc.org/
Source0:	https://github.com/michaelrsweet/htmldoc/archive/v%{version}.tar.gz

BuildRequires:	fltk-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(gnutls) pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xft)
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
autoconf

%build
# first build the non gui version
%configure \
	--disable-localpng \
	--disable-localjpeg \
	--disable-localzlib \
	--without-gui

%make
mv htmldoc/htmldoc htmldoc-nogui
make clean

%configure \
	--disable-localpng \
	--disable-localjpeg \
	--disable-localzlib \
	--with-gui \
	--with-openssl-libs \
	--with-openssl-includes

%make

%install
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

make install \
  BUILDROOT=%{buildroot} \
  VERBOSE=1

%files
%doc help.html htmldoc.pdf
%{_bindir}/htmldoc
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/htmldoc.xpm
%{_datadir}/mime/packages/htmldoc.xml

%files nogui
%{_bindir}/htmldoc-nogui
