Name:           python-stevedore
Version:        0.8
Release:        3%{?dist}
Summary:        Manage dynamic plugins for Python applications

Group:          Development/Languages
License:        ASL 2.0
URL:            https://github.com/dreamhost/stevedore
Source0:        http://pypi.python.org/packages/source/s/stevedore/stevedore-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
Manage dynamic plugins for Python applications

%prep
%setup -q -n stevedore-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%{python_sitelib}/stevedore
%{python_sitelib}/stevedore-%{version}-py?.?.egg-info

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Pádraig Brady <P@draigBrady.com> - 0.8-1
- Update to version 0.8

* Mon Dec 10 2012 Dan Prince <dprince@redhat.com> - 0.7.2-1
- Initial package.
