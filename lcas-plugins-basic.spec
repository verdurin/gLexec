Summary: Basic plugins for the LCAS authorization framework
Name: lcas-plugins-basic
Version: 1.3.6
Release: 2%{?dist}
License: ASL 2.0
Group: System Environment/Libraries
Prefix:	      /opt/ichep/emi2/glexec/0.9.6
URL: http://www.nikhef.nl/pub/projects/grid/gridwiki/index.php/Site_Access_Control
Source0: http://software.nikhef.nl/security/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: globus-common-devel, globus-gssapi-gsi-devel
BuildRequires: lcas-interface
Requires: lcas

%description
LCAS makes binary ('yes' or 'no') authorization decisions at the site
and resource level, based on grid (X.509) credentials and VOMS attributes.
It has a pluggable interface. This package contains the basic plug-ins.

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
%{_libdir}/lcas/lcas_timeslots.mod
%{_libdir}/lcas/lcas_userallow.mod
%{_libdir}/lcas/lcas_userban.mod
%{_libdir}/lcas/liblcas_timeslots.so
%{_libdir}/lcas/liblcas_userallow.so
%{_libdir}/lcas/liblcas_userban.so

%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 1.3.6-2
- use local custom prefix

* Fri Dec 16 2011 Mischa Salle <msalle@nikhef.nl> 1.3.6-1
- Updated version

* Wed Jul 13 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.5-1
- Updated version

* Tue Jul  5 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.4-3
- Remove Vendor tag

* Fri Mar  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.4-2
- disable static libraries
- fixed license string

* Thu Feb 24 2011 Dennis van Dok <dennisvd@nikhef.nl> 
- Initial build.
