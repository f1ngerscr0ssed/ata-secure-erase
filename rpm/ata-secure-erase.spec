Name:           ata-secure-erase
Version:        0.1
Release:        1%{?dist}
Summary:        A bash script to securely erase ATA disk

Group:          System Environment/Shells
License:        MIT
URL:            https://github.com/f1ngerscr0ssed/ata-secure-erase
Source0:        ata-secure-erase-%{version}.tar.gz
Requires:       bash

%description
A bash script to securely erase ATA disks, runs the SECURITY ERASE UNIT command using hdparm. Clears all SSD memory cells to reset drives to factory write performance state.

# EPEL compatibility
%if 0%{?rhel}
%global _pkgdocdir %{_docdir}/%{name}
%endif

%prep
%setup -q -n %{name}-%{version}

%install
install -Dm 0755 ata-secure-erase.sh %{buildroot}%{_bindir}/ata-secure-erase

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/ata-secure-erase

%changelog
* Wed Aug 16 2017 Thomas Oulevey <thomas.oulevey@cern.ch> - 0.1-1
- initial RPM release

