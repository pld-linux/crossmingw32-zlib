#
# Conditional build:
%bcond_without	asmopt	# without assmbler optimization for i586+
#
%ifnarch i586 i686 athlon
%undefine	with_asmopt
%endif
%define		realname		zlib
Summary:	Library for compression and decompression - Ming32 cross version
Summary(de):	Library für die Komprimierung und Dekomprimierung
Summary(es):	Biblioteca para compresión y descompresión
Summary(fr):	bibliothèque de compression et décompression
Summary(pl):	Biblioteka z podprogramami do kompresji i dekompresji - wersja skro¶na dla Ming32
Summary(pt_BR):	Biblioteca para compressão e descompressão
Summary(ru):	âÉÂÌÉÏÔÅËÁ ÄÌÑ ËÏÍÐÒÅÓÓÉÉ É ÄÅËÏÍÐÒÅÓÓÉÉ
Summary(tr):	Sýkýþtýrma iþlemleri için kitaplýk
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ ÄÌÑ ËÏÍÐÒÅÓ¦§ ÔÁ ÄÅËÏÍÐÒÅÓ¦§
Name:		crossmingw32-%{realname}
Version:	1.2.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.gzip.org/zlib/%{realname}-%{version}.tar.gz
# Source0-md5:	ef1cb003448b4a53517b8f25adb12452
Patch0:		%{realname}-asmopt.patch
URL:		http://www.zlib.org/
BuildRequires:	crossmingw32-gcc
Requires:	crossmingw32-runtime
BuildRoot:	%{tmpdir}/%{realname}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		arch			%{_prefix}/%{target}

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
âÉÂÌÉÏÔÅËÁ ËÏÍÐÒÅÓÓÉÉ zlib ÓÏÄÅÒÖÉÔ ÆÕÎËÃÉÉ ËÏÍÐÒÅÓÓÉÉ É ÄÅËÏÍÐÒÅÓÓÉÉ
× ÐÁÍÑÔÉ, ×ËÌÀÞÁÀ ÐÒÏ×ÅÒËÕ ÃÅÌÏÓÔÎÏÓÔÉ ÄÅËÏÍÐÒÅÓÓÉÒÏ×ÁÎÎÙÈ ÄÁÎÎÙÈ. üÔÁ
×ÅÒÓÉÑ ÐÏÄÄÅÒÖÉ×ÁÅÔ ÔÏÌØËÏ ÏÄÉÎ ÍÅÔÏÄ ËÏÍÐÒÅÓÓÉÉ (deflation), ÎÏ
×ÐÏÓÌÅÄÓÔ×ÉÉ × ÎÅÅ ÍÏÇÕÔ ÂÙÔØ ÄÏÂÁ×ÌÅÎÙ É ÄÒÕÇÉÅ ÍÅÔÏÄÙ, É ×ÓÅ ÏÎÉ
ÂÕÄÕÔ ÉÓÐÏÌØÚÏ×ÁÔØ ÔÏÔ ÖÅ ÐÏÔÏËÏ×ÙÊ ÉÎÔÅÒÆÅÊÓ.

%description -l tr
zlib sýkýþtýrma kitaplýðý bellekte sýkýþtýrma ve açma fonksiyonlarý
içermektedir. Bu sürüm yalnýzca 'deflation' yöntemini
desteklemektedir. Ancak baþka algoritmalarýn ayný arabirimle
eriþilebilecek þekilde eklenme olasýlýðý vardýr. Bu kitaplýk bir dizi
sistem yazýlýmý tarafýndan kullanýlmaktadýr.

%description -l uk
â¦ÂÌ¦ÏÔÅËÁ ËÏÍÐÒÅÓ¦§ zlib Í¦ÓÔÉÔØ ÆÕÎËÃ¦§ ËÏÍÐÒÅÓ¦§ ÔÁ ÄÅËÏÍÐÒÅÓ¦§ ×
ÐÁÍ'ÑÔ¦ Ú ÐÅÒÅ×¦ÒËÏÀ Ã¦ÌÏÓÔ¦ ÄÅËÏÍÐÒÅÓÏ×ÁÎÉÈ ÄÁÎÉÈ. ãÑ ×ÅÒÓ¦Ñ
Ð¦ÄÔÒÉÍÕ¤ Ô¦ÌØËÉ ÏÄÉÎ ÍÅÔÏÄ ËÏÍÐÒÅÓ¦§ (deflation), ÁÌÅ × ÍÁÊÂÕÔÎØÏÍÕ ×
ÎÅ§ ÍÏÖÕÔØ ÂÕÔÉ ÄÏÄÁÎ¦ ¦ ¦ÎÛ¦ ÍÅÔÏÄÉ ¦ ×Ó¦ ×ÏÎÉ ÂÕÄÕÔØ ×ÉËÏÒÉÓÔÏ×Õ×ÁÔÉ
ÔÏÊ ÖÅ ÓÁÍÉÊ ÐÏÔÏËÏ×ÉÊ ¦ÎÔÅÒÆÅÊÓ.

%prep
%setup -q -n %{realname}-%{version}

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
	--prefix=%{arch}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{arch}{/lib,/include}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{arch}

install zutil.h $RPM_BUILD_ROOT%{arch}/include

%{!?debug:%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{arch}/lib/libz.a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{arch}/include/*.h
%{arch}/lib/libz.a
