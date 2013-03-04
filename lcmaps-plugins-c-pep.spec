Summary: C-PEP plugin for the LCMAPS authorization framework
Name: lcmaps-plugins-c-pep
Version: 1.2.2
Release: 2%{?dist}
Vendor: Nikhef
License: ASL 2.0
Group: System Environment/Libraries
Prefix:	      /opt/ichep/emi2/glexec/0.9.6
URL: http://www.nikhef.nl/pub/projects/grid/gridwiki/index.php/Site_Access_Control
Source0: http://software.nikhef.nl/security/%{name}/%{name}-%{version}.tar.gz
BuildRequires: argus-pep-api-c-devel, lcmaps-interface
BuildRequires: openssl-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

This package contains the PEP client plug-in.


%prep
%setup -q

%build

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS  LICENSE
%{_libdir}/lcmaps/lcmaps_c_pep.mod
%{_libdir}/lcmaps/liblcmaps_c_pep.so
%{_datadir}/man/man8/lcmaps_plugins_c_pep.8.gz


%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 1.2.2-2
- use local custom prefix

* Mon Mar 19 2012 Mischa Salle <msalle@nikhef.nl> 1.2.2-1
- rename manpage to use underscore instead of hyphen
- updated version

* Mon Jan 30 2012 Mischa Salle <msalle@nikhef.nl> 1.2.1-1
- updated version

* Fri Dec 16 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.2.0-3
- Added build dependency on openssl-devel

* Thu Dec 15 2011 Mischa Salle <msalle@nikhef.nl> 1.2.0-2
- updated version
- new installation path /lcmaps/
- plugin creates only .so and .mod (no .so.0 etc)

* Tue Apr 26 2011 Oscar Koeroo <okoeroo@nikhef.nl> 1.1.4-1
- New release enables reading a proxy from a root-squashed NFS file system.

* Wed Mar 23 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.1.0-3
- removed explicit requires

* Fri Mar  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.1.0-2
- fixed license string
- disable static libraries
- dropped devel package

* Mon Feb 21 2011 Dennis van Dok <dennisvd@nikhef.nl> 
- Initial build.


