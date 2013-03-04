%ifarch alpha ia64 ppc64 s390x sparc64 x86_64
%global flavor gcc64
%else
%global flavor gcc32
%endif

Name:		globus-gsi-credential
%global _name %(tr - _ <<< %{name})
Version:	5.3
Release:	2%{?dist}
Summary:	Globus Toolkit - Globus GSI Credential Library

Group:		System Environment/Libraries
License:	ASL 2.0
Prefix:		/opt/ichep/emi2/glexec/0.9.6
URL:		http://www.globus.org/
Source:		http://www.globus.org/ftppub/gt5/5.2/5.2.1/packages/src/%{_name}-%{version}.tar.gz
#		README file
Source8:	GLOBUS-GSIC
#		This is a workaround for the broken epstopdf script in RHEL5
#		See: https://bugzilla.redhat.com/show_bug.cgi?id=450388
Source9:	epstopdf-2.9.5gw
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	globus-gsi-cert-utils%{?_isa} >= 8
Requires:	globus-gsi-proxy-ssl%{?_isa} >= 4
Requires:	globus-gsi-callback%{?_isa} >= 4
Requires:	globus-gsi-sysconfig%{?_isa} >= 5
Requires:	globus-common%{?_isa} >= 14
Requires:	globus-gsi-openssl-error%{?_isa} >= 2
BuildRequires:	grid-packaging-tools >= 3.4
BuildRequires:	globus-core%{?_isa} >= 8
BuildRequires:	globus-gsi-cert-utils-devel%{?_isa} >= 8
BuildRequires:	globus-gsi-proxy-ssl-devel%{?_isa} >= 4
BuildRequires:	globus-gsi-callback-devel%{?_isa} >= 4
BuildRequires:	globus-gsi-sysconfig-devel%{?_isa} >= 5
BuildRequires:	globus-common-devel%{?_isa} >= 14
BuildRequires:	globus-gsi-openssl-error-devel%{?_isa} >= 2
BuildRequires:	openssl-devel%{?_isa}
BuildRequires:	doxygen
BuildRequires:	graphviz
%if "%{?rhel}" == "5"
BuildRequires:	graphviz-gd
%endif
BuildRequires:	ghostscript
%if %{?fedora}%{!?fedora:0} >= 9 || %{?rhel}%{!?rhel:0} >= 5
BuildRequires:	tex(latex)
%else
BuildRequires:	tetex-latex
%endif

%package devel
Summary:	Globus Toolkit - Globus GSI Credential Library Development Files
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	globus-gsi-cert-utils-devel%{?_isa} >= 8
Requires:	globus-gsi-proxy-ssl-devel%{?_isa} >= 4
Requires:	globus-gsi-callback-devel%{?_isa} >= 4
Requires:	globus-gsi-sysconfig-devel%{?_isa} >= 5
Requires:	globus-common-devel%{?_isa} >= 14
Requires:	globus-gsi-openssl-error-devel%{?_isa} >= 2
Requires:	globus-core%{?_isa} >= 8
Requires:	openssl-devel%{?_isa}

%package doc
Summary:	Globus Toolkit - Globus GSI Credential Library Documentation Files
Group:		Documentation
%if %{?fedora}%{!?fedora:0} >= 10 || %{?rhel}%{!?rhel:0} >= 6
BuildArch:	noarch
%endif
Requires:	%{name} = %{version}-%{release}

%description
The Globus Toolkit is an open source software toolkit used for building Grid
systems and applications. It is being developed by the Globus Alliance and
many others all over the world. A growing number of projects and companies are
using the Globus Toolkit to unlock the potential of grids for their cause.

The %{name} package contains:
Globus GSI Credential Library

%description devel
The Globus Toolkit is an open source software toolkit used for building Grid
systems and applications. It is being developed by the Globus Alliance and
many others all over the world. A growing number of projects and companies are
using the Globus Toolkit to unlock the potential of grids for their cause.

The %{name}-devel package contains:
Globus GSI Credential Library Development Files

%description doc
The Globus Toolkit is an open source software toolkit used for building Grid
systems and applications. It is being developed by the Globus Alliance and
many others all over the world. A growing number of projects and companies are
using the Globus Toolkit to unlock the potential of grids for their cause.

The %{name}-doc package contains:
Globus GSI Credential Library Documentation Files

%prep
%setup -q -n %{_name}-%{version}

