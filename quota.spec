Summary:	Quota administration package
Summary(de):	Quotenverwaltungspaket
Summary(es):	Paquete de administraci�n cuota
Summary(fr):	Paquetage de gestion des quotas
Summary(pl):	Pakiet administaracyjny Quota
Summary(pt_BR):	Pacote de administra��o quota
Summary(ru):	������� ���������� �������������� ��� ���������� ��������� �������
Summary(tr):	Kota denetleme paketi
Summary(uk):	���̦�� ���������� ��ͦΦ�������� ��� ��������� ��������� �������
Summary(zh_CN):	����ʹ������ļ�ع���
Name:		quota
Version:	3.10
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/System
Source0:	http://dl.sourceforge.net/linuxquota/%{name}-%{version}.tar.gz
# Source0-md5:	a7e76cb4554e64a07df746ab0d85cc59
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	05a209bc054366ea190d1c67669f9ca3
Source2:	r%{name}d.init
Source3:	r%{name}d.sysconfig
URL:		http://sourceforge.net/projects/linuxquota/
Patch0:		%{name}-defaults.patch
Patch1:		%{name}-pl.po-update.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
BuildRequires:	gettext-devel
BuildRequires:	libwrap-devel
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

%package rquotad
Summary:	Remote quota server
Summary(pl):	Zdalny serwer quota
Group:		Networking/Daemons
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	portmap >= 4.0
Obsoletes:	nfs-utils-rquotad

%description rquotad
rquotad is an rpc(3N) server which returns quotas for a user of a
local file system which is mounted by a remote machine over the NFS.
The results are used by quota(1) to display user quotas for remote
file systems.

%description rquotad -l pl
rquotad jest serverem rpc(3N), kt�ry zwraca quoty u�ytkownika
lokalnego systemu plik�w, kt�ry jest zamountowany przez zdaln� maszyn�
poprzez NFS. Rezultaty s� u�ywane przez quota(1), aby wy�wietli� quote
dla zdalnego systemu plik�w.

%prep
%setup -q -n quota-tools
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,2,3,8}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

%{__make} install \
	ROOTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/rquotad
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/rquotad

echo ".so quotaon.8" > $RPM_BUILD_ROOT%{_mandir}/man8/quotaoff.8
echo ".so rquotad.8" >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.rquotad.8

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang quota

%clean
rm -rf $RPM_BUILD_ROOT

%post rquotad
/sbin/chkconfig --add rquotad
if [ -r /var/lock/subsys/rquotad ]; then
	/etc/rc.d/init.d/rquotad restart >&2
else
	echo "Run \"/etc/rc.d/init.d/rquotad start\" to start NFS quota daemon."
fi

%preun rquotad
if [ "$1" = "0" ]; then
	if [ -r /var/lock/subsys/rquotad ]; then
		/etc/rc.d/init.d/rquotad stop >&2
	fi
	/sbin/chkconfig --del rquotad
fi

%files -f quota.lang
%defattr(644,root,root,755)
%doc doc/{quotas-1.eps,quotas.ms} quotatab
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/quotagrpadmins
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/quotatab
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/warnquota.conf
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_mandir}/man8/quot*.8*
%{_mandir}/man8/*quota.8*

%lang(fi) %{_mandir}/fi/man1/*

%lang(hu) %{_mandir}/hu/man8/*

%lang(ja) %{_mandir}/ja/man1/*
%lang(ja) %{_mandir}/ja/man8/quota*
%lang(ja) %{_mandir}/ja/man8/edquota.8*
%lang(ja) %{_mandir}/ja/man8/repquota.8*
%lang(ja) %{_mandir}/ja/man8/setquota.8*

%lang(pl) %{_mandir}/pl/man1/*
%lang(pl) %{_mandir}/pl/man8/*

%files rquotad
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rpc.rquotad
%attr(754,root,root) /etc/rc.d/init.d/rquotad
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rquotad

%{_mandir}/man8/*rquotad.8*
%lang(fr) %{_mandir}/fr/man8/*rquotad.8*
%lang(ja) %{_mandir}/ja/man8/*rquotad.8*
