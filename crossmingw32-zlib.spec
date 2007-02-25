#
# Conditional build:
%bcond_without	asmopt	# without assmbler optimization for i586+
#
# disable asmopt where not applicable
%ifarch i386 i486
%undefine	with_asmopt
%endif
%ifnarch %{ix86}
%undefine	with_asmopt
%endif
%define		realname		zlib
Summary:	Library for compression and decompression - Ming32 cross version
Summary(de.UTF-8):	Library für die Komprimierung und Dekomprimierung
Summary(es.UTF-8):	Biblioteca para compresión y descompresión
Summary(fr.UTF-8):	bibliothèque de compression et décompression
Summary(pl.UTF-8):	Biblioteka z podprogramami do kompresji i dekompresji - wersja skrośna dla Ming32
Summary(pt_BR.UTF-8):	Biblioteca para compressão e descompressão
Summary(ru.UTF-8):	Библиотека для компрессии и декомпрессии
Summary(tr.UTF-8):	Sıkıştırma işlemleri için kitaplık
Summary(uk.UTF-8):	Бібліотека для компресії та декомпресії
Name:		crossmingw32-%{realname}
Version:	1.2.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.zlib.net/%{realname}-%{version}.tar.gz
# Source0-md5:	debc62758716a169df9f62e6ab2bc634
Patch0:		%{realname}-asmopt.patch
Patch1:		%{name}-shared.patch
URL:		http://www.zlib.org/
BuildRequires:	crossmingw32-gcc
Requires:	crossmingw32-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}
%define		gccarch			%{_prefix}/lib/gcc-lib/%{target}
%define		gcclib			%{_prefix}/lib/gcc-lib/%{target}/%{version}

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_aclocaldir		%{_datadir}/aclocal
%define		_pkgconfigdir		%{_libdir}/pkgconfig
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

%description -l de.UTF-8
Die zlib-Komprimierungs-Library bietet speicherinterne Komprimierungs-
und Dekomprimierungsfunktionen, einschließlich Integritätsprüfungen
der unkomprimierten Daten. Diese Version der Library unterstützt nur
eine Komprimierungsmethode (Deflation), doch können weitere
Algorithmen nachträglich eingefügt werden und haben dann dieselbe
Oberfläche.

%description -l es.UTF-8
La biblioteca de compresión 'zlib' nos ofrece funciones de compresión
y descompresión en memoria, incluyendo chequeo de la integridad de
datos no comprimidos. Esta versión de la biblioteca soporta solamente
un método de compresión (deflación) pero otros algoritmos pueden ser
añadidos más tarde y tendrán la misma interface. Esta biblioteca se
usa por varios programas de sistema.

%description -l fr.UTF-8
La bibliothèque de compression « zlib » offre des fonctions de
compression et de décompression en mémoire, ainsi qu'une vérification
de l'intégrité des données décompressées. La version de cette
bibliothèque ne gère qu'une méthode de compression (deflation), mais
d'autres algorithmes peuvent être ajoutés plus tard et auront la même
interface.

%description -l pl.UTF-8
Biblioteka zlib udostępnia podprogramy do kompresji i dekompresji w
pamięci operacyjnej włącznie ze sprawdzaniem integralności w trakcie
dekompresji. Ta wersja biblioteki udostępnia tylko jedną metodę
kompresji o nazwie deflation niemniej inne algorytmy mogą być
dodawane udostępniając taki sam interfejs funkcji operujących na
strumieniu danych.

%description -l pt_BR.UTF-8
A biblioteca de compressão 'zlib' oferece funções de compressão e
descompressão em memória, incluindo checagem da integridade de dados
não comprimidos. Essa versão da biblioteca suporta somente um método
de compressão (deflação) mas outros algoritmos podem ser adicionados
mais tarde e terão a mesma interface. Essa biblioteca é usada por
vários programas de sistema.

%description -l ru.UTF-8
Библиотека компрессии zlib содержит функции компрессии и декомпрессии
в памяти, включаю проверку целостности декомпрессированных данных. Эта
версия поддерживает только один метод компрессии (deflation), но
впоследствии в нее могут быть добавлены и другие методы, и все они
будут использовать тот же потоковый интерфейс.

%description -l tr.UTF-8
zlib sıkıştırma kitaplığı bellekte sıkıştırma ve açma fonksiyonları
içermektedir. Bu sürüm yalnızca 'deflation' yöntemini
desteklemektedir. Ancak başka algoritmaların aynı arabirimle
erişilebilecek şekilde eklenme olasılığı vardır. Bu kitaplık bir dizi
sistem yazılımı tarafından kullanılmaktadır.

%description -l uk.UTF-8
Бібліотека компресії zlib містить функції компресії та декомпресії в
пам'яті з перевіркою цілості декомпресованих даних. Ця версія
підтримує тільки один метод компресії (deflation), але в майбутньому в
неї можуть бути додані і інші методи і всі вони будуть використовувати
той же самий потоковий інтерфейс.

%package dll
Summary:	zlib - DLL library for Windows
Summary(pl.UTF-8):	zlib - biblioteka DLL dla Windows
Group:		Applications/Emulators

%description dll
zlib - DLL library for Windows.

%description dll -l pl.UTF-8
zlib - biblioteka DLL dla Windows.

%prep
%setup -q -n %{realname}-%{version}
%patch1 -p1

%if %{with asmopt}
%patch0 -p1
%ifarch i686 athlon
cp contrib/asm686/match.S .
%endif
%ifarch i586
cp contrib/asm586/match.S .
%endif
%endif

# fix for underline test
#sed -e 's/nm/%{target}-nm/' configure > configure.tmp
# but it's broken anyway (tries to use mmap test remains, but there is no mmap
# in mingw32) - so hardcode that underline is needed
sed -e 's/.*grep _hello.*/if false; then/' configure > configure.tmp
mv -f configure.tmp configure
chmod +x configure

%build
CC="%{__cc}" \
CXX="%{__cxx}" \
AR="%{target}-ar rc" \
RANLIB="%{target}-ranlib" \
CFLAGS="-D_REENTRANT %{rpmcflags}%{?with_asmopt: -DASMV}" \
./configure \
	--prefix=%{_prefix}

%{__make}
%{__make} z.dll

cat << "EOF" >> libz.la
# libz.la - a libtool library file
# Generated by ltmain.sh - GNU libtool 1.5.22 (1.1220.2.365 2005/12/18 22:14:06)
# ^^^^ This line needs to stay
# Made by czarny czarny at pld-linux.org

# The name that we can dlopen(3).
dlname='../bin/libz.dll'

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

%if 0%{!?debug:1}
%{target}-strip -R.comment -R.note z.dll
%{target}-strip -g -R.comment -R.note *.a
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{/lib,/include,/bin}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}
    

install zutil.h $RPM_BUILD_ROOT%{_includedir}
install libz.dll.a $RPM_BUILD_ROOT%{_libdir}
install z.dll $RPM_BUILD_ROOT%{_bindir}/libz.dll
install libz.la $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%{arch}/include/*.h
%{_includedir}/*.h
%{_libdir}/*

%files dll
%defattr(644,root,root,755)
%{_bindir}/*.dll
