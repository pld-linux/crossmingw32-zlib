#
# Conditional build:
%bcond_without	asmopt	# without assembler optimization for i686+
#
# disable asmopt where not applicable
%ifarch i386 i486 i586
%undefine	with_asmopt
%endif
%ifnarch %{ix86}
%undefine	with_asmopt
%endif
%define		realname		zlib
Summary:	Library for compression and decompression - MinGW32 cross version
Summary(pl.UTF-8):	Biblioteka z podprogramami do kompresji i dekompresji - wersja skrośna dla MinGW32
Name:		crossmingw32-%{realname}
Version:	1.2.7
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://www.zlib.net/current/%{realname}-%{version}.tar.gz
# Source0-md5:	60df6a37c56e7c1366cca812414f7b85
URL:		http://www.zlib.net/
BuildRequires:	crossmingw32-gcc
BuildRequires:	sed >= 4.0
Requires:	crossmingw32-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_libdir			%{_prefix}/lib
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
%define		_dlldir			/usr/share/wine/windows/system
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%ifarch alpha sparc sparc64 sparcv9
%define		optflags	-O2
%endif

%description
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the
uncompressed data. This version of the library supports only one
compression method (deflation) but other algorithms may be added later
and will have the same stream interface.

This package contains the cross version for Win32.

%description -l pl.UTF-8
Biblioteka zlib udostępnia podprogramy do kompresji i dekompresji w
pamięci operacyjnej włącznie ze sprawdzaniem integralności w trakcie
dekompresji. Ta wersja biblioteki udostępnia tylko jedną metodę
kompresji o nazwie deflation niemniej inne algorytmy mogą być
dodawane udostępniając taki sam interfejs funkcji operujących na
strumieniu danych.

Ten pakiet zawiera wersję skrośną dla Win32.

%package static
Summary:	Static zlib library (cross MinGW32 version)
Summary(pl.UTF-8):	Statyczna biblioteka zlib (wersja skrośna MinGW32)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static zlib library (cross MinGW32 version).

%description static -l pl.UTF-8
Statyczna biblioteka zlib (wersja skrośna MinGW32).

%package dll
Summary:	zlib - DLL library for Windows
Summary(pl.UTF-8):	zlib - biblioteka DLL dla Windows
Group:		Applications/Emulators
Requires:	wine

%description dll
zlib - DLL library for Windows.

%description dll -l pl.UTF-8
zlib - biblioteka DLL dla Windows.

%prep
%setup -q -n %{realname}-%{version}

%if %{with asmopt}
%ifarch i686 athlon
cp contrib/asm686/match.S .
%endif
%endif

%build
%{__make} -fwin32/Makefile.gcc all \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	AR="%{target}-ar" \
	RANLIB="%{target}-ranlib" \
	CFLAGS="-D_REENTRANT -D_LARGEFILE64_SOURCE=1 %{rpmcflags}%{?with_asmopt: -DASMV}" \
	DLLWRAP="%{target}-dllwrap" \
	RC="%{target}-windres" \
	CP="install" \
	IMPLIB="libz.dll.a" \
	prefix="%{_prefix}" \
	%{?with_asmopt:OBJA=match.o}

# used by libtool to detect dependencies
cat << "EOF" >> libz.la
# libz.la - a libtool library file
# Generated by ltmain.sh - GNU libtool 1.5.22 (1.1220.2.365 2005/12/18 22:14:06)
# ^^^^ This line needs to stay
# Made by czarny czarny at pld-linux.org

# The name that we can dlopen(3).
dlname='%{_dlldir}/zlib1.dll'

# Names of this library.
library_names='libz.dll.a'

# The name of the static archive.
old_library='libz.a'

# Libraries that this one depends upon.
dependency_libs=''

# Version information for libz.
current=0
age=0
revision=0

# Is this an already installed library?
installed=yes

# Should we warn about portability when linking against -modules?
shouldnotlink=no

# Files to dlopen/dlpreopen
dlopen=''
dlpreopen=''

# Directory that this library needs to be installed in:
libdir='%{_libdir}'
EOF

sed -e 's=@prefix@=%{_prefix}=;s=@exec_prefix@=%{_prefix}=;s=@\(shared\)\?libdir@=%{_libdir}=;s=@includedir@=%{_includedir}=;s=@VERSION@=%{version}=' \
	< zlib.pc.in > zlib.pc

%if 0%{!?debug:1}
%{target}-strip -R.comment -R.note zlib1.dll
%{target}-strip -g -R.comment -R.note *.a
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_dlldir},%{_pkgconfigdir}}

install zlib.h $RPM_BUILD_ROOT%{_includedir}
install zconf.h $RPM_BUILD_ROOT%{_includedir}
install libz.dll.a $RPM_BUILD_ROOT%{_libdir}
install libz.a $RPM_BUILD_ROOT%{_libdir}
install libz.la $RPM_BUILD_ROOT%{_libdir}
install zlib1.dll $RPM_BUILD_ROOT%{_dlldir}
install zlib.pc $RPM_BUILD_ROOT%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/libz.dll.a
%{_libdir}/libz.la
%{_includedir}/zconf.h
%{_includedir}/zlib.h
%{_pkgconfigdir}/zlib.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libz.a

%files dll
%defattr(644,root,root,755)
%{_dlldir}/zlib1.dll
