# $Id: mdvvhdprov.spec 273059 2011-07-05 08:13:27Z alissy $

%define name	mdvvhdprov
%define guiname mdvvhdprovgui
%define version	2.0
%define subrel	0
%define release  3
%define mdvvhddir %{_prefix}/lib/%{name}

Summary:	MDVVHDProv - A tool for Virtual Hard Drives Provisinning
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		System/Servers
URL:		http://svn.mandriva.com/svn/soft/lab/%{name}/
Source0:	%{name}-%{version}.tar.gz
Requires:	urpmi
Requires:       bash
Requires:       parted
Requires:	aria2
BuildRequires:	bash
BuildRequires:	asciidoc
BuildRequires:  xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:	docbook-dtd45-xml
BuildRequires:  pkgconfig(Qt3Support)
BuildRequires:	python-qt4-devel
BuildArch:      noarch 

%description
MDVVHDProv is a tool intented for provisionning Virtual Hard Drive with
Mandriva. It includes mdvbootstrap.sh, which takes care of installing a minimal
yet running system, in a similar manner as debootstrap.

Currently, Virtual Hard Drive are plain old sparse file, which can be converted
in the format you like (VDI, QCOW, etc.).

%prep
%setup -q -n %{name}-%{version}
%build
# Generate locales
./pymake.sh
#lrelease mdvvhdprovgui_*.ts
#pyuic4 ui_about.ui >ui_about.py
#pyuic4 ui_mdvvhdprovgui.ui >ui_mdvvhdprovgui.py

# Generate manpage
a2x -d manpage -f manpage mdvvhdprov.1.txt

%install
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{mdvvhddir}

ln -s %{mdvvhddir}/create_mdv_rawvhd.sh %{buildroot}%{_bindir}/mdvvhdprov
%{__cp} mdvbootstrap.sh %{buildroot}%{_bindir}

%{__cp} common.sh %{buildroot}%{mdvvhddir}
%{__cp} create_mdv_rawvhd.sh %{buildroot}%{mdvvhddir}
%{__cp} imgcreation.sh %{buildroot}%{mdvvhddir}
%{__cp} partformat.sh %{buildroot}%{mdvvhddir}
%{__cp} partumount.sh %{buildroot}%{mdvvhddir}
%{__cp} create_vm_hdd.sh %{buildroot}%{mdvvhddir}
%{__cp} losetup.sh %{buildroot}%{mdvvhddir}
%{__cp} partcreation.sh %{buildroot}%{mdvvhddir}
%{__cp} partmount.sh %{buildroot}%{mdvvhddir}
%{__cp} unlosetup.sh %{buildroot}%{mdvvhddir}

%{__mkdir_p} %buildroot/usr/share/apps/%{guiname}
%{__mkdir_p} %{buildroot}%{_sbindir}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/security/console.apps
%{__mkdir_p} %{buildroot}%{_sysconfdir}/pam.d
%{__cp} mdvvhdprovgui.py %{buildroot}/usr/share/apps/%{guiname}/
%{__cp} ui_mdvvhdprovgui.py %{buildroot}/usr/share/apps/%{guiname}/
%{__cp} ui_about.py %{buildroot}/usr/share/apps/%{guiname}/
%{__cp} mdvvhdprovgui_*.qm %{buildroot}/usr/share/apps/%{guiname}/
%{__cp} %{guiname} %{buildroot}%{_sysconfdir}/security/console.apps/
ln -s /usr/share/apps/%{guiname}/mdvvhdprovgui.py %{buildroot}%{_sbindir}/%{guiname}
ln -s /usr/bin/consolehelper %{buildroot}%{_bindir}/%{guiname}
ln -s %{_sysconfdir}/pam.d/mandriva-simple-auth %{buildroot}%{_sysconfdir}/pam.d/%{guiname}
%{__install} -Dp -m0644 mdvvhdprov.1 %{buildroot}%{_mandir}/man1/mdvvhdprov.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%{_bindir}/%{name}
%{_bindir}/mdvbootstrap.sh
%{mdvvhddir}/*
%doc %{_mandir}/man1/mdvvhdprov.1*

%package -n %{guiname}
Summary:    GUI for mdvvhdprov
Group:	    System/Servers
Requires:   mdvvhdprov >= %{version}
Requires:   python-qt4 >= 4.6
Requires:   usermode
Requires:   usermode-consoleonly
Requires:   python-sip >= 4.9

%description -n %{guiname}
GUI for mdvvhdprov

%files -n %{guiname}
%defattr(-,root,root)
%dir /usr
%dir /usr/sbin
%dir /usr/share/apps
%dir /usr/share/apps/mdvvhdprovgui
%dir /etc/pam.d
%dir /etc/security
%dir /etc/security/console.apps
/usr/share/apps/%{guiname}/mdvvhdprovgui.py
/usr/share/apps/%{guiname}/ui_mdvvhdprovgui.py
/usr/share/apps/%{guiname}/ui_about.py
/usr/share/apps/%{guiname}/mdvvhdprovgui_*.qm
/usr/sbin/%{guiname}
/usr/bin/%{guiname}
/etc/security/console.apps/%{guiname}
/etc/pam.d/%{guiname}


%changelog
* Tue Jul 05 2011 Alexandre Lissy <alissy@mandriva.com> 2.0-1
+ Revision: 688739
- Adding BuildRequires against docbook-dtd45-xml
- Verbose call to a2x
- Initial import of mdvvhdprov
- Created package structure for mdvvhdprov.

