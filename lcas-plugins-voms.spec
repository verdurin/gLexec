Summary: VOMS plugins for the LCAS authorization framework
Name: lcas-plugins-voms
Version: 1.3.10
Release: 2%{?dist}
Vendor: Nikhef
License: ASL 2.0
Group: System Environment/Libraries
Prefix:	      /opt/ichep/emi2/glexec/0.9.6
URL: http://www.nikhef.nl/pub/projects/grid/gridwiki/index.php/Site_Access_Control
Source0: http://software.nikhef.nl/security/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: globus-core
BuildRequires: globus-common-devel
BuildRequires: globus-gsi-callback-devel
BuildRequires: globus-gsi-credential-devel
BuildRequires: globus-gsi-proxy-core-devel
BuildRequires: globus-gsi-proxy-ssl-devel
BuildRequires: globus-gssapi-gsi-devel
BuildRequires: globus-gss-assist-devel
BuildRequires: voms-devel, lcas-interface
BuildRequires: gridsite-devel
BuildRequires: libxml2-devel
BuildRequires: openssl-devel


%description

LCAS makes binary ('yes' or 'no') authorization decisions at the site
and resource level, based on grid (X.509) credentials and VOMS attributes.
It has a pluggable interface. This package contains the VOMS plug-ins.

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
%doc AUTHORS LICENSE
%{_libdir}/lcas/lcas_voms.mod
%{_libdir}/lcas/liblcas_voms.so
%{_sbindir}/edg-lcas-voms2gacl
%{_sbindir}/glite-mapfile2gacl
%{_sbindir}/mapfile2gacl


%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 1.3.10-2
- use local custom prefix

* Mon Jan 30 2012 Mischa Salle <msalle@nikhef.nl> 1.3.10-1
- Bumped version

* Fri Dec 16 2011 Mischa Salle <msalle@nikhef.nl> 1.3.9-1
- Updated version

* Wed Jul 13 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.8-1
- updated version

* Wed Mar 23 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.7-2
- removed explicit requires

* Mon Mar  7 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.7-1
- fixed globus dependencies
- fixed openssl dependency

* Fri Mar  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.6-2
- disable static libraries
- fixed license string

* Thu Feb 24 2011 Dennis van Dok <dennisvd@nikhef.nl> 
- Initial build.


