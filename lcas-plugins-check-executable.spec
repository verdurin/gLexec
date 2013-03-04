Summary: Allowed executable plug-in for the LCAS authorization framework
Name: lcas-plugins-check-executable
Version: 1.2.4
Vendor: Nikhef
Release: 2%{?dist}
License: ASL 2.0
Group: System Environment/Libraries
Prefix:	      /opt/ichep/emi2/glexec/0.9.6
URL: http://www.nikhef.nl/pub/projects/grid/gridwiki/index.php/Site_Access_Control
Source0: http://software.nikhef.nl/security/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: globus-common-devel, globus-gssapi-gsi-devel
BuildRequires: lcas-interface

%description

LCAS makes binary ('yes' or 'no') authorization decisions at the site and
resource level, based on grid (X.509) credentials and VOMS attributes. It has a
pluggable interface. This package contains the check-executable plug-ins.

LCAS module that checks whether the executable name found in the RSL (Resource
Specification Language) is the allowed executable or not.

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
%{_libdir}/lcas/lcas_check_executable.mod
%{_libdir}/lcas/liblcas_check_executable.so

%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 1.2.4-2
- use local custom prefix

* Tue Feb 28 2012 Mischa Salle <msalle@nikhef.nl> 1.2.4-1
- cleanup of text to fix rpmlint warnings
- Updated version

* Fri Dec 16 2011 Mischa Salle <msalle@nikhef.nl> 1.2.3-1
- Updated version
- updated installation directory /modules into /lcas
- install .so (no .so.0*)

* Wed Mar 23 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.2.2-3
- removed explicit requires

* Fri Mar  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.2.2-2
- drop devel package
- disabled static libraries
- fixed license string

* Thu Feb 24 2011 Dennis van Dok <dennisvd@nikhef.nl> 
- Initial build.


