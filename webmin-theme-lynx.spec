%define webmin_rootdir	%{_datadir}/webmin

Name: webmin-theme-lynx
Version: 0.02
Release: %mkrel 6
Summary: Theme Lynx for Webmin
Summary(pt_BR): Tema Lynx para o Webmin
Group: System/Configuration/Other
License: GPL
URL: http://www.pello.info/?q=node/view/15
Source: http://www.pello.info/filez/lynxth.wbt
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
A very light theme for Webmin, lynx-enabled.

%prep
%setup -q -c
# misincluded file?
rm -f lynxth/tmp

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{webmin_rootdir}
tar -cf - lynxth | tar -C %{buildroot}%{webmin_rootdir} -xf -
chmod 755 %{buildroot}%{webmin_rootdir}/lynxth/{theme.pl,index.cgi}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,755)
%{webmin_rootdir}/lynxth

