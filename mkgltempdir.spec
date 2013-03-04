Summary: Create a directory owned by the gLExec target user
Name: mkgltempdir
Version: 0.0.3
Release: 3%{?dist}
Vendor: Nikhef
License: ASL 2.0
Group: Applications/System
Prefix:	/opt/ichep/emi2/glexec/0.9.6
URL: http://www.nikhef.nl/pub/projects/grid/gridwiki/index.php/Site_Access_Control
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: glexec

%description
Helper script to create a secure temporary directory owned by the gLExec target
user for use by the payload.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root,-)
%{_sbindir}/mkgltempdir
%{_datadir}/man/man8/mkgltempdir.8*
%doc README AUTHORS LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 0.0.3-3
- use local custom prefix

* Wed Feb  1 2012 Dennis van Dok <dennisvd@nikhef.nl> 0.0.3-2
- Updated for autoconfigured package
- Added manpage and README

* Wed Dec 21 2011 Mischa Salle <msalle@nikhef.nl> 0.0.3-1
- Initial version.
