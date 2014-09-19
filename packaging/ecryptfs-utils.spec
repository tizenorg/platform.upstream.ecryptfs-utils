%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:    ecryptfs-utils
Summary: ECryptfs utilities
Version: 104
Release: 0
Group:   System/Libraries
License: GPL-2.0+
Source:  %{name}_%{version}.orig.tar.gz
Source1: %{name}.manifest
URL:     http://ecryptfs.org
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
Requires:           keyutils
Requires:           libecryptfs = %{version}-%{release}
BuildRequires:      intltool
BuildRequires:      python-devel
BuildRequires:      keyutils-devel
BuildRequires:      nss-devel
BuildRequires:      pam-devel
BuildRequires:      pkgconfig(glib-2.0)
BuildRequires:      fdupes

%description
eCryptfs user space utilities.


%package -n libecryptfs
Summary:    ECryptfs library
Group:      System/Libraries

%description -n libecryptfs
eCryptfs runtime library.


%package -n libecryptfs-devel
Summary:    Devel files for libecryptfs
Group:      Development/Libraries
Requires:   libecryptfs = %{version}-%{release}
Requires:   keyutils-devel

%description -n libecryptfs-devel
Development files for eCryptfs library.


%package -n libecryptfs-python
Summary:    Python bindings for libecryptfs
Group:      Development/Libraries
Requires:   libecryptfs = %{version}-%{release}

%description -n libecryptfs-python
Python bindings for eCryptfs library.


%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} .


%build
%reconfigure --disable-openssl
%__make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install

%find_lang %{name}

%fdupes %{buildroot}


%post -n libecryptfs -p /sbin/ldconfig

%postun -n libecryptfs -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root,-)
%manifest %{name}.manifest
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/ecryptfs*
/sbin/mount.ecryptfs*
/sbin/umount.ecryptfs*
/%{_lib}/security/pam_ecryptfs.so
%{_mandir}/man1/*ecryptfs*
%{_mandir}/man7/*ecryptfs*
%{_mandir}/man8/*ecryptfs*
%{_datadir}/doc/%{name}/*
%{_datadir}/ecryptfs-utils/*


%files -n libecryptfs
%defattr(-,root,root,-)
%manifest %{name}.manifest
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
