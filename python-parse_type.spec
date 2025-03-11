#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Simplify building parse types based on the parse module
Summary(pl.UTF-8):	Uproszczenie tworzenia typów do analizy w oparciu o moduł parse
Name:		python-parse_type
Version:	0.6.2
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/parse-type/
Source0:	https://files.pythonhosted.org/packages/source/p/parse-type/parse_type-%{version}.tar.gz
# Source0-md5:	f5c79d0643db5a3936ac22f92d7ee21d
URL:		https://pypi.org/project/parse-type/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-enum34
BuildRequires:	python-parse >= 1.13.1
BuildRequires:	python-pytest >= 3.2
BuildRequires:	python-pytest-html >= 1.19.0
BuildRequires:	python-pytest-metadata
BuildRequires:	python-six >= 1.15
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-parse >= 1.18.0
BuildRequires:	python3-pytest >= 5.0
BuildRequires:	python3-pytest-html >= 1.19.0
BuildRequires:	python3-pytest-metadata
BuildRequires:	python3-six >= 1.15
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
parse_type extends the parse module (opposite of "string.format()").

%description -l pl.UTF-8
parse_type rozszerza moduł parse (odwrotność "string.format()").

%package -n python3-parse_type
Summary:	Simplify building parse types based on the parse module
Summary(pl.UTF-8):	Uproszczenie tworzenia typów do analizy w oparciu o moduł parse
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-parse_type
parse_type rozszerza moduł parse (odwrotność "string.format()").

%description -n python3-parse_type -l pl.UTF-8
parse_type rozszerza moduł parse (odwrotność "string.format()").

%prep
%setup -q -n parse_type-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_html.plugin,pytest_metadata.plugin \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_html.plugin,pytest_metadata.plugin \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE README.rst
%{py_sitescriptdir}/parse_type
%{py_sitescriptdir}/parse_type-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-parse_type
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE README.rst
%{py3_sitescriptdir}/parse_type
%{py3_sitescriptdir}/parse_type-%{version}-py*.egg-info
%endif
