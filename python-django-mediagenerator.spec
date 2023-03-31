%bcond_without python2

Summary:	Media asset manager for Django

Name:		python-django-mediagenerator
Version:	1.12
Release:	8
Source0:	https://pypi.python.org/packages/9c/9c/174dac7b8ea9ee2c9a8629eca9bc165cb7243e69811d23f496bda88da132/django-mediagenerator-%{version}.zip
License:	BSD
Group:		Development/Python
Url:		https://pypi.python.org/pypi/django-mediagenerator
Patch0:		mediagenerator-1.12-python3.patch
Patch1:		mediagenerator-1.12-django-1.9.patch
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3-distribute
Requires:	python-django

%description
Media asset manager for Django

%if %{with python2}
%package -n python2-django-mediagenerator
Summary:	Media asset manager for Django
Group:		Development/Python
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
Requires:	python2-django

%description -n python2-django-mediagenerator
Media asset manager for Django
%endif

%prep
%setup -qc
mv django-mediagenerator-%{version} python3
cd python3
%patch1 -p1 -b .dj19~
cd ..

%if %{with python2}
cp -r python3 python2
%endif

%patch0 -p1 -b .py3~
find python3 -name "*.py" |while read r; do
	2to3 -w $r
done

%build
%if %{with python2}
cd python2
python2 setup.py build
cd ..
%endif

cd python3
python setup.py build
cd ..

%install
%if %{with python2}
cd python2
python2 setup.py install --skip-build --root %{buildroot}
cd ..
%endif

cd python3
python setup.py install --skip-build --root=%{buildroot} 
cd ..

%files
%{py_puresitedir}/*

%if %{with python2}
%files -n python2-django-mediagenerator
%{py2_puresitedir}/*
%endif
