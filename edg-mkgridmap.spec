Summary: A tool to build the grid-mapfile
Name: edg-mkgridmap
Version: 4.0.0
Release: 2
Source: %{name}-%{version}.tar.gz
Url: http://jra1mw.cvs.cern.ch:8180/cgi-bin/jra1mw.cgi/Auth/edg-mkgridmap/
License: ASL 2.0
Group: Applications/Internet
Packager: EMI
Vendor: EMI
Prefix: /opt/ichep/emi2/glexec/0.9.6
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
Requires: perl(URI)
Requires: perl(Net::LDAP)
Requires: perl(Net::LDAPS)
Requires: perl(Term::ReadKey)
Requires: perl(IO::Socket::SSL) >= 0.90
Requires: perl(Net::SSLeay) >= 1.16
Requires: perl(Crypt::SSLeay)
Requires: perl(LWP)
Requires: perl(XML::DOM)
Requires: perl(Date::Manip)

%description
edg-mkgridmap is a tool to build the grid-mapfile.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%docdir %{_defaultdocdir}/%{name}
%docdir %{_mandir}/man5
%docdir %{_mandir}/man8
%{_libexecdir}/edg-mkgridmap
%{_libexecdir}/edg-mkgridmap/edg-mkgridmap.pl
%{_sbindir}/edg-mkgridmap
%{_defaultdocdir}/%{name}
%{_defaultdocdir}/%{name}/AUTHORS
%{_defaultdocdir}/%{name}/LICENSE
%{_defaultdocdir}/%{name}/MAINTAINERS
%{_mandir}/man5/edg-mkgridmap.conf.5*
%{_mandir}/man8/edg-mkgridmap.8*

%changelog
* Mon Mar  4 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 4.0.0-2
- use local prefix

* Sun Apr  3 2011 Maarten.Litmaath@cern.ch
- Adaptations for EMI.
- Removed obsolete components.
- Version 4.0.0

* Thu Mar  5 2009 LCG <support-lcg-deployment@cern.ch>
- Replaced obsolete Copyright with License in spec file.
- Version 3.0.1

* Sun Dec  9 2007 LCG <support-lcg-deployment@cern.ch>
- Try ensure compatibility with OpenSSL 0.9.6 as well as >= 0.9.7.
- Version 3.0.0

* Wed Oct  3 2007 LCG <support-lcg-deployment@cern.ch>
- Added explicit dependency on XML::Parser, not always present by default.
- Version 2.9.1

* Sat Mar  3 2007 LCG <support-lcg-deployment@cern.ch>
- Fixed bug #24343: edg-mkgridmap incompatible with axis 1.2.1 and
  voms-admin >1.2.20.  Patch by Andrea.Ceccanti@cnaf.infn.it applied
  (slightly modified).
- Some cosmetic changes.
- Version 2.9.0

* Mon Jan 29 2007 LCG <support-lcg-deployment@cern.ch>
- Also reject trailing backslashes.
- Fixed corresponding error status.
- Updated spec file release, URL, copyright and packager.
- Updated documentation.
- Version 2.8.1

* Sun Jan 28 2007 LCG <support-lcg-deployment@cern.ch>
- Put in work-around for bug #23292: "escaped quotes in grid-mapfile cause
  infinite loop".  We now reject entries with embedded double quotes.
- Added "--usermode" option to facilitate running the script as an ordinary
  user by having the relevant environment variables point to the user's X509
  proxy instead of using the personal certificate and key.
- Made scanning of grid-mapfile-local robust against trailing white space.
  Warn about malformed lines.
- Updated documentation.
- Version 2.8.0

* Tue Nov 28 2006 LCG <support-lcg-deployment@cern.ch>
- Fix for bug #19765: "edg-mkgridmap ignores X509_USER_CERT env veriables
  when run as non-root".
- Fix for bug #21932: "edg-mkgridmap not robust against xml parsing errors".
  We now specify ISO-8859-1 as the character encoding, such that the XML
  parser will not bomb out on finding a character with the high bit set.
- Added "--cache" option for VDT, which causes the grid-mapfile to be
  treated as a cache, i.e. it is only rewritten when the contents change.
- Updated edg-mkgridmap.conf.in: removed references to lcg-voms.cern.ch,
  added new sources for "lhcbsgm" and "lhcbprd", get "atlas" users from
  root group instead of "lcg1" subgroup.
- Version 2.7.0

* Mon Mar 13 2006 LCG <support-lcg-deployment@cern.ch>
- The fix applied in the previous version only avoided pool accounts
  getting wrongly overridden: now we also do the right thing for
  static mappings.
- Updated edg-mkgridmap.conf.in with LCG-2_7_0 defaults.
- Version 2.6.1

* Sun Oct 02 2005 LCG <support-lcg-deployment@cern.ch>
- Alberto Di Meglio found that a multi-VO DN may unintentionally get mapped
  to a secondary VO when the primary VOMS server has a problem: we now keep
  the original mapping unless the new mapping gives more privileges, i.e.
  when the new mapping is to a special (e.g. "sgm") account instead of a
  pool account
- Fixed spelling errors in edg-mkgridmap.conf.in
- Version 2.6.0

