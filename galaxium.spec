%define name galaxium
%define version 0.7.1
%define release %mkrel 1

Summary: Galaxium Messenger for MSN
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_%{version}.tar.gz
License: GPL
Group: Networking/Instant messaging
Url: http://galaxium.googlecode.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: glade-sharp2
#BuildRequires: gecko-sharp2
BuildRequires: mono-devel
BuildRequires: webkit-sharp-devel
BuildRequires: ndesk-dbus-glib
BuildRequires: mono-addins
BuildRequires: libanculus-sharp
BuildRequires: libgstreamer-devel
BuildRequires: libswfdec-devel

%description
This is an instant messaging client that uses the MSN service. It has
a simple GNOME interface.

%prep
%setup -q
sh ./autogen.sh

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%if %_lib != lib
mv %buildroot%_prefix/lib/%name/* %buildroot%_libdir/%name/
%endif
cp build/*.config %buildroot%_libdir/%name

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) %_bindir/galaxium
%_libdir/%name
%_datadir/%name
%_datadir/applications/%name.desktop
%_mandir/man1/%{name}*
%_datadir/pixmaps/*

