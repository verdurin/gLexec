Summary: Development files for Argus PEP client library (thread-safe)
Name: argus-pep-api-c-devel
Version: 2.1.0
Release: 4.sl5
License: ASL 2.0
Vendor: EMI
Group: System Environment/Libraries
Packager: ETICS
BuildRequires: doxygen
BuildRequires: pkgconfig
BuildRequires: automake
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: curl-devel
BuildRequires: argus-pep-api-c
Requires: curl-devel
Requires: argus-pep-api-c
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
AutoReqProv: yes
Source: argus-pep-api-c-devel-2.1.0.tar.gz

%description
Development files for Argus PEP client library for C (EMI)

%prep
 

%setup  

%build
./configure --prefix=$RPM_BUILD_ROOT/usr --libdir=$RPM_BUILD_ROOT/usr/lib64 --disable-library
 make
  
 make html

%install
rm -rf $RPM_BUILD_ROOT
 mkdir -p $RPM_BUILD_ROOT
 mkdir -p $RPM_BUILD_ROOT/usr && make install
 find $RPM_BUILD_ROOT -name '*.la' -exec rm -rf {} \;
 find $RPM_BUILD_ROOT -name '*.pc' -exec sed -i -e "s|$RPM_BUILD_ROOT||g" {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /usr/include/argus/
/usr/include/argus/xacml.h
/usr/include/argus/profiles.h
/usr/include/argus/pip.h
/usr/include/argus/pep.h
/usr/include/argus/error.h
/usr/include/argus/oh.h
/usr/lib64/pkgconfig/libargus-pep.pc
%dir /usr/share/doc/argus-pep-api-c-2.1.0/
%dir /usr/share/doc/argus-pep-api-c-2.1.0/example/
/usr/share/doc/argus-pep-api-c-2.1.0/example/pep_client_example.c
/usr/share/doc/argus-pep-api-c-2.1.0/example/README
%dir /usr/share/doc/argus-pep-api-c-2.1.0/api/
/usr/share/doc/argus-pep-api-c-2.1.0/api/tabs.css
/usr/share/doc/argus-pep-api-c-2.1.0/api/group___logging.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/oh_8h.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/group___error.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/group___profiles.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/globals_vars.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/group___profiles_adapters.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/doxygen.png
/usr/share/doc/argus-pep-api-c-2.1.0/api/examples.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/profiles_8h-source.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/xacml_8h.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/pep__client__example_8c-example.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/pages.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/group___p_e_p_client.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/structpep__pip.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/group___obligation_handler.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/doxygen.css
/usr/share/doc/argus-pep-api-c-2.1.0/api/error_8h.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/files.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/globals_0x67.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/group___x_a_c_m_l.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/structpep__obligationhandler.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/globals_func.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/modules.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/deprecated.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/xacml_8h-source.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/group___grid_w_n_auth_z.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/oh_8h-source.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/group___p_i_p.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/globals_0x70.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/globals_defs.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/pip_8h-source.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/pep_8h-source.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/globals_type.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/tab_r.gif
/usr/share/doc/argus-pep-api-c-2.1.0/api/functions.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/globals_eval.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/annotated.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/pep_8h.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/globals_0x6f.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/tab_l.gif
/usr/share/doc/argus-pep-api-c-2.1.0/api/globals.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/globals_0x78.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/error_8h-source.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/tab_b.gif
/usr/share/doc/argus-pep-api-c-2.1.0/api/functions_vars.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/pip_8h.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/group___common_auth_z.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/index.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/group___authz_interop.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/globals_enum.html
/usr/share/doc/argus-pep-api-c-2.1.0/api/profiles_8h.html

%changelog
* Tue Mar  5 2013 Adam Huffman <a,huffman@imperial.ac.uk> - 2.1.0-4.sl5
- use local prefix

* Tue Apr 3 2012 Valery Tschopp <valery.tschopp@switch.ch> 2.1.0-3

- Initial PEP client C API for EMI 2.



