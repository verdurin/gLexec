Summary: Authorization service for grid credentials
Name: lcas
Version: 1.3.18
Release: 3%{?dist}
License: ASL 2.0
Group: System Environment/Libraries
Prefix: /opt/ichep/emi2/glexec/0.9.6
URL: http://www.nikhef.nl/pub/projects/grid/gridwiki/index.php/Site_Access_Control
Source0: http://software.nikhef.nl/security/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: globus-core
BuildRequires: globus-common-devel
BuildRequires: globus-gsi-credential-devel
BuildRequires: globus-gssapi-gsi-devel
BuildRequires: openssl-devel

%description
LCAS makes binary ('yes' or 'no') authorization decisions at the site
and resource level. In making this decision, it can use a variety of
inputs: the 'grid' name of the user (the Subject Distinguished Name),
any VO attributes the user has (like VOMS FQANs), the name of the
executable the user intends to execute. It supports basic black and
white list functionality, but also more complex VOMS-based
expressions, based on the GACL language.

%package interface
Group: Development/Libraries
Summary: LCAS plug-in API header files
Requires: globus-gssapi-gsi-devel
Requires: pkgconfig
%if %{?fedora}%{!?fedora:0} >= 10 || %{?rhel}%{!?rhel:0} >= 6
BuildArch: noarch
%endif

%description interface
This package contains the interface, needed to build plug-ins for
LCAS.

%package devel
Group: Development/Libraries
Summary: LCAS development libraries
Requires: %{name}-interface = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: globus-gssapi-gsi-devel

%description devel
This package contains the development libraries for LCAS.

%prep
%setup -q

%build

%configure --disable-static

# The following two lines were suggested by
# https://fedoraproject.org/wiki/Packaging/Guidelines to prevent any
# RPATHs creeping in.
# sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
# sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# remove the files we don't want
rm -rf %{buildroot}%{_docdir}
rm %{buildroot}%{_libdir}/%{name}/lcas_plugin_example.mod
rm %{buildroot}%{_libdir}/%{name}/liblcas_plugin_example.so
# next list is basically a bug in LCAS itself: these files are examples and
# should be installed as such, also the directory is wrong
rm %{buildroot}%{_sysconfdir}/allowed_users.db.in
rm %{buildroot}%{_sysconfdir}/ban_users.db.in
rm %{buildroot}%{_sysconfdir}/lcas.db.in
rm %{buildroot}%{_sysconfdir}/lcas_voms.gacl.in
rm %{buildroot}%{_sysconfdir}/timeslots.db.in
# Do create the proper directory for db files.
mkdir %{buildroot}%{_sysconfdir}/%{name}
# Cope with non-standard doc location
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-%{version}
cp INSTALL LICENSE README %{buildroot}%{_defaultdocdir}/%{name}-%{version}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# This library is sometimes dlopened, so the .so symlink cannot be in devel
%{_libdir}/liblcas.so
%{_libdir}/liblcas.so.0
%{_libdir}/liblcas.so.0.0.0
%dir %{_libdir}/%{name}
%dir %{_sysconfdir}/%{name}
# %%doc INSTALL LICENSE README
%{_defaultdocdir}/%{name}-%{version}

%files interface
%defattr(-,root,root,-)
%{_includedir}/lcas
%{_datadir}/pkgconfig/lcas-interface.pc
%%doc LICENSE
%{_defaultdocdir}/%{name}-%{version}/LICENSE

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/lcas.pc

%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 1.3.18-3
- change docs location for local layout

* Fri Mar  9 2012 Mischa Salle <msalle@nikhef.nl> 1.3.18-2
- %%configure should NOT override the sysconfdir
- don't install example config files (certainly not in %%sysconfdir)
- Bumped version

* Tue Feb 28 2012 Mischa Salle <msalle@nikhef.nl> 1.3.17-1
- Bumped version

* Mon Jan 30 2012 Mischa Salle <msalle@nikhef.nl> 1.3.16-1
- Bumped version

* Fri Dec 16 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.15-2
- Added openssl-devel build dependency

* Fri Dec 16 2011 Mischa Salle <msalle@nikhef.nl> 1.3.15-1
- Updated version

* Wed Jul 13 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.14-1
- Bumped version

* Mon Jul  4 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.13-3
- Make interface package noarch
- Remove Vendor tag

* Wed Mar 23 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.13-2
- removed explicit requires

* Mon Mar  7 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.13-1
- bumped to version 1.3.13
- Added globus-gssapi-gsi-devel dependency on devel pkg
- Reduced globus dependencies to minimum

* Fri Mar  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.12-5
- Added post(un) ldconfig scripts
- disable static libraries
- fixed license string

* Thu Mar  3 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.3.12-4
- Fixed typo in summary

* Thu Feb 24 2011 Dennis van Dok <dennisvd@nikhef.nl> 
- Initial build.
