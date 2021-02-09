#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : redsocks
Version  : 0.5
Release  : 22
URL      : https://github.com/darkk/redsocks/archive/release-0.5.tar.gz
Source0  : https://github.com/darkk/redsocks/archive/release-0.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: redsocks-bin = %{version}-%{release}
Requires: redsocks-libexec = %{version}-%{release}
Requires: redsocks-license = %{version}-%{release}
Requires: redsocks-services = %{version}-%{release}
BuildRequires : libevent-dev
Patch1: 0001-Add-make-install-target.patch
Patch2: 0002-Update-redsocks.service-to-work-on-Clear.patch
Patch3: 0003-Add-a-script-to-configure-iptables-rules-for-automat.patch
Patch4: 0004-Add-support-for-a-configuration-file-for-the-PAC-par.patch
Patch5: 0005-Add-a-way-to-configure-proxy-overrides-to-the-config.patch

%description
This tool allows you to redirect any TCP connection to SOCKS or HTTPS
proxy using your firewall, so redirection is system-wide.

%package autostart
Summary: autostart components for the redsocks package.
Group: Default

%description autostart
autostart components for the redsocks package.


%package bin
Summary: bin components for the redsocks package.
Group: Binaries
Requires: redsocks-libexec = %{version}-%{release}
Requires: redsocks-license = %{version}-%{release}
Requires: redsocks-services = %{version}-%{release}

%description bin
bin components for the redsocks package.


%package libexec
Summary: libexec components for the redsocks package.
Group: Default
Requires: redsocks-license = %{version}-%{release}

%description libexec
libexec components for the redsocks package.


%package license
Summary: license components for the redsocks package.
Group: Default

%description license
license components for the redsocks package.


%package services
Summary: services components for the redsocks package.
Group: Systemd services

%description services
services components for the redsocks package.


%prep
%setup -q -n redsocks-release-0.5
cd %{_builddir}/redsocks-release-0.5
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579713611
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1579713611
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/redsocks
cp %{_builddir}/redsocks-release-0.5/debian/copyright %{buildroot}/usr/share/package-licenses/redsocks/b00f8fda4bdf2cabe16d585497c23f0dd098640c
%make_install

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/redsocks-wpad.path

%files bin
%defattr(-,root,root,-)
/usr/bin/redsocks

%files libexec
%defattr(-,root,root,-)
/usr/libexec/parse-pac.pl

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/redsocks/b00f8fda4bdf2cabe16d585497c23f0dd098640c

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/redsocks-wpad.path
/usr/lib/systemd/system/redsocks-managed.service
/usr/lib/systemd/system/redsocks-wpad.path
/usr/lib/systemd/system/redsocks-wpad.service
/usr/lib/systemd/system/redsocks.service
