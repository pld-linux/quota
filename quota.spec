Summary:	Quota administration package
Summary(de):	Quotenverwaltungspaket
Summary(es):	Paquete de administración cuota
Summary(fr):	Paquetage de gestion des quotas
Summary(pl):	Pakiet administaracyjny Quota
Summary(pt_BR):	Pacote de administração quota
Summary(ru):	õÔÉÌÉÔÙ ÓÉÓÔÅÍÎÏÇÏ ÁÄÍÉÎÉÓÔÒÁÔÏÒÁ ÄÌÑ ÕÐÒÁ×ÌÅÎÉÑ ÄÉÓËÏ×ÙÍÉ Ë×ÏÔÁÍÉ
Summary(tr):	Kota denetleme paketi
Summary(uk):	õÔÉÌ¦ÔÉ ÓÉÓÔÅÍÎÏÇÏ ÁÄÍ¦Î¦ÓÔÒÁÔÏÒÁ ÄÌÑ ËÅÒÕ×ÁÎÎÑ ÄÉÓËÏ×ÉÍÉ Ë×ÏÔÁÍÉ
Summary(zh_CN):	´ÅÅÌÊ¹ÓÃÇé¿öµÄ¼à¿Ø¹¤¾ß
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
durch einen Anwender und/oder Gruppen pro Dateisystem zu beschränken.
Es enthält die Tools, die zur Aktivierung, Modifikation und zum
Aktualisieren von Quoten erforderlich sind."

%description -l es
Cuotas permite al administrador del sistema limitar el uso de disco
por un usuario y/o grupo por sistema de archivos. Este paquete
contiene las herramientas que son necesarias para activar, modificar y
actualizar cuotas.

%description -l fr
Les quotas permettant à l'administrateur système de limiter
l'utilisation disque par un utilisateur et/ou un groupe par système de
fichiers. Ce paquetage contient les outils nécessaires à la mise en
place, la modification et la mise à jour des quotas.

%description -l pl
Quota pozwala administaratorowi systemu na ograniczanie wielko¶ci
miejsca na dysku dla u¿ytkownika/grupy. Pakiet ten zawiera narzêdzia
do aktywacji i modyfikacji Quoty.

%description -l pt_BR
Quotas permite ao administrador do sistema limitar o uso de disco por
um usuário e/ou grupo por sistema de arquivos. Este pacote contém as
ferramentas que são necessárias para ativar, modificar e atualizar
quotas.

%description -l ru
ðÁËÅÔ quota ÓÏÄÅÒÖÉÔ ÕÔÉÌÉÔÙ ÓÉÓÔÅÍÎÏÇÏ ÁÄÍÉÎÉÓÔÒÁÔÏÒÁ ÄÌÑ ÍÏÎÉÔÏÒÉÎÇÁ
É ÏÇÒÁÎÉÞÅÎÉÑ ÉÓÐÏÌØÚÏ×ÁÎÉÑ ÄÉÓËÏ×ÏÇÏ ÐÒÏÓÔÒÁÎÓÔ×Á ÐÏÌØÚÏ×ÁÔÅÌÑÍÉ É ÉÈ
ÇÒÕÐÐÁÍÉ × ËÁÖÄÏÊ ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÅ.

%description -l tr
Kota, sistem yöneticisine, bir kullanýcýnýn ya da kullanýcý grubunun
disk kullanýmýný sýnýrlama yeteneði verir. Bu paket içerisindeki
yazýlýmlar kota sistemini kullanmak için gereken kontrol
yazýlýmlarýdýr.

%description -l uk
ðÁËÅÔ quota Í¦ÓÔÉÔØ ÕÔÉÌ¦ÔÉ ÓÉÓÔÅÍÎÏÇÏ ÁÄÍ¦Î¦ÓÔÒÁÔÏÒÁ ÄÌÑ ÍÏÎ¦ÔÏÒÉÎÇÕ
ÔÁ ÏÂÍÅÖÅÎÎÑ ×ÉËÏÒÉÓÔÁÎÎÑ ÄÉÓËÏ×ÏÇÏ ÐÒÏÓÔÏÒÕ ËÏÒÉÓÔÕ×ÁÞÁÍÉ ÔÁ §È
ÇÒÕÐÁÍÉ × ËÏÖÎ¦Ê ÆÁÊÌÏ×¦Ê ÓÉÓÔÅÍ¦.

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
rquotad jest serverem rpc(3N), który zwraca quoty u¿ytkownika
lokalnego systemu plików, który jest zamountowany przez zdaln± maszynê
poprzez NFS. Rezultaty s± u¿ywane przez quota(1), aby wy¶wietliæ quote
dla zdalnego systemu plików.

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
