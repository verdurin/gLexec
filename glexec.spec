Summary: User identity switching tool based on grid credentials
Name: glexec
Version: 0.9.6
Release: 2%{?dist}
License: ASL 2.0
Group: Applications/System
Prefix: /opt/ichep/emi2/glexec/0.9.6
URL: http://www.nikhef.nl/pub/projects/grid/gridwiki/index.php/Site_Access_Control
Source0: http://software.nikhef.nl/security/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: lcmaps-basic-interface >= 1.4.31
Requires: logrotate

# Since liblcmaps.so is dlopen'd we need this explicit requirement.
Requires: lcmaps
Requires(pre): shadow-utils

%description
gLExec is a program that acts as a light-weight 'gatekeeper'. it takes
Grid credentials as input, and takes the local site policy into
account to authenticate and authorize the credentials. It will then
switch to a new execution sandbox and execute the given command as the
switched identity. gLExec is also capable of functioning as a
light-weight control point which offers a binary yes/no result in
logging-only mode.

%prep
%setup -q

%build
%configure --with-lcmaps-moduledir-sfx=/lcmaps --with-lcas-moduledir-sfx=/lcas

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make DESTDIR=%{buildroot} install
chmod u+r %{buildroot}%{_sbindir}/glexec

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE 
%config(noreplace) %{_sysconfdir}/logrotate.d/glexec
%attr(600, glexec, root) %config(noreplace) %{_sysconfdir}/glexec.conf
%config(noreplace) %{_sysconfdir}/lcmaps/lcmaps-glexec.db
%{_datadir}/man/man5/glexec.conf.5*
%{_datadir}/man/man1/glexec.1*
%{_datadir}/man/man8/glexec-configure.8*
%attr(4111, root, root) %{_sbindir}/glexec
%attr(755, root, root) %{_sbindir}/glexec-configure


# Add the glexec group and user (see http://fedoraproject.org/wiki/Packaging:UsersAndGroups)
%pre
getent group glexec >/dev/null || groupadd -r glexec
getent passwd glexec >/dev/null || \
    useradd -r -g glexec -d / -s /sbin/nologin \
    -c "gLExec user account to be used with %{_sbindir}/glexec" glexec
exit 0

%changelog
* Fri Jan 25 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 0.9.6-2
- use local prefix

* Sun Apr  1 2012 Mischa Salle <msalle@nikhef.nl> 0.9.6-1
- updating version

* Mon Mar 26 2012 Mischa Salle <msalle@nikhef.nl> 0.9.5-1
- updating version

* Fri Mar 16 2012 Mischa Salle <msalle@nikhef.nl> 0.9.4-1
- updating version

* Tue Feb 28 2012 Mischa Salle <msalle@nikhef.nl> 0.9.3-1
- fixing macros in ChangeLog and commented-out release
- updating version

* Mon Feb 27 2012 Mischa Salle <msalle@nikhef.nl> 0.9.2-1
- add manpage for glexec-configure
- updating version

* Mon Feb 20 2012 Mischa Salle <msalle@nikhef.nl> 0.9.1-2
- new install permissions on binary, should be chmod u+r in install phase
- updating version

* Wed Dec 14 2011 Mischa Salle <msalle@nikhef.nl> 0.9.0-1
- add installation of glexec-configure

* Mon Aug 15 2011 Mischa Salle <msalle@nikhef.nl> 0.8.12-3
- sbindir should have been _sbindir in useradd
- Need minimal lcmaps-basic-interface 1.4.31
- Format for testing release (commented-out)

* Thu Jul 21 2011 Mischa Salle <msalle@nikhef.nl> 0.8.11-2
- use the new --with-lcmaps-moduledir-sfx and --with-lcas-moduledir-sfx
  configure options instead of the --with-lcmaps-moduledir.

* Wed Jul 20 2011 Mischa Salle <msalle@nikhef.nl> 0.8.11-1
- use %%{_sysconfdir} instead of /etc in the %%files list

* Thu Jul 14 2011 Dennis van Dok <dennisvd@nikhef.nl> 0.8.10-2
- change lcmaps moduledir according to new schema
- fix the permissions of the configuration file
- create a glexec account on demand

* Wed Jun 29 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.8.10-1
- Remove Vendor tag

* Mon Mar 14 2011 Dennis van Dok <dennisvd@nikhef.nl> 0.8.4-2a
- removed lcas.db
- updated sources

* Fri Mar 11 2011 Dennis van Dok <dennisvd@nikhef.nl> 0.8.4-1
- new version including lcas/lcmaps db files

* Tue Mar  8 2011 Dennis van Dok <dennisvd@nikhef.nl> 0.8.2-3
- setup config fiiles noreplace

* Fri Mar  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 0.8.2-2
- fixed configuration files and license string

* Fri Feb 25 2011 Dennis van Dok <dennisvd@nikhef.nl> 
- Initial build.
