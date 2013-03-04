Summary: Groupid tracking plugin for the LCMAPS authorization framework
Name: lcmaps-plugins-tracking-groupid
Version: 0.1.0
Release: 2%{?dist}
License: ASL 2.0
Group: System Environment/Libraries
Prefix:	      /opt/ichep/emi2/glexec/0.9.6
URL: http://www.nikhef.nl/pub/projects/grid/gridwiki/index.php/Site_Access_Control
Source0: http://software.nikhef.nl/security/%{name}/%{name}-%{version}.tar.gz
BuildRequires: lcmaps-interface

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

This package contains the tracking group ID plug-in. This plug-in will
add one or more secondary Group IDs to the final mapping result. Some
batch systems can be configured to add a unique group ID to a batch
job to be able to track its movements; this should be preserved even
across user ID switches through LCMAPS.

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
%{_libdir}/lcmaps/lcmaps_tracking_groupid.mod
%{_libdir}/lcmaps/liblcmaps_tracking_groupid.so
%{_datadir}/man/man8/lcmaps_tracking_groupid.mod.8.gz


%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 0.1.0-2
- use local custom prefix

* Thu Dec 15 2011 Mischa Salle <msalle@nikhef.nl> 0.1.0-1
- updated version

* Fri Jul 15 2011 Dennis van Dok <dennisvd@nikhef.nl> 0.0.2-1
- removed vendor tag
- disabled versioning
- changed moduledir

* Wed Apr  6 2011 Dennis van Dok <dennisvd@nikhef.nl> 0.0.1-1
- Initial build

