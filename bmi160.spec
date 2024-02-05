%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     bmi160
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  BMI160 IMU Linux driver
License:  GPLv2
URL:      https://github.com/KyleGospo/bmi160

Source:   %{url}/archive/refs/heads/main.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
This is a kernel module driver for the BMI160 IMU with support for AYANEO

%prep
%setup -q -c %{name}-main

%files
%doc %{name}-main/README.md
%license %{name}-main/LICENSE

%changelog
{{{ git_dir_changelog }}}
