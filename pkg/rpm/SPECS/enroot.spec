%define _prefix %{nil}
%define _exec_prefix /usr
%define _libdir /usr/lib
%define _datarootdir /usr/share

Name: %{PACKAGE}
Version: %{VERSION}
Release: 1%{?dist}
License: ASL 2.0
Vendor: %{USERNAME}
Packager: %{USERNAME} <%{EMAIL}>
URL: https://github.com/NVIDIA/enroot

BuildRequires: make gcc libtool

Summary: Unprivileged container sandboxing utility
%if "%{?getenv:PACKAGE}" != ""
Conflicts: enroot
%endif
Requires: bash >= 4.2, curl, gawk, jq >= 1.5, parallel, shadow-utils, squashfs-tools
Requires: coreutils, grep, findutils, gzip, glibc-common, sed, tar, util-linux
#Recommends: pv, pigz, ncurses
#Suggests: libnvidia-container-tools, squashfuse, fuse-overlayfs
%description
A simple yet powerful tool to turn traditional container/OS images into
unprivileged sandboxes.

This package provides the main utility, its set of helper binaries and
standard configuration files.
%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/*
%{_libdir}/*
%{_bindir}/*
%{_datadir}/*

%package -n %{name}+caps
Summary: Unprivileged container sandboxing utility (extra capabilities)
Requires: %{name}%{?_isa} = %{version}-%{release}, libcap
%description -n %{name}+caps
A simple yet powerful tool to turn traditional container/OS images into
unprivileged sandboxes.

This dependency package grants extra capabilities to unprivileged users which
allows them to import and convert container images directly.
%post -n %{name}+caps
setcap cap_sys_admin+pe "$(command -v enroot-mksquashovlfs)"
setcap cap_sys_admin,cap_mknod+pe "$(command -v enroot-aufs2ovlfs)"
%preun -n %{name}+caps
setcap cap_sys_admin-pe "$(command -v enroot-mksquashovlfs)"
setcap cap_sys_admin,cap_mknod-pe "$(command -v enroot-aufs2ovlfs)"
%files -n %{name}+caps

%build
%make_build prefix=%{_prefix} exec_prefix=%{_exec_prefix} libdir=%{_libdir} datarootdir=%{_datarootdir}

%install
%make_install prefix=%{_prefix} exec_prefix=%{_exec_prefix} libdir=%{_libdir} datarootdir=%{_datarootdir}

%changelog
* Thu Oct 30 2019 %{packager} 2.2.0-1
- Release v2.2.0

* Thu Oct 17 2019 %{packager} 2.1.0-1
- Release v2.1.0

* Thu Sep 05 2019 %{packager} 2.0.1-1
- Release v2.0.1

* Tue Aug 13 2019 %{packager} 2.0.0-1
- Release v2.0.0

* Mon Jun 03 2019 %{packager} 1.1.0-1
- Release v1.1.0

* Sat Apr 20 2019 %{packager} 1.0.0-1
- Initial release
