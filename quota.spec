# TODO:
# - add warnquota as cron job
#
# Conditional build:
%bcond_with	kernel64	# build 32bit userland for 64bit kernel
#

# possibly also sparc and ppc
%ifnarch %{ix86}
%undefine	with_kernel64
%endif

Summary:	Quota administration package%{?with_kernel64: - 32bit userland for 64bit kernel}
Summary(de.UTF-8):	Quotenverwaltungspaket
Summary(es.UTF-8):	Paquete de administración cuota
Summary(fr.UTF-8):	Paquetage de gestion des quotas
Summary(pl.UTF-8):	Pakiet administaracyjny Quota%{?with_kernel64: - 32 bitowe programy dla 64 bitowego jądra}
Summary(pt_BR.UTF-8):	Pacote de administração quota
Summary(ru.UTF-8):	Утилиты системного администратора для управления дисковыми квотами
Summary(tr.UTF-8):	Kota denetleme paketi
Summary(uk.UTF-8):	Утиліти системного адміністратора для керування дисковими квотами
Summary(zh_CN.UTF-8):	磁盘使用情况的监控工具
Name:		quota%{?with_kernel64:64}
Version:	3.15
Release:	2
Epoch:		1
License:	BSD
Group:		Applications/System
Source0:	http://dl.sourceforge.net/linuxquota/quota-%{version}.tar.gz
# Source0-md5:	5a1c2f5e669aba825e0126d2f30ee622
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/quota-non-english-man-pages.tar.bz2
# Source1-md5:	05a209bc054366ea190d1c67669f9ca3
Source2:	rquotad.init
Source3:	rquotad.sysconfig
URL:		http://sourceforge.net/projects/linuxquota/
Patch0:		quota-defaults.patch
Patch1:		quota-pl.po-update.patch
Patch2:		quota-repquota-len-fix.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	e2fsprogs-devel
BuildRequires:	gettext-devel
BuildRequires:	libwrap-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/quota-%{version}-root-%(id -u -n)

%description
Quotas allow the system administrator to limit disk usage by a user
and/or group per filesystem. This package contains the tools which are
needed to enable, modify, and update quotas.

%if %{with kernel64}
Warning: This package is for 32bit systems running on 64bit kernel!
%endif

%description -l de.UTF-8
Quotas gestatten es dem Systemadministrator, die Festplattennutzung
durch einen Anwender und/oder Gruppen pro Dateisystem zu beschränken.
Es enthält die Tools, die zur Aktivierung, Modifikation und zum
Aktualisieren von Quoten erforderlich sind."

%description -l es.UTF-8
Cuotas permite al administrador del sistema limitar el uso de disco
por un usuario y/o grupo por sistema de archivos. Este paquete
contiene las herramientas que son necesarias para activar, modificar y
actualizar cuotas.

%description -l fr.UTF-8
Les quotas permettant à l'administrateur système de limiter
l'utilisation disque par un utilisateur et/ou un groupe par système de
fichiers. Ce paquetage contient les outils nécessaires à la mise en
place, la modification et la mise à jour des quotas.

%description -l pl.UTF-8
Quota pozwala administratorowi systemu na ograniczanie wielkości
miejsca na dysku dla użytkownika/grupy. Pakiet ten zawiera narzędzia
do aktywacji i modyfikacji Quoty.

%if %{with kernel64}
Uwaga: Ten pakiet jest przeznaczony wyłącznie dla 32 bitowych systemów
       działających na 64 bitowym jądrze!
%endif

%description -l pt_BR.UTF-8
Quotas permite ao administrador do sistema limitar o uso de disco por
um usuário e/ou grupo por sistema de arquivos. Este pacote contém as
ferramentas que são necessárias para ativar, modificar e atualizar
quotas.

%description -l ru.UTF-8
Пакет quota содержит утилиты системного администратора для мониторинга
и ограничения использования дискового пространства пользователями и их
группами в каждой файловой системе.

%description -l tr.UTF-8
Kota, sistem yöneticisine, bir kullanıcının ya da kullanıcı grubunun
disk kullanımını sınırlama yeteneği verir. Bu paket içerisindeki
yazılımlar kota sistemini kullanmak için gereken kontrol
yazılımlarıdır.

%description -l uk.UTF-8
Пакет quota містить утиліти системного адміністратора для моніторингу
та обмеження використання дискового простору користувачами та їх
групами в кожній файловій системі.

%package rquotad
Summary:	Remote quota server
Summary(pl.UTF-8):	Zdalny serwer quota
Group:		Networking/Daemons
Requires(post,preun):	/sbin/chkconfig
Requires:	portmap >= 4.0
Requires:	rc-scripts >= 0.4.1.5
Obsoletes:	nfs-utils-rquotad

%description rquotad
rquotad is an rpc(3N) server which returns quotas for a user of a
local file system which is mounted by a remote machine over the NFS.
The results are used by quota(1) to display user quotas for remote
file systems.

%if %{with kernel64}
Warning: This package is for 32bit systems running on 64bit kernel!
%endif

%description rquotad -l pl.UTF-8
rquotad jest serverem rpc(3N), który zwraca quoty użytkownika
lokalnego systemu plików, który jest zamountowany przez zdalną maszynę
poprzez NFS. Rezultaty są używane przez quota(1), aby wyświetlić quote
dla zdalnego systemu plików.

%if %{with kernel64}
Uwaga: Ten pakiet jest przeznaczony wyłącznie dla 32 bitowych systemów
       działających na 64 bitowym jądrze!
%endif

%prep
%setup -q -n quota-tools
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}

%if %{with kernel64}
CFLAGS="%{rpmcflags} -malign-double"
export CFLAGS
%endif

%configure \
	--enable-rpcsetquota

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,/etc/{rc.d/init.d,sysconfig}}

%{__make} install \
	ROOTDIR=$RPM_BUILD_ROOT

# essential, used by rc-scripts
mv -f $RPM_BUILD_ROOT%{_sbindir}/{quotacheck,quotaon,quotaoff,convertquota} \
	$RPM_BUILD_ROOT/sbin

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
%service rquotad restart "RPC rquotad"

%preun rquotad
if [ "$1" = "0" ]; then
	%service rquotad stop
	/sbin/chkconfig --del rquotad
fi

%triggerpostun rquotad -- quota-rquotad < 3.14-3
/sbin/chkconfig rquotad reset

%files -f quota.lang
%defattr(644,root,root,755)
%doc Changelog doc/{quotas-1.eps,quotas.ms} quotatab
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/quotagrpadmins
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/quotatab
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/warnquota.conf
%attr(755,root,root) /sbin/convertquota
%attr(755,root,root) /sbin/quotacheck
%attr(755,root,root) /sbin/quotaoff
%attr(755,root,root) /sbin/quotaon
%attr(755,root,root) %{_sbindir}/edquota
%attr(755,root,root) %{_sbindir}/quotastats
%attr(755,root,root) %{_sbindir}/quot
%attr(755,root,root) %{_sbindir}/repquota
%attr(755,root,root) %{_sbindir}/setquota
%attr(755,root,root) %{_sbindir}/warnquota
%attr(755,root,root) %{_sbindir}/xqmstats
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_mandir}/man8/quot*.8*
%{_mandir}/man8/*quota.8*
%{_mandir}/man8/xqmstats.8*

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
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rquotad

%{_mandir}/man8/*rquotad.8*
%lang(fr) %{_mandir}/fr/man8/*rquotad.8*
%lang(ja) %{_mandir}/ja/man8/*rquotad.8*
