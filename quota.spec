Summary:	Quota administration package
Summary(de):	Quotenverwaltungspaket
Summary(es):	Paquete de administraci�n cuota
Summary(fr):	Paquetage de gestion des quotas
Summary(pl):	Pakiet administaracyjny Quota
Summary(pt_BR):	Pacote de administra��o quota
Summary(ru):	������� ���������� �������������� ��� ���������� ��������� �������
Summary(tr):	Kota denetleme paketi
Summary(uk):	���̦�� ���������� ��ͦΦ�������� ��� ��������� ��������� �������
Name:		quota
Version:	3.04
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/System
Source0:	http://prdownloads.sourceforge.net/linuxquota/%{name}-%{version}.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
URL:		http://sourceforge.net/projects/linuxquota/
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-defaults.patch
Patch2:		%{name}-fixfree.patch
Patch3:		%{name}-libwrap.patch
BuildRequires:	e2fsprogs-devel
BuildRequires:	libwrap-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quotas allow the system administrator to limit disk usage by a user
and/or group per filesystem. This package contains the tools which are
needed to enable, modify, and update quotas.

%description -l de
Quotas gestatten es dem Systemadministrator, die Festplattennutzung
durch einen Anwender und/oder Gruppen pro Dateisystem zu beschr�nken.
Es enth�lt die Tools, die zur Aktivierung, Modifikation und zum
Aktualisieren von Quoten erforderlich sind."

%description -l es
Cuotas permite al administrador del sistema limitar el uso de disco
por un usuario y/o grupo por sistema de archivos. Este paquete
contiene las herramientas que son necesarias para activar, modificar y
actualizar cuotas.

%description -l fr
Les quotas permettant � l'administrateur syst�me de limiter
l'utilisation disque par un utilisateur et/ou un groupe par syst�me de
fichiers. Ce paquetage contient les outils n�cessaires � la mise en
place, la modification et la mise � jour des quotas.

%description -l pl
Quota pozwala administaratorowi systemu na ograniczanie wielko�ci
miejsca na dysku dla u�ytkownika/grupy. Pakiet ten zawiera narz�dzia
do aktywacji i modyfikacji Quoty.

%description -l pt_BR
Quotas permite ao administrador do sistema limitar o uso de disco por
um usu�rio e/ou grupo por sistema de arquivos. Este pacote cont�m as
ferramentas que s�o necess�rias para ativar, modificar e atualizar
quotas.

%description -l ru
����� quota �������� ������� ���������� �������������� ��� �����������
� ����������� ������������� ��������� ������������ �������������� � ��
�������� � ������ �������� �������.

%description -l tr
Kota, sistem y�neticisine, bir kullan�c�n�n ya da kullan�c� grubunun
disk kullan�m�n� s�n�rlama yetene�i verir. Bu paket i�erisindeki
yaz�l�mlar kota sistemini kullanmak i�in gereken kontrol
yaz�l�mlar�d�r.

%description -l uk
����� quota ͦ����� ���̦�� ���������� ��ͦΦ�������� ��� ��Φ�������
�� ��������� ������������ ��������� �������� ������������� �� ��
������� � ���Φ� �����צ� �����ͦ.

%prep
%setup -q -n quota-tools
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_bindir},%{_sbindir},%{_mandir}/man{1,2,3,8}}

%{__make} install \
	ROOTDIR=$RPM_BUILD_ROOT

echo .so quotaon.8 > $RPM_BUILD_ROOT%{_mandir}/man8/quotaoff.8
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/*rquotad.8

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT%{_mandir}/*/man8/*rquotad.8

gzip -9 doc/{quotas-1.eps,quotas.ms}

%find_lang quota

%clean
rm -rf $RPM_BUILD_ROOT

%files -f quota.lang
%defattr(644,root,root,755)
%doc doc/*.gz
%attr(755,root,root) /sbin/*
%attr(755,root,root) %{_sbindir}/edquota
%attr(755,root,root) %{_sbindir}/quot
%attr(755,root,root) %{_sbindir}/quotastats
%attr(755,root,root) %{_sbindir}/repquota
%attr(755,root,root) %{_sbindir}/setquota
%attr(755,root,root) %{_sbindir}/warnquota
%attr(755,root,root) %{_sbindir}/xqmstats
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_mandir}/man8/*

%lang(fi) %{_mandir}/fi/man1/*

%lang(hu) %{_mandir}/hu/man8/*

%lang(ja) %{_mandir}/ja/man1/*
%lang(ja) %{_mandir}/ja/man8/*

%lang(pl) %{_mandir}/pl/man1/*
%lang(pl) %{_mandir}/pl/man8/*
