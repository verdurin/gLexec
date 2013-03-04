Summary: AFS plugin for the LCMAPS authorization framework
Name: lcmaps-plugins-afs
Version: 1.4.0
Release: 2%{?dist}
Vendor: Nikhef
License: ASL 2.0
Group: System Environment/Libraries
Prefix:	      /opt/ichep/emi2/glexec/0.9.6
URL: http://www.nikhef.nl/pub/projects/grid/gridwiki/index.php/Site_Access_Control
Source0: http://software.nikhef.nl/security/%{name}/%{name}-%{version}.tar.gz
BuildRequires: lcmaps-interface
BuildRequires: globus-core
BuildRequires: globus-common-devel
BuildRequires: globus-gssapi-gsi-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

This package contains the AFS plug-in.

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
# remove documentation as installed by upstream
make DESTDIR=$RPM_BUILD_ROOT uninstall-docDATA

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/lcmaps/lcmaps_afs.mod
%{_libdir}/lcmaps/liblcmaps_afs.so
%doc AUTHORS LICENSE README.AFS


%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 1.4.0-2
- use local custom prefix

* Thu Dec 15 2011 Mischa Salle <msalle@nikhef.nl> 1.4.0-1
- updated version

* Wed Jul 13 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.11-1
- updated version
- no versioning of plugin

* Wed Mar 23 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.10-2
- removed explicit requires

* Mon Mar  7 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.10-1
- Reduced globus dependencies

* Fri Mar  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.9-2
- fixed license string
- disable static libraries
- dropped separate devel package

* Mon Feb 21 2011 Dennis van Dok <dennisvd@nikhef.nl> 
- Initial build.


