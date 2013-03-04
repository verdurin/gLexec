Summary: Basic plugins for the LCMAPS authorization framework
Name: lcmaps-plugins-basic
Version: 1.5.0
Release: 4%{?dist}
License: ASL 2.0
Group: System Environment/Libraries
Prefix:	      /opt/ichep/emi2/glexec/0.9.6
URL: http://www.nikhef.nl/pub/projects/grid/gridwiki/index.php/Site_Access_Control
Source0: http://software.nikhef.nl/security/%{name}/%{name}-%{version}.tar.gz
BuildRequires: lcmaps-interface
BuildRequires: openldap-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

This package contains the basic plugins.

%package ldap
Summary: LDAP enforcement plug-in for LCMAPS
Group: System Environment/Libraries
Requires: lcmaps

%description ldap
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

This package contains the LDAP enforcement plug-in.

%prep
%setup -q

%build
%configure --disable-static --with-moduledir=%{_libdir}/lcmaps
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/lcmaps/lcmaps_dummy_bad.mod
%{_libdir}/lcmaps/lcmaps_dummy_good.mod
%{_libdir}/lcmaps/lcmaps_localaccount.mod
%{_libdir}/lcmaps/lcmaps_poolaccount.mod
%{_libdir}/lcmaps/lcmaps_posix_enf.mod
%{_libdir}/lcmaps/liblcmaps_dummy_bad.so
%{_libdir}/lcmaps/liblcmaps_dummy_good.so
%{_libdir}/lcmaps/liblcmaps_localaccount.so
%{_libdir}/lcmaps/liblcmaps_poolaccount.so
%{_libdir}/lcmaps/liblcmaps_posix_enf.so
%{_mandir}/man8/lcmaps_dummy_bad.mod.8*
%{_mandir}/man8/lcmaps_dummy_good.mod.8*
%{_mandir}/man8/lcmaps_localaccount.mod.8*
%{_mandir}/man8/lcmaps_poolaccount.mod.8*
%{_mandir}/man8/lcmaps_posix_enf.mod.8*
%doc AUTHORS LICENSE

%files ldap
%defattr(-,root,root,-)
%{_libdir}/lcmaps/lcmaps_ldap_enf.mod
%{_libdir}/lcmaps/liblcmaps_ldap_enf.so
%{_mandir}/man8/lcmaps_ldap_enf.mod.8*
%doc AUTHORS LICENSE

%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 1.5.0-4
- use local custom prefix

* Thu Dec 27 2011 Oscar Koeroo <okoeroo@nikhef.nl> 1.5.0-3
- Changed the install directory to libdir/lcmaps/ for the LDAP plugin.

* Thu Dec 23 2011 Oscar Koeroo <okoeroo@nikhef.nl> 1.5.0-2
- Changed the install directory to libdir/lcmaps/ for the plugins.

* Thu Dec 15 2011 Mischa Salle <msalle@nikhef.nl> 1.5.0-1
- updated version

* Wed Nov 16 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.6-2
- moved plugin to plugins/ subdirectory

* Thu Jul 14 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.6-1
- Updated version

* Tue Jul  5 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.4.5-2
- Remove Vendor tag

* Thu Jun 30 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.5-1
- Moved lcmaps_ldap_enf.mod to the -ldap package
- Updated to version 1.4.5

* Wed Apr  6 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.3-1
- bumped version

* Wed Mar 23 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.2-4
- removed explicit requires

* Mon Mar  7 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.2-3
- Split off the ldap enforcement plug-in

* Fri Mar  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.2-2
- drop the development package
- fixed the licence string

* Mon Feb 21 2011 Dennis van Dok <dennisvd@nikhef.nl> 
- Initial build.
