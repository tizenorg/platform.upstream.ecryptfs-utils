%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:    ecryptfs-utils
Summary: eCryptfs user space utilities
Version: 104
Release: 1
Group:   System/Libraries
License: GPL-2.0+
Source:  %{name}_%{version}.orig.tar.gz
URL:     http://ecryptfs.org
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: keyutils
Requires: libecryptfs = %{version}-%{release}
BuildRequires: intltool
BuildRequires: python-devel
BuildRequires: keyutils-devel
BuildRequires: libopenssl-devel
BuildRequires: nss-devel
BuildRequires: pam-devel


%description
%{summary}.


%package -n libecryptfs
Summary:    eCryptfs runtime library
Group:      System/Libraries

%description -n libecryptfs
%{summary}.


%package -n libecryptfs-devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   libecryptfs = %{version}-%{release}
Requires:   keyutils-devel

%description -n libecryptfs-devel
%{summary}.


%package -n libecryptfs-python
Summary:    Python bindings for %{name}
Group:      Development/Libraries
Requires:   libecryptfs = %{version}-%{release}

%description -n libecryptfs-python
%{summary}.


%prep
%setup -q -n %{name}-%{version}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL NEWS README
%{_bindir}/ecryptfs*
/sbin/mount.ecryptfs*
/sbin/umount.ecryptfs*
%ifarch x86_64
/lib64/security/pam_ecryptfs.so
%else
/lib/security/pam_ecryptfs.so
%endif
%{_datadir}/locale/*/LC_MESSAGES/ecryptfs-utils.mo
%{_mandir}/man1/*ecryptfs*
%{_mandir}/man7/*ecryptfs*
%{_mandir}/man8/*ecryptfs*
%{_datadir}/doc/%{name}/*
%{_datadir}/ecryptfs-utils/*


%files -n libecryptfs
%defattr(-,root,root,-)
%{_libdir}/libecryptfs.so.*
%{_libdir}/ecryptfs/*


%files -n libecryptfs-devel
%defattr(-,root,root,-)
%{_includedir}/ecryptfs.h
%{_libdir}/libecryptfs.so
%{_libdir}/pkgconfig/libecryptfs.pc


%files -n libecryptfs-python
%defattr(-,root,root,-)
%{python2_sitelib}/ecryptfs-utils/*
%{python2_sitearch}/ecryptfs-utils/*

