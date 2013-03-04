%ifarch alpha ia64 ppc64 s390x sparc64 x86_64
%global flavor gcc64
%else
%global flavor gcc32
%endif

%{!?perl_vendorlib: %global perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)}

Name:		globus-common
%global _name %(tr - _ <<< %{name})
Version:	14.7
Release:	2%{?dist}
Summary:	Globus Toolkit - Common Library

Group:		System Environment/Libraries
Prefix:		/opt/ichep/emi2/glexec/0.9.6
License:	ASL 2.0
URL:		http://www.globus.org/
Source:		http://www.globus.org/ftppub/gt5/5.2/5.2.2/packages/src/%{_name}-%{version}.tar.gz
#		README file
Source8:	GLOBUS-CCOMMONLIB
#		This is a workaround for the broken epstopdf script in RHEL5
#		See: https://bugzilla.redhat.com/show_bug.cgi?id=450388
Source9:	epstopdf-2.9.5gw
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
#		Obsolete dropped packages from Globus Toolkit 4.2.1
Obsoletes:	globus-data-conversion
Obsoletes:	globus-mp
Obsoletes:	globus-nexus
Obsoletes:	globus-duct-common
Obsoletes:	globus-duct-control
Obsoletes:	globus-duroc-common
Obsoletes:	globus-duroc-control
#		Obsolete dropped packages from Globus Toolkit 5.2.0
Provides:	globus-libtool = 2
Provides:	globus-libtool%{?_isa} = 2
Obsoletes:	globus-libtool < 2
Provides:	globus-openssl = 6
Provides:	globus-openssl%{?_isa} = 6
Obsoletes:	globus-openssl < 6
Provides:	globus-libxml2 = 2
Provides:	globus-libxml2%{?_isa} = 2
Obsoletes:	globus-libxml2 < 2
BuildRequires:	grid-packaging-tools >= 3.4
BuildRequires:	globus-core%{?_isa} >= 8
%if %{?fedora}%{!?fedora:0} >= 4 || %{?rhel}%{!?rhel:0} >= 5
BuildRequires:	libtool-ltdl-devel%{?_isa}
%else
BuildRequires:	libtool
%endif
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
Summary:	Globus Toolkit - Common Library Programs
Group:		Applications/Internet
#		Keep providing globus-common-setup until it is not needed
Provides:	%{name}-setup = 2.6
Requires:	%{name}%{?_isa} = %{version}-%{release}
#		Obsolete dropped packages from Globus Toolkit 5.2.0
Provides:	globus-openssl-progs = 6
Provides:	globus-openssl-progs%{?_isa} = 6
Obsoletes:	globus-openssl-progs < 6

%package devel
Summary:	Globus Toolkit - Common Library Development Files
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	%{name}-progs%{?_isa} = %{version}-%{release}
Requires:	globus-core%{?_isa} >= 8
#		Obsolete dropped packages from Globus Toolkit 4.2.1
Obsoletes:	globus-data-conversion-devel
Obsoletes:	globus-mp-devel
Obsoletes:	globus-nexus-devel
Obsoletes:	globus-duct-common-devel
Obsoletes:	globus-duct-control-devel
Obsoletes:	globus-duroc-common-devel
Obsoletes:	globus-duroc-control-devel
#		Obsolete dropped packages from Globus Toolkit 5.2.0
Provides:	globus-libtool-devel = 2
Provides:	globus-libtool-devel%{?_isa} = 2
Provides:	pkgconfig(globus-libtool) = 2
Obsoletes:	globus-libtool-devel < 2
Provides:	globus-openssl-devel = 6
Provides:	globus-openssl-devel%{?_isa} = 6
Provides:	pkgconfig(globus-openssl) = 6
Obsoletes:	globus-openssl-devel < 6
Provides:	globus-libxml2-devel = 2
Provides:	globus-libxml2-devel%{?_isa} = 2
Provides:	pkgconfig(globus-libxml2) = 2
Obsoletes:	globus-libxml2-devel < 2

%package doc
Summary:	Globus Toolkit - Common Library Documentation Files
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
Common Library

%description progs
The Globus Toolkit is an open source software toolkit used for building Grid
systems and applications. It is being developed by the Globus Alliance and
many others all over the world. A growing number of projects and companies are
using the Globus Toolkit to unlock the potential of grids for their cause.

The %{name}-progs package contains:
Common Library Programs

%description devel
The Globus Toolkit is an open source software toolkit used for building Grid
systems and applications. It is being developed by the Globus Alliance and
many others all over the world. A growing number of projects and companies are
using the Globus Toolkit to unlock the potential of grids for their cause.

The %{name}-devel package contains:
Common Library Development Files

%description doc
The Globus Toolkit is an open source software toolkit used for building Grid
systems and applications. It is being developed by the Globus Alliance and
many others all over the world. A growing number of projects and companies are
using the Globus Toolkit to unlock the potential of grids for their cause.

The %{name}-doc package contains:
Common Library Documentation Files

%prep
%setup -q -n %{_name}-%{version}

# custom perl requires that removes dependency on gpt perl modules
cat << EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(Grid::GPT::.*)/d'
EOF
%global __perl_requires %{_builddir}/%{_name}-%{version}/%{name}-req
chmod +x %{__perl_requires}

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

export GLOBUS_VERSION=5.2.2
%configure --disable-static --with-flavor=%{flavor} \
	   --enable-doxygen --with-docdir=%{_docdir}/%{name}-%{version} \
	   --with-backward-compatibility-hack

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

