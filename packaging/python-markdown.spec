%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define srcname Markdown

Name:           python-markdown
Version:        2.0.3
Release:        1
Summary:        Markdown implementation in Python
Group:          Development/Languages
License:        BSD
URL:            http://www.freewisdom.org/projects/python-markdown/
Source0:        http://pypi.python.org/packages/source/M/%{srcname}/%{srcname}-%{version}.tar.gz
Source1001: packaging/python-markdown.manifest 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-devel
%if 0%{?rhel}
BuildRequires:  python-elementtree
Requires:       python-elementtree
%endif


%description
This is a Python implementation of John Gruber's Markdown. It is
almost completely compliant with the reference implementation, though
there are a few known issues.


%prep
%setup -q -n %{srcname}-%{version}

# remove shebangs
find markdown -type f -name '*.py' \
  -exec sed -i -e '/^#!/{1D}' {} \;


%build
cp %{SOURCE1001} .
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --prefix %{_prefix}


%files
%manifest python-markdown.manifest
%{python_sitelib}/*
%{_bindir}/markdown


