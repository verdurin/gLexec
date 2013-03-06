%ifarch alpha ia64 ppc64 s390x sparc64 x86_64
%global flavor gcc64
%global enable64 yes
%else
%global flavor gcc32
%global enable64 no
%endif

%global debug_package %{nil}

%{!?perl_vendorlib: %global perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)}

Name:		globus-core
%global _name %(tr - _ <<< %{name})
Version:	8.9
Release:	3%{?dist}
Summary:	Globus Toolkit - Globus Core

Group:		Development/Tools
Prefix:		/opt/ichep/emi2/glexec/0.9.6
License:	ASL 2.0
URL:		http://www.globus.org/
Source:		http://www.globus.org/ftppub/gt5/5.2/5.2.2/packages/src/%{_name}-%{version}.tar.gz
#		README file
Source8:	GLOBUS-CCOMMONLIB
Patch0:		%{name}-texlive-2012.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	pkgconfig
Requires:	perl(XML::Parser)
BuildRequires:	grid-packaging-tools >= 3.4
BuildRequires:	perl(XML::Parser)

%description
The Globus Toolkit is an open source software toolkit used for building Grid
systems and applications. It is being developed by the Globus Alliance and
many others all over the world. A growing number of projects and companies are
using the Globus Toolkit to unlock the potential of grids for their cause.

The %{name} package contains:
Globus Core

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

sed 's/5.2.0/5.2.3/' -i scripts/globus-spec-creator
sed 's/ -L$libdir//' -i config/accompiler.m4

# custom perl requires that removes dependency on gpt perl modules
cat << EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '/perl(Grid::GPT::.*)/d'
EOF
%global __perl_requires %{_builddir}/%{_name}-%{version}/%{name}-req
chmod +x %{__perl_requires}

%build
# Remove files that should be replaced during bootstrap
rm -rf autom4te.cache

unset GLOBUS_LOCATION
unset GPT_LOCATION
./bootstrap

# Reduce overlinking
export LDFLAGS="-Wl,--as-needed %{?__global_ldflags}"

%configure --disable-static --with-flavor=%{flavor} \
	   --enable-64bit=%{enable64} \
	   --enable-debug \
	   --includedir='${prefix}/include/globus' \
	   --libexecdir='${datadir}/globus' \
	   --with-setupdir='${datadir}/globus/setup' \
	   --with-testdir='${datadir}/globus/test/${PACKAGE}' \
	   --with-flavorincludedir='${libdir}/globus/include' \
	   --with-perlmoduledir=%{perl_vendorlib} \
	   --with-doxygendir='${datadir}/globus/doxygen' \
	   --with-docdir=%{_docdir}/%{name}-%{version} \
	   --with-initializer-libdir-based-on-machine-type

# Reduce overlinking
sed 's!CC -shared !CC \${wl}--as-needed -shared !g' -i libtool

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# These scripts are intended to be sourced, not executed
chmod 644 %{buildroot}%{_datadir}/globus/globus-build-env-*.sh

GLOBUSPACKAGEDIR=%{buildroot}%{_datadir}/globus/packages

# Don't use /usr/bin/env
sed 's!/usr/bin/env perl!/usr/bin/perl!' -i %{buildroot}%{_sbindir}/globus-*

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_docdir}/%{name}-%{version}/README

# Generate package filelists
cat $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_pgm.filelist \
    $GLOBUSPACKAGEDIR/%{_name}/%{flavor}_dev.filelist \
    $GLOBUSPACKAGEDIR/%{_name}/noflavor_data.filelist \
  | sed s!^!%{_prefix}! > package.filelist
cat $GLOBUSPACKAGEDIR/%{_name}/noflavor_doc.filelist \
  | sed -e 's!/man/.*!&*!' -e 's!^!%doc %{_prefix}!' >> package.filelist

%clean
rm -rf %{buildroot}

%files -f package.filelist
%defattr(-,root,root,-)
%dir %{_datadir}/globus
%dir %{_datadir}/globus/aclocal
%dir %{_datadir}/globus/doxygen
%dir %{_datadir}/globus/flavors
%dir %{_datadir}/globus/packages
%dir %{_datadir}/globus/packages/%{_name}
%dir %{_libdir}/globus
%dir %{_libdir}/globus/include
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/README

%changelog
* Tue Mar  5 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 8.9-3
- use local prefix

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.9-2
- Fix globus-spec-creator for TexLive 2012 (Fedora 18+)

* Sun Jul 22 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.9-1
- Update to Globus Toolkit 5.2.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.8-1
- Update to Globus Toolkit 5.2.1
- Drop patch globus-core-openssl.patch (fixed upstream)

* Mon Jan 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.5-2
- Fix broken links in README file

* Tue Dec 13 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 8.5-1
- Update to Globus Toolkit 5.2.0
- Drop patches implemented upstream
- Drop the globus-gpt2pkg-config script (now part of grid-packaging-tools)
- Drop the globus-spec-creator script (now part of the upstream package)

* Sun Apr 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.17-3
- Update globus-spec-creator script
- Add README file

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.17-1
- Update to Globus Toolkit 5.0.2

* Mon Apr 12 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.16-1
- Update to Globus Toolkit 5.0.1

* Thu Jan 21 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.15-8
- Update to Globus Toolkit 5.0.0

* Mon Dec 07 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.15-7
- rebuild against perl 5.10.1

* Thu Jul 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.15-6
- The globus-spec-creator script now uses isa tags and noarch doc subpackages
- Replace /usr/bin/env shebangs

* Tue Jun 02 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.15-5
- Update to official Fedora Globus packaging guidelines
- Fix build configuration for s390x and kfreebsd
- Make globus-core work with automake 1.11

* Mon Apr 27 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.15-4
- Install the globus-spec-creator script
- Add -Wl,--as-needed to the libtool script

* Tue Apr 21 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.15-3
- Update after clarification of packaging guidelines

* Wed Apr 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.15-2
- Make comment about source retrieval more explicit

* Fri Mar 20 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.15-1
- Change defines to globals

* Sun Mar 15 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.15-0.5
- Merge devel with main

* Thu Feb 26 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.15-0.4
- Add s390x to the list of 64 bit platforms

* Mon Dec 29 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.15-0.3
- Adapt to updated GPT package

* Sun Oct 12 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.15-0.2
- Update to Globus Toolkit 4.2.1

* Mon Jul 14 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.14-0.1
- Autogenerated
