
%ifnarch i586 i686 athlon
%define				_asmopt		0
%else
%{?_without_asmopt:%define	_asmopt		0}
%{!?_without_asmopt:%define	_asmopt		1}
%endif

%define		realname		zlib
Summary:	Library for compression and decompression
Summary(de):	Library für die Komprimierung und Dekomprimierung
Summary(es):	Biblioteca para compresión y descompresión
Summary(fr):	bibliothèque de compression et décompression
Summary(pl):	Biblioteka z podprogramami do kompresji i dekompresji
Summary(pt_BR):	Biblioteca para compressão e descompressão
Summary(ru):	âÉÂÌÉÏÔÅËÁ ÄÌÑ ËÏÍĞÒÅÓÓÉÉ É ÄÅËÏÍĞÒÅÓÓÉÉ
Summary(tr):	Sıkıştırma işlemleri için kitaplık
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ ÄÌÑ ËÏÍĞÒÅÓ¦§ ÔÁ ÄÅËÏÍĞÒÅÓ¦§
Name:		crossmingw32-%{realname}
Version:	1.1.4
Release:	7
License:	BSD
Group:		Libraries
Source0:	http://www.gzip.org/%{realname}/%{realname}-%{version}.tar.gz
# Source0-md5: abc405d0bdd3ee22782d7aa20e440f08
Patch0:		%{realname}-sharedlib.patch
Patch1:		%{realname}-asmopt.patch
Patch2:		%{realname}-gzprintf_sec.patch
URL:		http://www.zlib.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{realname}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}
%define		gccarch			%{_prefix}/lib/gcc-lib/%{target}
%define		gcclib			%{_prefix}/lib/gcc-lib/%{target}/%{version}

%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%description
The 'zlib' compression library provides in-memory compression and
decompression functions, including integrity checks of the
uncompressed data. This version of the library supports only one
compression method (deflation) but other algorithms may be added later
and will have the same stream interface.

%description -l de
Die zlib-Komprimierungs-Library bietet speicherinterne Komprimierungs-
und Dekomprimierungsfunktionen, einschließlich Integritätsprüfungen
der unkomprimierten Daten. Diese Version der Library unterstützt nur
eine Komprimierungsmethode (Deflation), doch können weitere
Algorithmen nachträglich eingefügt werden und haben dann dieselbe
Oberfläche.

%description -l es
La biblioteca de compresión 'zlib' nos ofrece funciones de compresión
y descompresión en memoria, incluyendo chequeo de la integridad de
datos no comprimidos. Esta versión de la biblioteca soporta solamente
un método de compresión (deflación) pero otros algoritmos pueden ser
añadidos más tarde y tendrán la misma interface. Esta biblioteca se
usa por varios programas de sistema.

%description -l fr
La bibliothèque de compression « zlib » offre des fonctions de
compression et de décompression en mémoire, ainsi qu'une vérification
de l'intégrité des données décompressées. La version de cette
bibliothèque ne gère qu'une méthode de compression (deflation), mais
d'autres algorithmes peuvent être ajoutés plus tard et auront la même
interface.

%description -l pl
Biblioteka zlib udostêpnia podprogramy do kompresji i dekompresji w
pamiêci operacyjnej w³±cznie ze sprawdzaniem integralno¶ci w trakcie
dekompresji. Ta wersja biblioteki udostêpnia tylko jedn± metodê
kompresji o nazwie deflation niemniej inne algorytmy mog± byæ
dodawane udostêpniaj±c taki sam interfejs funkcji operuj±cych na
strumieniu danych.

%description -l pt_BR
A biblioteca de compressão 'zlib' oferece funções de compressão e
descompressão em memória, incluindo checagem da integridade de dados
não comprimidos. Essa versão da biblioteca suporta somente um método
de compressão (deflação) mas outros algoritmos podem ser adicionados
mais tarde e terão a mesma interface. Essa biblioteca é usada por
vários programas de sistema.

