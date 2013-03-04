Summary: Nagios plugin for gLExec-wn
Name: nagios-plugins-emi.glexec
Version: 0.3.0
Release: 1.sl5
License: Apache Software License
Vendor: EMI
Group: System Environment/Libraries
Packager: ETICS
BuildArch: noarch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
AutoReqProv: yes
Source: nagios-plugins-emi.glexec-0.3.0.tar.gz

%description
emi.sac.nagios-plugins-glexec

%prep
 

%setup  

%build
./configure --libexecdir=/usr/libexec/grid-monitoring/probes/nagios-plugins-emi.glexec
 make
  
  

%install
rm -rf $RPM_BUILD_ROOT
 mkdir -p $RPM_BUILD_ROOT
 make DESTDIR=$RPM_BUILD_ROOT install
 find $RPM_BUILD_ROOT -name '*.la' -exec rm -rf {} \;
 find $RPM_BUILD_ROOT -name '*.pc' -exec sed -i -e "s|$RPM_BUILD_ROOT||g" {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /usr/libexec/
%dir /usr/libexec/grid-monitoring/
%dir /usr/libexec/grid-monitoring/probes/
%dir /usr/libexec/grid-monitoring/probes/nagios-plugins-emi.glexec/
/usr/libexec/grid-monitoring/probes/nagios-plugins-emi.glexec/check_glexec

%changelog
 