%if "%{rhel}" == "5"
mkdir bin
install %{SOURCE9} bin/epstopdf
%endif

%build
%if "%{rhel}" == "5"
export PATH=$PWD/bin:$PATH
%endif

# Remove files that should be replaced during bootstrap
rm -f doxygen/Doxyfile*
rm -f doxygen/Makefile.am
rm -f pkgdata/Makefile.am
rm -f globus_automake*
rm -rf autom4te.cache

unset GLOBUS_LOCATION
unset GPT_LOCATION
%{_datadir}/globus/globus-bootstrap.sh

%configure --disable-static --with-flavor=%{flavor} \
	   --enable-doxygen --with-docdir=%{_docdir}/%{name}-%{version}

# Reduce overlinking
sed 's!CC -shared !CC \${wl}--as-needed -shared !g' -i libtool

make %{?_smp_mflags}

%install
%if "%{rhel}" == "5"
export PATH=$PWD/bin:$PATH
%endif

rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

GLOBUSPACKAGEDIR=$RPM_BUILD_ROOT%{_datadir}/globus/packages

# Remove libtool archives (.la files)
find $RPM_BUILD_ROOT%{_libdir} -name 'lib*.la' -exec rm -v '{}' \;
sed '/lib.*\.la$/d' -i $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_dev.filelist

# Move license file to main package
grep GLOBUS_LICENSE $GLOBUSPACKAGEDIR/%{_name}/noflavor_doc.filelist \
  >> $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_rtl.filelist
sed /GLOBUS_LICENSE/d -i $GLOBUSPACKAGEDIR/%{_name}/noflavor_doc.filelist

# Remove unwanted documentation (needed for RHEL4)
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/*_%{_name}-%{version}_*.3
sed -e '/_%{_name}-%{version}_.*\.3/d' \
  -i $GLOBUSPACKAGEDIR/%{_name}/noflavor_doc.filelist

# Install README file
install -m 644 -p %{SOURCE8} \
  $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/README

# Generate package filelists
cat $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_rtl.filelist \
  | sed s!^!%{_prefix}! > package.filelist
cat $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_dev.filelist \
  | sed s!^!%{_prefix}! > package-devel.filelist
cat $GLOBUSPACKAGEDIR/%{_name}/noflavor_doc.filelist \
  | sed -e 's!/man/.*!&*!' -e 's!^!%doc %{_prefix}!' > package-doc.filelist

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f package.filelist
%defattr(-,root,root,-)
%dir %{_datadir}/globus/packages/%{_name}
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/README

%files -f package-devel.filelist devel
%defattr(-,root,root,-)

%files -f package-doc.filelist doc
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}-%{version}/html

%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 5.3-2
- Use local custom prefix

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.3-1
- Update to Globus Toolkit 5.2.1
- Drop patch globus-gsi-credential-deps.patch (fixed upstream)

* Mon Jan 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.1-2
- Fix broken links in README file

* Tue Dec 13 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.1-1
- Update to Globus Toolkit 5.2.0

* Sun Apr 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.5-3
- Add README file

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.5-1
- Update to Globus Toolkit 5.0.2
- Drop patch globus-gsi-credential-oid.patch (fixed upstream)

* Mon May 31 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.3-2
- Fix OID registration pollution

* Wed Apr 14 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.3-1
- Update to Globus Toolkit 5.0.1
- Drop patch globus-gsi-credential-openssl.patch (fixed upstream)

* Fri Jan 22 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.2-1
- Update to Globus Toolkit 5.0.0

* Sat Aug 22 2009 Tomas Mraz <tmraz@redhat.com> - 2.2-4
- rebuilt with new openssl

* Thu Jul 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-3
- Add instruction set architecture (isa) tags
- Make doc subpackage noarch

* Wed Jun 03 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-2
- Update to official Fedora Globus packaging guidelines

* Thu Apr 16 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-1
- Make comment about source retrieval more explicit
- Change defines to globals
- Remove explicit requires on library packages
- Put GLOBUS_LICENSE file in extracted source tarball

* Sun Mar 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-0.5
- Adapting to updated globus-core package

* Thu Feb 26 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-0.4
- Add s390x to the list of 64 bit platforms

* Thu Jan 01 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-0.3
- Adapt to updated GPT package

* Wed Oct 15 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.2-0.2
- Update to Globus Toolkit 4.2.1

* Mon Jul 14 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0-0.1
- Autogenerated