%description -l ru
âÉÂÌÉÏÔÅËÁ ËÏÍĞÒÅÓÓÉÉ zlib ÓÏÄÅÒÖÉÔ ÆÕÎËÃÉÉ ËÏÍĞÒÅÓÓÉÉ É ÄÅËÏÍĞÒÅÓÓÉÉ
× ĞÁÍÑÔÉ, ×ËÌÀŞÁÀ ĞÒÏ×ÅÒËÕ ÃÅÌÏÓÔÎÏÓÔÉ ÄÅËÏÍĞÒÅÓÓÉÒÏ×ÁÎÎÙÈ ÄÁÎÎÙÈ. üÔÁ
×ÅÒÓÉÑ ĞÏÄÄÅÒÖÉ×ÁÅÔ ÔÏÌØËÏ ÏÄÉÎ ÍÅÔÏÄ ËÏÍĞÒÅÓÓÉÉ (deflation), ÎÏ
×ĞÏÓÌÅÄÓÔ×ÉÉ × ÎÅÅ ÍÏÇÕÔ ÂÙÔØ ÄÏÂÁ×ÌÅÎÙ É ÄÒÕÇÉÅ ÍÅÔÏÄÙ, É ×ÓÅ ÏÎÉ
ÂÕÄÕÔ ÉÓĞÏÌØÚÏ×ÁÔØ ÔÏÔ ÖÅ ĞÏÔÏËÏ×ÙÊ ÉÎÔÅÒÆÅÊÓ.

%description -l tr
zlib sıkıştırma kitaplığı bellekte sıkıştırma ve açma fonksiyonları
içermektedir. Bu sürüm yalnızca 'deflation' yöntemini
desteklemektedir. Ancak başka algoritmaların aynı arabirimle
erişilebilecek şekilde eklenme olasılığı vardır. Bu kitaplık bir dizi
sistem yazılımı tarafından kullanılmaktadır.

%description -l uk
â¦ÂÌ¦ÏÔÅËÁ ËÏÍĞÒÅÓ¦§ zlib Í¦ÓÔÉÔØ ÆÕÎËÃ¦§ ËÏÍĞÒÅÓ¦§ ÔÁ ÄÅËÏÍĞÒÅÓ¦§ ×
ĞÁÍ'ÑÔ¦ Ú ĞÅÒÅ×¦ÒËÏÀ Ã¦ÌÏÓÔ¦ ÄÅËÏÍĞÒÅÓÏ×ÁÎÉÈ ÄÁÎÉÈ. ãÑ ×ÅÒÓ¦Ñ
Ğ¦ÄÔÒÉÍÕ¤ Ô¦ÌØËÉ ÏÄÉÎ ÍÅÔÏÄ ËÏÍĞÒÅÓ¦§ (deflation), ÁÌÅ × ÍÁÊÂÕÔÎØÏÍÕ ×
ÎÅ§ ÍÏÖÕÔØ ÂÕÔÉ ÄÏÄÁÎ¦ ¦ ¦ÎÛ¦ ÍÅÔÏÄÉ ¦ ×Ó¦ ×ÏÎÉ ÂÕÄÕÔØ ×ÉËÏÒÉÓÔÏ×Õ×ÁÔÉ
ÔÏÊ ÖÅ ÓÁÍÉÊ ĞÏÔÏËÏ×ÉÊ ¦ÎÔÅÒÆÅÊÓ.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1
%{?_with_asmopt:%patch1 -p1}

%if %{_asmopt}
%patch1 -p1
%ifarch i686 athlon
cp contrib/asm686/match.S .
%endif
%ifarch i586
cp contrib/asm586/match.S .
%endif
%endif
%patch2 -p1

%build
CC=%{target}-gcc ; export CC
CXX=%{target}-g++ ; export CXX
LD=%{target}-ld ; export LD
AR="%{target}-ar rc" ; export AR
AS=%{target}-as ; export AS
CROSS_COMPILE=1 ; export CROSS_COMPILE
CPPFLAGS="-I%{arch}/include" ; export CPPFLAGS
RANLIB=%{target}-ranlib ; export RANLIB
LDSHARED="%{target}-gcc -shared" ; export LDSHARED

./configure \
	--shared \
	--prefix=%{arch}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{arch}{/lib,/include}

install libz.a $RPM_BUILD_ROOT%{arch}/lib
install zutil.h $RPM_BUILD_ROOT%{arch}/include
%{__make} prefix=$RPM_BUILD_ROOT%{arch} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{arch}