* Thu Jul 14 2005 LCG <support-lcg-deployment@cern.ch>
- Decouple groups (VOs), let errors for one group not influence other groups
- Allow for multiple sources per group, any of which is allowed to fail
- Let special accounts always override pool accounts
- Version 2.5.0

* Thu Apr 28 2005 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Adopted a more secure grid-mapfile writing strategy
- Version 2.4.2

* Wed Feb 16 2005 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Added server certificate verification in VOMSS connections
- Version 2.4.1

* Mon Feb 07 2005 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- auth directives in edg-mkgridmap.conf restricted to LDAP/LDAPS connections
- Version 2.4.0

* Mon Oct 11 2004 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- VOMS role support for VOMS/VOMSS connections
- Version 2.3.0

* Mon Mar 22 2004 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Version 2.2.2

* Mon Feb 16 2004 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Version 2.2.1

* Sun Feb 15 2004 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- VOMS support via VOMS/VOMSS connection to edg-voms-admin
- Proxy support for HTTP/HTTPS and VOMS/VOMSS connections
- Added --proxy/--noproxy option
- Added perl(Term::ReadKey) dependence
- Added perl(IO::Socket::SSL) dependence
- Added perl(Net::SSLeay) dependence
- Removed --vo/--novo option
- Updated documentation
- Version 2.2.0

* Thu Dec 18 2003 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Updated documentation
- Version 2.0.7

* Mon Jun 23 2003 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Updated documentation
- Version 2.0.6

* Mon Jun 09 2003 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- New error message in edg-mkgridmap if grid-mapfile writing is skipped
- Updated documentation
- Version 2.0.5

* Tue Jun 03 2003 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Increased verbosity of edg-mkgridmap error messages
- Updated DEPENDENCIES
- Updated README
- Removed edg-mkgridmap.pl
- Removed edg-mkgridpool.pl
- Added edg-mkgridmap.pl.in
- Added edg-mkgridpool.pl.in
- Version 2.0.4

* Thu May 22 2003 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Removed profile.d/edg-mkgridmap.csh from config files
- Removed profile.d/edg-mkgridmap.sh from config files
- Removed alias mkgridmap
- Removed alias mkgridpool
- Version 2.0.3

* Wed May 07 2003 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- The perl(Crypt::SSLeay) is explicitly required by edg-mkgridmap
- Support for machine-dependent configuration file
- Modified user agent for HTTP/HTTPS connections
- Updated documentation
- Added man and html documentation to edg-mkgridmap-conf package
- Added alias mkgridmap
- Added alias mkgridpool
- Version 2.0.2

* Sun Apr 27 2003 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Added 'edg-' prefix
- Added --version option
- Added --quiet option to disable error messages
- Added a common timeout of 30 seconds for network connections
- Added libexec/edg-mkgridmap
- Added DEPENDENCIES to doc files
- Added LICENSE to doc files
- Added MAINTAINERS to doc files
- Added html documentation
- Added grid-mapfile-local.template to config files
- Added edg-mkgridmap.conf to config files
- Added profile.d/edg-mkgridmap.csh to config files
- Added profile.d/edg-mkgridmap.sh to config files
- Added doc files to edg-mkgridmap-conf package
- Removed COPYING from doc files
- Removed grid-mapfile-local from config files
- Removed mkgridmap.conf from config files
- Removed sysconfig/mkgridmap from config files
- Version 2.0.1

* Thu Apr 10 2003 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- VOMS support via HTTP/HTTPS connection to voms-httpd-query
- The perl(LWP), perl(XML::DOM) modules are required by mkgridmap
- Added AUTHORS to doc files
- Version 2.0.0

* Tue Apr 08 2003 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Updated documentation
- Version 1.2.3

* Fri Mar 21 2003 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- New --from and --to options in mkgridpool
- The perl(Date::Manip) module is required by mkgridpool
- Moved all config files to conf package
- Added noreplace attribute for config files
- Added COPYING to doc files
- Version 1.2.2

* Fri Feb 21 2003 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- The perl(URI) module is required by mkgridmap to provide a complete support
  of the LDAP URI format
- Version 1.2.1

* Wed Jan 15 2003 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- The configuration file is distributed in a separate package
- Autotools and syslog support
- Added --safe option
- Added mkgridpool
- Version 1.2.0

* Thu Aug 01 2002 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Added --vo option
- New environment variable EDG_LOCATION
- Binary package is relocateable
- Version 1.0.10

* Mon Jul 15 2002 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Added --output option
- Version 1.0.9

* Wed Jun 26 2002 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Options auth and gmf_local can be repeated more times
- A failure in network connection just produces a warning message
- Improved ldap search algorithm
- General code revision
- Version 1.0.8

* Mon Apr 15 2002 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- New configuration file
- Version 1.0.7

* Mon Jan 21 2002 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Improved building tool
- Version 1.0.6

* Tue Dec 04 2001 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Small changes
- Version 1.0.5

* Wed Nov 28 2001 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Package is not relocateable
- Version 1.0.4

* Tue Nov 27 2001 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- Small changes
- Version 1.0.3

* Mon Nov 26 2001 EU DataGrid Authorization Working Group <sec-grid@infn.it>
- First stable
- Version 1.0.2