# These scripts are intended to be sourced, not executed
chmod 644 $RPM_BUILD_ROOT%{_datadir}/globus/globus-args-parser-header
chmod 644 $RPM_BUILD_ROOT%{_datadir}/globus/globus-script-initializer
chmod 644 $RPM_BUILD_ROOT%{_datadir}/globus/globus-sh-tools.sh

# Remove libtool archives (.la files)
find $RPM_BUILD_ROOT%{_libdir} -name 'libglobus_common.la' -exec rm -v '{}' \;
sed '/libglobus_common.la$/d' \
  -i $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_dev.filelist

# This library is opened using lt_dlopenext, so the libtool archive
# (.la file) can not be removed - fix the libdir and clear dependency_libs
# ... and move it to the main package
for lib in `find $RPM_BUILD_ROOT%{_libdir} -name 'libglobus_thread_*.la'` ; do
  sed -e "s!^libdir=.*!libdir=\'%{_libdir}\'!" \
      -e "s!^dependency_libs=.*!dependency_libs=\'\'!" -i $lib
done
grep 'libglobus_thread_.*\.la$' \
  $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_dev.filelist \
  >> $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_rtl.filelist
sed '/libglobus_thread_.*\.la$/d' \
  -i $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_dev.filelist

# Move globus-makefile-header to devel package
grep globus-makefile-header $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_pgm.filelist \
  >> $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_dev.filelist
sed /globus-makefile-header/d \
  -i $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_pgm.filelist

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

# Remove deprecated.3 man page (too common name)
rm -f $RPM_BUILD_ROOT%{_mandir}/man3/deprecated.3
sed -e '/deprecated\.3/d' -i $GLOBUSPACKAGEDIR/%{_name}/noflavor_doc.filelist

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
%dir %{_datadir}/globus
%dir %{_datadir}/globus/packages
%dir %{_datadir}/globus/packages/%{_name}
%dir %{perl_vendorlib}/Globus
%dir %{perl_vendorlib}/Globus/Core
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/README

%files -f package-progs.filelist progs
%defattr(-,root,root,-)

%files -f package-devel.filelist devel
%defattr(-,root,root,-)
%dir %{_includedir}/globus

%files -f package-doc.filelist doc
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}-%{version}/html

%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 14.7-2
- Use local custom prefix for glexec

* Sun Jul 22 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.7-1
- Update to Globus Toolkit 5.2.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 14.6-2
- Perl 5.16 rebuild

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.6-1
- Update to Globus Toolkit 5.2.1
- Drop patches globus-common-initializers.patch, globus-common-format.patch,
  globus-common-doxygen.patch and globus-common-sh-env.patch implemented
  upstream
- Drop manpages from packaging that are now included in upstream sources

* Thu Feb 02 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.5-4
- Add missing default to GLOBUS_SH_* variables

* Sat Jan 28 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.5-3
- Add dependency on -progs to -devel for globus-makefile-header

* Mon Jan 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.5-2
- Fix broken links in README file

* Tue Dec 13 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 14.5-1
- Update to Globus Toolkit 5.2.0
- Drop patches implemented upstream

* Sun Oct 02 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.6-5
- Add contributed manpages

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 11.6-4
- Perl mass rebuild

* Fri Jun 10 2011 Marcela Mašláňová <mmaslano@redhat.com> - 11.6-3
- Perl 5.14 mass rebuild

* Sun Apr 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.6-2
- Add README file

* Wed Feb 23 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.6-1
- Update to Globus Toolkit 5.0.3
- Try to ensure that most of globus-sh-tools-vars.sh gets filled

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 06 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.5-3
- Updated pthread exception patch for better compatibility with boost's headers

* Sun Aug 08 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.5-2
- Fix perl dependncies (use vs. require)

* Sat Jul 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.5-1
- Update to Globus Toolkit 5.0.2

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 11.4-2
- Mass rebuild with perl-5.12.0

* Tue Apr 13 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.4-1
- Update to Globus Toolkit 5.0.1

* Wed Feb 24 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.2-2
- Make the globus-version script return the right value

* Thu Jan 21 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 11.2-1
- Update to Globus Toolkit 5.0.0

* Fri Dec 04 2009 Stepan Kasal <skasal@redhat.com> - 10.2-9
- rebuild against perl 5.10.1

* Sun Nov 08 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-8
- Let globus-makefile-header fail gracefully when GPT is not present
- Workaround a bug in doxygen

* Mon Aug 03 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-7
- Patch globus_location function to allow unset GLOBUS_LOCATION
- Put back config.guess file

* Thu Jul 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-6
- Add instruction set architecture (isa) tags
- Make doc subpackage noarch
- Replace /usr/bin/env shebangs

* Tue Jun 02 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-5
- Update to official Fedora Globus packaging guidelines

* Mon Apr 27 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-4
- Rebuild with updated libtool

* Tue Apr 21 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-3
- Put GLOBUS_LICENSE file in extracted source tarball

* Thu Apr 16 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-2
- Remove config.guess file

* Tue Apr 07 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-1
- Change defines to globals

* Mon Apr 06 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-0.6
- Make comment about source retrieval more explicit

* Sun Mar 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-0.5
- Adapting to updated globus-core package

* Thu Feb 26 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-0.4
- Add s390x to the list of 64 bit platforms
- Move globus-makefile-header to devel package

* Thu Jan 01 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-0.3
- Adapt to updated GPT package

* Wed Oct 15 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-0.2
- Update to Globus Toolkit 4.2.1

* Mon Jul 14 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.2-0.1
- Autogenerated
