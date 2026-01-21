%define module pytest-examples
%define oname pytest_examples
# disable tests on ABF
%bcond tests 0

Name:		python-pytest-examples
Version:	0.0.18
Release:	1
Summary:	Pytest plugin for testing examples in docstrings and markdown files.
URL:		https://pypi.org/project/pytest-examples/
License:	None
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-examples/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# patch Bump Ruff to 0.12.9, update regexes for new output rendering - https://github.com/pydantic/pytest-examples/pull/65
Patch0:	pytest_examples-0.0.18-ruff-fixes.patch
Patch1:	pytest_examples-0.0.18-fix-tests.patch

BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(black)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(installer)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(ruff)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pre-commit)
BuildRequires:	python%{pyver}dist(pathlib2)
%endif

%description
Pytest plugin for testing examples in docstrings and markdown files.

%if %{with tests}
%check
export PIP_INDEX_URL=http://host.invalid./
export PIP_NO_DEPS=yes
export CI=true
export PYTHONPATH="%{buildroot}%{py_sitedir}:${PWD}"
pytest -vv -Wdefault -rs
%endif

%files
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.dist-info
%license LICENSE
