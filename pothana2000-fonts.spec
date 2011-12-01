%global fontname pothana2000
%global fontconf 69-%{fontname}.conf

Name: %{fontname}-fonts
Version: 1.3.2
Release: 3%{?dist}
Summary: Unicode compliant OpenType font for Telugu

Group: User Interface/X
License: GPLv2+ with exceptions
URL: http://www.kavya-nandanam.com/dload.htm

Source0: http://www.kavya-nandanam.com/Pothana2k-Li.zip
Source1: %{name}-fontconfig.conf
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch: noarch
BuildRequires: fontpackages-devel
Requires: fontpackages-filesystem

%description
A Free OpenType font for Telugu created by
Dr. Tirumala Krishna Desikacharyulu. 

%prep
%setup -q -c -n %{name}
sed -i 's/\r//' gpl.txt

%build

%install
rm -fr %{buildroot}
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Pothana2000.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
 %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
 %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
 %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%clean
rm -fr %{buildroot}

%_font_pkg -f %{fontconf} Pothana2000.ttf

%doc gpl.txt

%changelog
* Tue Feb 02 2010 Sandeep Shedmake <sshedmak@redhat.com> - 1.3.2-3
- Fixed Source0 url
- Resolves: rhbz#560901

* Tue Feb 02 2010 Sandeep Shedmake <sshedmak@redhat.com> - 1.3.2-2
- Resolves: rhbz#560901

* Tue Dec 15 2009 Sandeep Shedmake <sshedmak@redhat.com> - 1.3.2-1
- Rebase from upstream for RHEL 6
- Resolves: bug 547619

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.3.1-3.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 25 2009 <sshedmak@redhat.com> - 1.3.1-2
- Fixed download URL

* Tue Mar 24 2009 <sshedmak@redhat.com> - 1.3.1-1
- Font Exception text added to font license

* Tue Jan 15 2008 <sshedmak@redhat.com> - 1.3-1
- Initial packaging
