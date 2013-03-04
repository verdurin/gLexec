%ifarch alpha ia64 ppc64 s390x sparc64 x86_64
%global flavor gcc64
%else
%global flavor gcc32
%endif

Name:		globus-gss-assist
%global _name %(tr - _ <<< %{name})
Version:	8.6
Release:	2%{?dist}
Summary:	Globus Toolkit - GSSAPI Assist library

Group:		System Environment/Libraries
License:	ASL 2.0
URL:		http://www.globus.org/
Source:		http://www.globus.org/ftppub/gt5/5.2/5.2.2/packages/src/%{_name}-%{version}.tar.gz
#		README file
Source8:	GLOBUS-GSIC
#		This is a workaround for the broken epstopdf script in RHEL5
#		See: https://bugzilla.redhat.com/show_bug.cgi?id=450388
Source9:	epstopdf-2.9.5gw
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	globus-gsi-cert-utils%{?_isa} >= 8
Requires:	globus-gsi-sysconfig%{?_isa} >= 5
Requires:	globus-common%{?_isa} >= 14
Requires:	globus-callout%{?_isa} >= 2
Requires:	globus-gssapi-gsi%{?_isa} >= 9
BuildRequires:	grid-packaging-tools >= 3.4
BuildRequires:	globus-core%{?_isa} >= 8
BuildRequires:	globus-gsi-cert-utils-devel%{?_isa} >= 8
BuildRequires:	globus-gsi-sysconfig-devel%{?_isa} >= 5
BuildRequires:	globus-common-devel%{?_isa} >= 14
BuildRequires:	globus-callout-devel%{?_isa} >= 2
BuildRequires:	globus-gssapi-gsi-devel%{?_isa} >= 9
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

%package progs
Summary:	Globus Toolkit - GSSAPI Assist library Programs
Group:		Applications/Internet
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	globus-common-progs >= 14

%package devel
Summary:	Globus Toolkit - GSSAPI Assist library Development Files
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	globus-gsi-cert-utils-devel%{?_isa} >= 8
Requires:	globus-gsi-sysconfig-devel%{?_isa} >= 5
Requires:	globus-common-devel%{?_isa} >= 14
Requires:	globus-callout-devel%{?_isa} >= 2
Requires:	globus-gssapi-gsi-devel%{?_isa} >= 9
Requires:	globus-core%{?_isa} >= 8

%package doc
Summary:	Globus Toolkit - GSSAPI Assist library Documentation Files
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
GSSAPI Assist library

%description progs
The Globus Toolkit is an open source software toolkit used for building Grid
systems and applications. It is being developed by the Globus Alliance and
many others all over the world. A growing number of projects and companies are
using the Globus Toolkit to unlock the potential of grids for their cause.

The %{name}-progs package contains:
GSSAPI Assist library Programs

%description devel
The Globus Toolkit is an open source software toolkit used for building Grid
systems and applications. It is being developed by the Globus Alliance and
many others all over the world. A growing number of projects and companies are
using the Globus Toolkit to unlock the potential of grids for their cause.

The %{name}-devel package contains:
GSSAPI Assist library Development Files

%description doc
The Globus Toolkit is an open source software toolkit used for building Grid
systems and applications. It is being developed by the Globus Alliance and
many others all over the world. A growing number of projects and companies are
using the Globus Toolkit to unlock the potential of grids for their cause.

The %{name}-doc package contains:
GSSAPI Assist library Documentation Files

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

# Move client man pages to progs package
grep '.[18]$' $GLOBUSPACKAGEDIR/%{_name}/noflavor_doc.filelist \
  >> $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_pgm.filelist
sed '/.[18]$/d' -i $GLOBUSPACKAGEDIR/%{_name}/noflavor_doc.filelist

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
cat $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_pgm.filelist \
  | sed -e s!^!%{_prefix}! -e 's!.*/man/.*!%doc &*!' > package-progs.filelist
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

%files -f package-progs.filelist progs
%defattr(-,root,root,-)

%files -f package-devel.filelist devel
%defattr(-,root,root,-)

%files -f package-doc.filelist doc
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}-%{version}/html

%changelog
* Mon Mar  4 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 8.6-2
- Use local prefix

* Sun Jul 22 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.6-1
- Update to Globus Toolkit 5.2.2
- Drop patch globus-gss-assist-mingw.patch (fixed upstream)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.5-1
- Update to Globus Toolkit 5.2.1
- Drop patches globus-gss-assist-doxygen.patch, globus-gss-assist-deps.patch
  and globus-gss-assist-format.patch (fixed upstream)

* Tue Jan 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.1-2
- Fix broken links in README file

* Wed Dec 14 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.1-1
- Update to Globus Toolkit 5.2.0
- Drop patches globus-gss-assist-normalization.patch and
  globus-gss-assist-gridmapdir.patch (fixed upstream)

* Fri Jun 03 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.10-1
- Update to Globus Toolkit 5.0.4
- Fix doxygen markup

* Sun Apr 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-4
- Add README file

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 18 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-2
- Move client man pages to progs package

* Sat Jul 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-1
- Update to Globus Toolkit 5.0.2

* Wed Apr 14 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.8-1
- Update to Globus Toolkit 5.0.1

* Fri Jan 22 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.5-1
- Update to Globus Toolkit 5.0.0

* Thu Jul 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-3
- Add instruction set architecture (isa) tags
- Make doc subpackage noarch

* Wed Jun 03 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-2
- Update to official Fedora Globus packaging guidelines

* Thu Apr 16 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-1
- Make comment about source retrieval more explicit
- Change defines to globals
- Remove explicit requires on library packages
- Put GLOBUS_LICENSE file in extracted source tarball

* Sun Mar 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-0.5
- Adapting to updated globus-core package

* Thu Feb 26 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-0.4
- Add s390x to the list of 64 bit platforms

* Thu Jan 01 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-0.3
- Adapt to updated GPT package

* Wed Oct 15 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.0-0.2
- Update to Globus Toolkit 4.2.1

* Mon Jul 14 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.25-0.1
- Autogenerated
