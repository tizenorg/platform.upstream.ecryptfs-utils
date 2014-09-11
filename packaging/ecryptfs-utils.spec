Name:    ecryptfs-utils
Summary: Userspace Utilities for ecryptfs
Version: 104
Release: 0
Group:   System/Libraries
License: GPL-2.0+
Source:  %{name}_%{version}.orig.tar.gz
Source1: %{name}.manifest
URL:     http://ecryptfs.org
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: keyutils
Requires: libecryptfs = %{version}-%{release}
BuildRequires: intltool
BuildRequires: python-devel
BuildRequires: keyutils-devel
BuildRequires: nss-devel
BuildRequires: pam-devel
BuildRequires:  fdupes

%description
A stacked cryptographic filesystem for Linux.
eCryptfs user space utilities

%package -n libecryptfs
Summary:    Library for eCryptfs 
Group:      System/Libraries

%description -n libecryptfs
%{summary} files.

%package -n libecryptfs-devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   libecryptfs = %{version}-%{release}
Requires:   keyutils-devel

%description -n libecryptfs-devel
A stacked cryptographic filesystem for Linux.

%package -n libecryptfs-python
Summary:    Python bindings for %{name}
Group:      Development/Libraries
Requires:   libecryptfs = %{version}-%{release}

%description -n libecryptfs-python
A stacked cryptographic filesystem for Linux.

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1} .

%build
%configure --disable-openssl
%__make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

chmod a-x %{buildroot}%{_datadir}/ecryptfs-utils/ecryptfs-record-passphrase

%fdupes %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n libecryptfs -p /sbin/ldconfig

%postun -n libecryptfs -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%license COPYING
%doc AUTHORS NEWS 
%{_bindir}/ecryptfs*
/sbin/mount.ecryptfs*
/sbin/umount.ecryptfs*
/%{_lib}/security/pam_ecryptfs.so
%{_datadir}/locale/*/LC_MESSAGES/ecryptfs-utils.mo
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
%manifest %{name}.manifest
%{_includedir}/ecryptfs.h
%{_libdir}/libecryptfs.so
%{_libdir}/pkgconfig/libecryptfs.pc

%files -n libecryptfs-python
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{py_sitedir}/ecryptfs-utils/*
