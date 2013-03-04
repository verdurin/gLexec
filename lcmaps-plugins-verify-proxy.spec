Summary: Proxy verification plugin for LCMAPS
Name: lcmaps-plugins-verify-proxy
Version: 1.5.2
Release: 2%{?dist}
Vendor: Nikhef
License: ASL 2.0
Group: System Environment/Libraries
Prefix:	      /opt/ichep/emi2/glexec/0.9.6
URL: http://www.nikhef.nl/pub/projects/grid/gridwiki/index.php/Site_Access_Control
Source0: http://software.nikhef.nl/security/%{name}/%{name}-%{version}.tar.gz
BuildRequires: lcmaps-interface, openssl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

This package contains the Verify Proxy plugin.

%prep
%setup -q

%build

%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# clean up installed documentation files
rm -rf ${RPM_BUILD_ROOT}%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE
%{_libdir}/lcmaps/lcmaps_verify_proxy.mod
%{_libdir}/lcmaps/liblcmaps_verify_proxy.so
%{_datadir}/man/man8/lcmaps_verify_proxy.mod.8.gz


%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 1.5.2-2
- use local custom prefix

* Mon Jan 30 2012 Mischa Salle <msalle@nikhef.nl> 1.5.2-1
- updated version

* Thu Dec 15 2011 Mischa Salle <msalle@nikhef.nl> 1.5.0-2
- updated version
- adding manpage

* Tue Aug  7 2011 Mischa Salle <msalle@nikhef.nl> 1.4.12-3
- Forgot to add changelog entry for 1.4.12-2

* Tue Aug  2 2011 Mischa Salle <msalle@nikhef.nl> 1.4.12-2
- Remove docs created in make install, rpm does it via %doc
- Update %files to reflect new layout: modules in lcmaps, no .so.0*

* Tue Aug  2 2011 Oscar Koeroo <okoeroo@nikhef.nl> 1.4.12-1
- New version 1.4.12

* Wed Mar 23 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.9-2
- removed explicit requires

* Mon Mar  7 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.9-1
- Updated dependencies on openssl

* Fri Mar  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.8-2
- disable static libraries
- fixed license string
- dropped devel package

* Mon Feb 21 2011 Dennis van Dok <dennisvd@nikhef.nl> 
- Initial build.


