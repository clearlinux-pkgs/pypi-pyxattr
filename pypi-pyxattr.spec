#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF66E3E419F84F4DE (iusty@k1024.org)
#
Name     : pypi-pyxattr
Version  : 0.7.2
Release  : 32
URL      : https://files.pythonhosted.org/packages/31/9a/5211b7345c70b0ae3d164a1d0004b9642baf26c5ddd6cc3af04cf2c45ee4/pyxattr-0.7.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/31/9a/5211b7345c70b0ae3d164a1d0004b9642baf26c5ddd6cc3af04cf2c45ee4/pyxattr-0.7.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/31/9a/5211b7345c70b0ae3d164a1d0004b9642baf26c5ddd6cc3af04cf2c45ee4/pyxattr-0.7.2.tar.gz.asc
Summary  : Filesystem extended attributes for python
Group    : Development/Tools
License  : LGPL-2.1
Requires: pypi-pyxattr-filemap = %{version}-%{release}
Requires: pypi-pyxattr-lib = %{version}-%{release}
Requires: pypi-pyxattr-license = %{version}-%{release}
Requires: pypi-pyxattr-python = %{version}-%{release}
Requires: pypi-pyxattr-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
implements extended attributes manipulation. It is a wrapper on top
        of the attr C library - see attr(5).

%package filemap
Summary: filemap components for the pypi-pyxattr package.
Group: Default

%description filemap
filemap components for the pypi-pyxattr package.


%package lib
Summary: lib components for the pypi-pyxattr package.
Group: Libraries
Requires: pypi-pyxattr-license = %{version}-%{release}
Requires: pypi-pyxattr-filemap = %{version}-%{release}

%description lib
lib components for the pypi-pyxattr package.


%package license
Summary: license components for the pypi-pyxattr package.
Group: Default

%description license
license components for the pypi-pyxattr package.


%package python
Summary: python components for the pypi-pyxattr package.
Group: Default
Requires: pypi-pyxattr-python3 = %{version}-%{release}

%description python
python components for the pypi-pyxattr package.


%package python3
Summary: python3 components for the pypi-pyxattr package.
Group: Default
Requires: pypi-pyxattr-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(pyxattr)

%description python3
python3 components for the pypi-pyxattr package.


%prep
%setup -q -n pyxattr-0.7.2
cd %{_builddir}/pyxattr-0.7.2
pushd ..
cp -a pyxattr-0.7.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656403311
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyxattr
cp %{_builddir}/pyxattr-0.7.2/COPYING %{buildroot}/usr/share/package-licenses/pypi-pyxattr/9a1929f4700d2407c70b507b3b2aaf6226a9543c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-pyxattr

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyxattr/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
