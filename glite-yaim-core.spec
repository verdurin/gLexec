Summary: YAIM core package
Name: glite-yaim-core
Version: 5.1.0
Release: 2.sl5
License: Apache Software License
Vendor: EMI
Group: System Environment/Admin Tools
Prefix: /opt/ichep/emi2/glexec/0.9.6
Packager: ETICS
BuildArch: noarch
Requires: redhat-lsb
Requires: perl
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
AutoReqProv: yes
Source: glite-yaim-core-5.1.0.tar.gz

%description
YAIM core package

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
%dir /opt/glite/bin/
%dir /opt/glite/yaim/
%dir /opt/glite/yaim/etc/
/opt/glite/yaim/etc/clean-grid-env-funcs.sh
/opt/glite/yaim/etc/grid-env.csh
%dir /opt/glite/yaim/etc/versions/
/opt/glite/yaim/etc/versions/glite-yaim-core
/opt/glite/yaim/etc/grid-clean-env.csh
/opt/glite/yaim/etc/grid-env-funcs.sh
%dir /opt/glite/yaim/examples/
/opt/glite/yaim/examples/wn-list.conf
/opt/glite/yaim/examples/users.conf
/opt/glite/yaim/examples/edgusers.conf
%dir /opt/glite/yaim/examples/siteinfo/
/opt/glite/yaim/examples/siteinfo/site-info.def
/opt/glite/yaim/examples/users.conf.README
/opt/glite/yaim/examples/groups.conf
/opt/glite/yaim/examples/wn-list.conf.README
/opt/glite/yaim/examples/groups.conf.README
%dir /opt/glite/yaim/node-info.d/
%dir /opt/glite/yaim/functions/
/opt/glite/yaim/functions/config_glite_initd
/opt/glite/yaim/functions/config_vomsdir
/opt/glite/yaim/functions/config_root_email
/opt/glite/yaim/functions/config_globus_clients
/opt/glite/yaim/functions/config_mkgridmap
%dir /opt/glite/yaim/functions/utils/
/opt/glite/yaim/functions/utils/run
/opt/glite/yaim/functions/utils/cron_job
/opt/glite/yaim/functions/utils/users_getprduser
/opt/glite/yaim/functions/utils/set_mysql_passwd
/opt/glite/yaim/functions/utils/users_getfirstpoolaccount
/opt/glite/yaim/functions/utils/vo_param
/opt/glite/yaim/functions/utils/central_certs
/opt/glite/yaim/functions/utils/gridenv
/opt/glite/yaim/functions/utils/detect_platform
/opt/glite/yaim/functions/utils/requires
/opt/glite/yaim/functions/utils/users_getsgmuser
/opt/glite/yaim/functions/utils/users_getspecialprefix
/opt/glite/yaim/functions/utils/yaimlog
/opt/glite/yaim/functions/utils/users_getvogroup
/opt/glite/yaim/functions/utils/check_users_conf_format
/opt/glite/yaim/functions/utils/users_getspecialusers
/opt/glite/yaim/functions/utils/users_getspecialgroup
/opt/glite/yaim/functions/utils/config_file
/opt/glite/yaim/functions/utils/start_mysql
/opt/glite/yaim/functions/utils/split_quoted_variable
/opt/glite/yaim/functions/utils/detect_tomcat
/opt/glite/yaim/functions/utils/convert_fqan
/opt/glite/yaim/functions/utils/users_getvoprefix
/opt/glite/yaim/functions/create_siteinforpm
/opt/glite/yaim/functions/config_gip_vo_tag
/opt/glite/yaim/functions/config_lcgenv
/opt/glite/yaim/functions/config_lcas_lcmaps_gt4
%dir /opt/glite/yaim/functions/extensions/
/opt/glite/yaim/functions/config_apt_prefs
/opt/glite/yaim/functions/config_vomses
/opt/glite/yaim/functions/config_globus_gridftp
/opt/glite/yaim/functions/config_vomsmap
/opt/glite/yaim/functions/config_users
/opt/glite/yaim/functions/config_apt
/opt/glite/yaim/functions/config_gip_service_release
/opt/glite/yaim/functions/config_host_certs
/opt/glite/yaim/functions/config_edgusers
/opt/glite/yaim/functions/config_sysconfig_edg
/opt/glite/yaim/functions/config_ldconf
/opt/glite/yaim/functions/config_glite_locallogger
/opt/glite/yaim/functions/config_sysconfig_globus
/opt/glite/yaim/functions/config_crl
/opt/glite/yaim/functions/config_bdii_only
%dir /opt/glite/yaim/functions/local/
/opt/glite/yaim/functions/config_rfio
/opt/glite/yaim/functions/config_sysconfig_lcg
/opt/glite/yaim/functions/config_add_pool_env
/opt/glite/yaim/functions/config_add_glite_env
/opt/glite/yaim/functions/config_secure_tomcat
/opt/glite/yaim/functions/config_check_oraclelibs
%dir /opt/glite/yaim/defaults/
/opt/glite/yaim/defaults/node-info.def
/opt/glite/yaim/defaults/site-info.pre
/opt/glite/yaim/defaults/mapping
/opt/glite/yaim/defaults/site-info.post
%dir /opt/glite/yaim/log/
%dir /opt/glite/yaim/libexec/
/opt/glite/yaim/libexec/YAIM2gLiteConvertor.py
/opt/glite/yaim/libexec/YAIM2gLiteConvertor.pyc
/opt/glite/yaim/libexec/YAIM2gLiteConvertor.pyo
/opt/glite/yaim/libexec/run_function
/opt/glite/yaim/libexec/gLiteContainers.xml
/opt/glite/yaim/libexec/parse_bash_params
/opt/glite/yaim/libexec/XMLHelper.py
/opt/glite/yaim/libexec/XMLHelper.pyc
/opt/glite/yaim/libexec/XMLHelper.pyo
/opt/glite/yaim/libexec/ClassAdsHelper.py
/opt/glite/yaim/libexec/ClassAdsHelper.pyc
/opt/glite/yaim/libexec/ClassAdsHelper.pyo
/opt/glite/yaim/libexec/install_node
/opt/glite/yaim/libexec/xmlUtils.py
/opt/glite/yaim/libexec/xmlUtils.pyc
/opt/glite/yaim/libexec/xmlUtils.pyo
/opt/glite/yaim/libexec/configure_node
/opt/glite/yaim/libexec/gLite.def
/opt/glite/yaim/libexec/ClassAd.py
/opt/glite/yaim/libexec/ClassAd.pyc
/opt/glite/yaim/libexec/ClassAd.pyo
%dir /opt/glite/yaim/bin/
/opt/glite/yaim/bin/yaim
%dir /opt/glite/share/
%dir /opt/glite/share/man/
%dir /opt/glite/share/man/man1/
/opt/glite/share/man/man1/yaim.1

%changelog
* Tue Mar  5 2013 Adam Huffman <a.huffman@imperial.ac.uk> - 5.1.0-2.sl5
- use local prefix

 
