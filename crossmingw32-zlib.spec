
%ifnarch i586 i686 athlon
%define				_asmopt		0
%else
%{?_without_asmopt:%define	_asmopt		0}
%{!?_without_asmopt:%define	_asmopt		1}
%endif

%define		realname		zlib
Summary:	Library for compression and decompression
Summary(de):	Library f�r die Komprimierung und Dekomprimierung
Summary(es):	Biblioteca para compresi�n y descompresi�n
Summary(fr):	biblioth�que de compression et d�compression
Summary(pl):	Biblioteka z podprogramami do kompresji i dekompresji
Summary(pt_BR):	Biblioteca para compress�o e descompress�o
Summary(ru):	���������� ��� ���������� � ������������
Summary(tr):	S�k��t�rma i�lemleri i�in kitapl�k
Summary(uk):	��̦����� ��� ������Ӧ� �� ��������Ӧ�
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
und Dekomprimierungsfunktionen, einschlie�lich Integrit�tspr�fungen
der unkomprimierten Daten. Diese Version der Library unterst�tzt nur
eine Komprimierungsmethode (Deflation), doch k�nnen weitere
Algorithmen nachtr�glich eingef�gt werden und haben dann dieselbe
Oberfl�che.

%description -l es
La biblioteca de compresi�n 'zlib' nos ofrece funciones de compresi�n
y descompresi�n en memoria, incluyendo chequeo de la integridad de
datos no comprimidos. Esta versi�n de la biblioteca soporta solamente
un m�todo de compresi�n (deflaci�n) pero otros algoritmos pueden ser
a�adidos m�s tarde y tendr�n la misma interface. Esta biblioteca se
usa por varios programas de sistema.

%description -l fr
La biblioth�que de compression � zlib � offre des fonctions de
compression et de d�compression en m�moire, ainsi qu'une v�rification
de l'int�grit� des donn�es d�compress�es. La version de cette
biblioth�que ne g�re qu'une m�thode de compression (deflation), mais
d'autres algorithmes peuvent �tre ajout�s plus tard et auront la m�me
interface.

%description -l pl
Biblioteka zlib udost�pnia podprogramy do kompresji i dekompresji w
pami�ci operacyjnej w��cznie ze sprawdzaniem integralno�ci w trakcie
dekompresji. Ta wersja biblioteki udost�pnia tylko jedn� metod�
kompresji o nazwie deflation niemniej inne algorytmy mog� by�
dodawane udost�pniaj�c taki sam interfejs funkcji operuj�cych na
strumieniu danych.

%description -l pt_BR
A biblioteca de compress�o 'zlib' oferece fun��es de compress�o e
descompress�o em mem�ria, incluindo checagem da integridade de dados
n�o comprimidos. Essa vers�o da biblioteca suporta somente um m�todo
de compress�o (defla��o) mas outros algoritmos podem ser adicionados
mais tarde e ter�o a mesma interface. Essa biblioteca � usada por
v�rios programas de sistema.

%description -l ru
���������� ���������� zlib �������� ������� ���������� � ������������
� ������, ������� �������� ����������� ������������������� ������. ���
������ ������������ ������ ���� ����� ���������� (deflation), ��
������������ � ��� ����� ���� ��������� � ������ ������, � ��� ���
����� ������������ ��� �� ��������� ���������.

%description -l tr
zlib s�k��t�rma kitapl��� bellekte s�k��t�rma ve a�ma fonksiyonlar�
i�ermektedir. Bu s�r�m yaln�zca 'deflation' y�ntemini
desteklemektedir. Ancak ba�ka algoritmalar�n ayn� arabirimle
eri�ilebilecek �ekilde eklenme olas�l��� vard�r. Bu kitapl�k bir dizi
sistem yaz�l�m� taraf�ndan kullan�lmaktad�r.

%description -l uk
��̦����� ������Ӧ� zlib ͦ����� ����æ� ������Ӧ� �� ��������Ӧ� �
���'�Ԧ � ����צ���� æ���Ԧ ��������������� �����. �� ���Ӧ�
Ц�����դ Ԧ���� ���� ����� ������Ӧ� (deflation), ��� � ����������� �
�ŧ ������ ���� ����Φ � ��ۦ ������ � �Ӧ ���� ������ ���������������
��� �� ����� ��������� ���������.

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
