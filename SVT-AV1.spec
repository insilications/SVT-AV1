#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : SVT-AV1
Version  : 0.8.5
Release  : 4
URL      : file:///insilications/build/clearlinux/packages/SVT-AV1/SVT-AV1-v0.8.5.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/SVT-AV1/SVT-AV1-v0.8.5.tar.gz
Summary  : AV1-compliant encoder library core.
Group    : Development/Tools
License  : GPL-2.0
Requires: SVT-AV1-bin = %{version}-%{release}
Requires: SVT-AV1-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : nasm-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-base-1.0)
BuildRequires : pkgconfig(gstreamer-video-1.0)
BuildRequires : python3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Scalable Video Technology for AV1 (SVT-AV1 Encoder and Decoder)
[![CI](https://github.com/OpenVisualCloud/SVT-AV1/workflows/CI/badge.svg)](https://github.com/OpenVisualCloud/SVT-AV1/actions?query=workflow%3ACI+branch%3Amaster)
[![MSVC builds](https://github.com/OpenVisualCloud/SVT-AV1/workflows/MSVC%20builds/badge.svg)](https://github.com/OpenVisualCloud/SVT-AV1/actions?query=workflow%3A%22MSVC+builds%22+branch%3Amaster)
[![macOS](https://github.com/OpenVisualCloud/SVT-AV1/workflows/macOS/badge.svg)](https://github.com/OpenVisualCloud/SVT-AV1/actions?query=workflow%3AmacOS+branch%3Amaster)
[![Travis Build Status](https://travis-ci.com/OpenVisualCloud/SVT-AV1.svg?branch=master)](https://travis-ci.com/OpenVisualCloud/SVT-AV1)

%package bin
Summary: bin components for the SVT-AV1 package.
Group: Binaries

%description bin
bin components for the SVT-AV1 package.


%package dev
Summary: dev components for the SVT-AV1 package.
Group: Development
Requires: SVT-AV1-lib = %{version}-%{release}
Requires: SVT-AV1-bin = %{version}-%{release}
Provides: SVT-AV1-devel = %{version}-%{release}
Requires: SVT-AV1 = %{version}-%{release}

%description dev
dev components for the SVT-AV1 package.


%package lib
Summary: lib components for the SVT-AV1 package.
Group: Libraries

%description lib
lib components for the SVT-AV1 package.


%package staticdev
Summary: staticdev components for the SVT-AV1 package.
Group: Default
Requires: SVT-AV1-dev = %{version}-%{release}

%description staticdev
staticdev components for the SVT-AV1 package.


%prep
%setup -q -n SVT-AV1
cd %{_builddir}/SVT-AV1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600056099
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%define _lto_cflags 1
#%define _lto_cflags %{nil}
#
# export PATH="/usr/lib64/ccache/bin:$PATH"
# export CCACHE_NOHASHDIR=1
# export CCACHE_DIRECT=1
# export CCACHE_SLOPPINESS=pch_defines,locale,time_macros
# export CCACHE_DISABLE=1
## altflags1 end
##
%define _lto_cflags 1
##
%cmake .. -DNATIVE=ON -DBUILD_APPS=ON -DBUILD_DEC=ON -DBUILD_ENC=ON -DBUILD_SHARED_LIBS=ON -DCMAKE_POSITION_INDEPENDENT_CODE=OFF -DSTATIC_LINK_CRT=ON -DCMAKE_BUILD_TYPE=Release
make  %{?_smp_mflags}  V=1 VERBOSE=1
popd
mkdir -p clr-build-special
pushd clr-build-special
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%define _lto_cflags 1
#%define _lto_cflags %{nil}
#
# export PATH="/usr/lib64/ccache/bin:$PATH"
# export CCACHE_NOHASHDIR=1
# export CCACHE_DIRECT=1
# export CCACHE_SLOPPINESS=pch_defines,locale,time_macros
# export CCACHE_DISABLE=1
## altflags1 end
##
%define _lto_cflags 1
##
%cmake .. -DNATIVE=ON -DBUILD_APPS=ON -DBUILD_DEC=ON -DBUILD_ENC=ON -DBUILD_SHARED_LIBS=OFF -DCMAKE_POSITION_INDEPENDENT_CODE=OFF -DSTATIC_LINK_CRT=ON -DCMAKE_BUILD_TYPE=Release
make  %{?_smp_mflags}  V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1600056099
rm -rf %{buildroot}
pushd clr-build-special
%make_install_special  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/SvtAv1DecApp
/usr/bin/SvtAv1EncApp

%files dev
%defattr(-,root,root,-)
/usr/include/svt-av1/EbDebugMacros.h
/usr/include/svt-av1/EbSvtAv1.h
/usr/include/svt-av1/EbSvtAv1Dec.h
/usr/include/svt-av1/EbSvtAv1Enc.h
/usr/include/svt-av1/EbSvtAv1ErrorCodes.h
/usr/include/svt-av1/EbSvtAv1ExtFrameBuf.h
/usr/include/svt-av1/EbSvtAv1Formats.h
/usr/lib64/libSvtAv1Dec.so
/usr/lib64/libSvtAv1Enc.so
/usr/lib64/pkgconfig/SvtAv1Dec.pc
/usr/lib64/pkgconfig/SvtAv1Enc.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSvtAv1Dec.so.0
/usr/lib64/libSvtAv1Dec.so.0.8.5
/usr/lib64/libSvtAv1Enc.so.0
/usr/lib64/libSvtAv1Enc.so.0.8.5

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libSvtAv1Dec.a
/usr/lib64/libSvtAv1Enc.a
