Summary: VOMS plugins for the LCMAPS authorization framework
Name: lcmaps-plugins-voms
Version: 1.5.3
Release: 2%{?dist}
License: ASL 2.0
Group: System Environment/Libraries
Prefix:	      /opt/ichep/emi2/glexec/0.9.6
URL: http://www.nikhef.nl/pub/projects/grid/gridwiki/index.php/Site_Access_Control
Source0: http://software.nikhef.nl/security/%{name}/%{name}-%{version}.tar.gz
BuildRequires: lcmaps-interface, voms-devel, openssl-devel
BuildRequires: globus-common-devel, globus-core, globus-gsi-callback-devel
BuildRequires: globus-gsi-credential-devel, globus-gsi-proxy-core-devel
BuildRequires: globus-gsi-proxy-ssl-devel,
BuildRequires: globus-gssapi-gsi-devel, globus-gss-assist-devel
Requires: lcmaps, voms, openssl
Requires: globus-common, globus-gsi-callback
Requires: globus-gsi-credential, globus-gsi-proxy-core
Requires: globus-gsi-proxy-ssl
Requires: globus-gssapi-gsi, globus-gss-assist

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

This package contains the VOMS plugins.


%prep
%setup -q

%build

%configure --disable-static

# The following two lines were suggested by
# https://fedoraproject.org/wiki/Packaging/Guidelines to prevent any
# RPATHs creeping in.
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

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
%{_libdir}/lcmaps/lcmaps_voms.mod
%{_libdir}/lcmaps/lcmaps_voms_localaccount.mod
%{_libdir}/lcmaps/lcmaps_voms_localgroup.mod
%{_libdir}/lcmaps/lcmaps_voms_poolaccount.mod
%{_libdir}/lcmaps/lcmaps_voms_poolgroup.mod
%{_libdir}/lcmaps/liblcmaps_voms.so
%{_libdir}/lcmaps/liblcmaps_voms_localaccount.so
%{_libdir}/lcmaps/liblcmaps_voms_localgroup.so
%{_libdir}/lcmaps/liblcmaps_voms_poolaccount.so
%{_libdir}/lcmaps/liblcmaps_voms_poolgroup.so
%{_datadir}/man/man8/lcmaps_voms.mod.8*
%{_datadir}/man/man8/lcmaps_voms_localaccount.mod.8*
%{_datadir}/man/man8/lcmaps_voms_localgroup.mod.8*
%{_datadir}/man/man8/lcmaps_voms_poolaccount.mod.8*
%{_datadir}/man/man8/lcmaps_voms_poolgroup.mod.8*

%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 1.5.3-2
- use local custom prefix

* Tue Mar 20 2012 Mischa Salle <msalle@nikhef.nl> 1.5.3-1
- updated version
- adding manpages

* Wed Feb 29 2012 Mischa Salle <msalle@nikhef.nl> 1.5.2-1
- updated version

* Mon Jan 30 2012 Mischa Salle <msalle@nikhef.nl> 1.5.1-1
- updated version

* Thu Dec 15 2011 Mischa Salle <msalle@nikhef.nl> 1.5.0-1
- updated version

* Fri Jul 15 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.4-1
- removed vendor tag
- disabled versioning

* Wed Apr  6 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.3-1
- bumped version

* Mon Mar  7 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.2-1
- Updated dependencies

* Fri Mar  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.1-2
- fixed license string
- disabled static libraries
- dropped devel package

* Mon Feb 21 2011 Dennis van Dok <dennisvd@nikhef.nl> 
- Initial build.


