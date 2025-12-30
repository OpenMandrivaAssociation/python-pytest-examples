%define module pytest-examples
%define oname pytest_examples
# disable tests on abf
%bcond_with test

Name:		python-pytest-examples
Version:	0.0.17
Release:	3
Summary:	Pytest plugin for testing examples in docstrings and markdown files.
URL:		https://pypi.org/project/pytest-examples/
License:	None
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-examples/%{oname}-%{version}.tar.gz
# patch for pytest > 8.3.4 compatibility - https://github.com/pydantic/pytest-examples/pull/54
Patch0:		https://github.com/pydantic/pytest-examples/pull/54/commits/733170e37f31ec9cb70bd8d6eb282a36564406a3.patch
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(black)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
%if %{with test}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(ruff)
BuildRequires:	python%{pyver}dist(pre-commit)
BuildRequires:	python%{pyver}dist(pathlib2)
%endif

%description
Pytest plugin for testing examples in docstrings and markdown files.

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%py_build

%install
%py3_install

%if %{with test}
%check
export PIP_INDEX_URL=http://host.invalid./
export PIP_NO_DEPS=yes
pytest -vv -Wdefault -rs
%endif

%files
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.dist-info
%license LICENSE