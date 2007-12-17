%define name	htmldoc
%define version	1.8.27
%define release %mkrel 1

Summary:	Convert HTML documents into PDF or PS format 
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		%{name}-%{version}-source.tar.bz2 
License:	GPL
Group:		File tools
URL:		http://www.htmldoc.org/
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRequires:	openssl-devel
BuildRequires:	libfltk-devel
Requires:	fltk

%description
HTMLDOC allow you to convert Html documents into PDF or PS format.
Links and somes specific things of PDF format can be used.

%package	nogui
Summary:	Convert HTML documents into PDF or PS format 
Group:		File tools

%description	nogui
This package contains the non gui version of %{name}

%prep

%setup -q

%build

# first build the non gui version
%configure \
    --without-gui

%make
mv htmldoc/htmldoc htmldoc-nogui
make clean

%configure \
    --disable-rpath \
    --enable-localpng \
    --enable-localjpeg \
    --enable-localzlib \
    --with-gui \
    --with-openssl-libs \
    --with-openssl-includes

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_menudir}

cat > %{buildroot}%{_menudir}/%{name} <<EOF
?package(%{name}): \
command="%{_bindir}/htmldoc" \
title="Htmldoc" \
longtitle="Converting Html files to PDF or PostScript" \
icon="publishing_section.png" \
needs="x11" \
section="Office/Publishing"
EOF

install -m0755 htmldoc-nogui %{buildroot}%{_bindir}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root,0755)
%doc CHANGES.txt README.txt
%{_bindir}/htmldoc
%{_mandir}/man1/*
%{_docdir}/htmldoc/*
%{_datadir}/htmldoc/*
%{_menudir}/*

%files nogui
%defattr(-,root,root,0755)
%doc CHANGES.txt README.txt
%{_bindir}/htmldoc-nogui


