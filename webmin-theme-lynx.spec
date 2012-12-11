%define webmin_rootdir	%{_datadir}/webmin

Name: webmin-theme-lynx
Version: 0.02
Release: %mkrel 7
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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.02-7mdv2010.0
+ Revision: 434738
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.02-6mdv2009.0
+ Revision: 261927
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.02-5mdv2009.0
+ Revision: 255889
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.02-3mdv2008.1
+ Revision: 136572
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 21 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.02-3mdv2008.0
+ Revision: 92008
- Fix Group.
- Removed i18n from the .spec.

* Thu Aug 23 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.02-2mdv2008.0
+ Revision: 70136
- use %%mkrel


* Fri Aug 05 2005 Marcelo Ricardo Leitner <mrl@conectiva.com.br> 0.02-1mdk
- Adopted to Mandriva.

