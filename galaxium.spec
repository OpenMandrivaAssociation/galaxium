%define name galaxium
%define version 0.7.4.1
%define release %mkrel 4

Summary: Galaxium Messenger for MSN
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://galaxium.googlecode.com/files/%{name}_%{version}.tar.gz
Patch: galaxium-0.7.4.1-swfdec-major.patch
#gw from svn, fix build with new mono
Patch1: galaxium-r1218-fix-build.patch
License: GPLv2+
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
BuildRequires: desktop-file-utils

%description
This is an instant messaging client that uses the MSN service. It has
a simple GNOME interface.

%prep
%setup -q
%patch -p1 -b .swfdec-major
%patch1
sh ./autogen.sh

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
cp build/*.config %buildroot%_libdir/%name

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

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

