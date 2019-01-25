#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : redsocks
Version  : 0.5
Release  : 16
URL      : https://github.com/darkk/redsocks/archive/release-0.5.tar.gz
Source0  : https://github.com/darkk/redsocks/archive/release-0.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: redsocks-bin = %{version}-%{release}
Requires: redsocks-license = %{version}-%{release}
Requires: redsocks-services = %{version}-%{release}
BuildRequires : libevent-dev
Patch1: 0001-Add-make-install-target.patch
Patch2: 0002-Update-redsocks.service-to-work-on-Clear.patch

%description
This tool allows you to redirect any TCP connection to SOCKS or HTTPS
proxy using your firewall, so redirection is system-wide.

%package bin
Summary: bin components for the redsocks package.
Group: Binaries
Requires: redsocks-license = %{version}-%{release}
Requires: redsocks-services = %{version}-%{release}

%description bin
bin components for the redsocks package.


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
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548390016
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1548390016
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/redsocks
cp debian/copyright %{buildroot}/usr/share/package-licenses/redsocks/debian_copyright
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/redsocks

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/redsocks/debian_copyright

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/redsocks.service
