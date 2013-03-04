Summary: YAIM package to configure a GLEXEC Worker Node
Name: yaim-glexec-wn
Version: 2.3.2
Release: 1.sl5
License: ASL 2.0
Vendor: EMI
Group: System Environment/Libraries
Packager: ETICS
BuildArch: noarch
Requires: glite-yaim-core
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
AutoReqProv: yes
Source: yaim-glexec-wn-2.3.2.tar.gz

%description
emi.sac.yaim-glexec-wn

%prep
 

%setup  

%build
 
  
  
  

%install
rm -rf $RPM_BUILD_ROOT
 mkdir -p $RPM_BUILD_ROOT
 make install prefix=$RPM_BUILD_ROOT/opt/glite
 find $RPM_BUILD_ROOT -name '*.la' -exec rm -rf {} \;
 find $RPM_BUILD_ROOT -name '*.pc' -exec sed -i -e "s|$RPM_BUILD_ROOT||g" {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /opt/glite/
%dir /opt/glite/yaim/
%dir /opt/glite/yaim/etc/
%dir /opt/glite/yaim/etc/versions/
/opt/glite/yaim/etc/versions/glite-yaim-glexec-wn
%dir /opt/glite/yaim/examples/
%dir /opt/glite/yaim/examples/siteinfo/
%dir /opt/glite/yaim/examples/siteinfo/services/
/opt/glite/yaim/examples/siteinfo/services/glite-glexec_wn
%dir /opt/glite/yaim/node-info.d/
/opt/glite/yaim/node-info.d/glite-glexec_wn
%dir /opt/glite/yaim/functions/
/opt/glite/yaim/functions/config_glexec_wn_log
/opt/glite/yaim/functions/config_glexec_wn
/opt/glite/yaim/functions/config_glexec_wn_users
/opt/glite/yaim/functions/config_glexec_wn_lcaslcmaps
%dir /opt/glite/yaim/defaults/
/opt/glite/yaim/defaults/glite-glexec_wn.pre
/opt/glite/yaim/defaults/glite-glexec_wn.post
%dir /opt/glite/share/
%dir /opt/glite/share/man/
%dir /opt/glite/share/man/man1/
/opt/glite/share/man/man1/yaim-glexec-wn.1

%changelog
 
