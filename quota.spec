Summary:	Quota administration package
Summary(de):	Quotenverwaltungspaket 
Summary(fr):	Paquetage de gestion des quotas
Summary(pl):	Pakiet administaracyjny Quota
Summary(tr):	Kota denetleme paketi
Name:		quota
Version:	3.00.3
Release:	1
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/local/jack/quota/utils/%{name}-3.00-3.tar.gz
Source1:	rquotad.init
Source2:	rquotad.sysconfig
Patch0:		%{name}-opt.patch
Patch1:		%{name}-edquota.patch
Patch2:		%{name}-setquota.patch
Copyright:	BSD
Group:		Utilities/System
Group(pl):	Narzêdzia/System
BuildRequires:	e2fsprogs-devel
BuildRequires:	libwrap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quotas allow the system administrator to limit disk usage by a user and/or
group per filesystem. This package contains the tools which are needed to
enable, modify, and update quotas.

%description -l de
Quotas gestatten es dem Systemadministrator, die Festplattennutzung durch 
einen Anwender und/oder Gruppen pro Dateisystem zu beschränken. Es 
enthält die Tools, die zur Aktivierung, Modifikation und zum Aktualisieren 
von Quoten erforderlich sind."

%description -l fr
Les quotas permettant à l'administrateur système de limiter l'utilisation
disque par un utilisateur et/ou un groupe par système de fichiers. Ce paquetage
contient les outils nécessaires à la mise en place, la modification et la mise
à jour des quotas.

%description -l pl
Quota pozwala administaratorowi systemu na ograniczanie wielko¶ci miejsca 
na dysku dla u¿ytkownika/grupy. Pakiet ten zawiera narzêdzia do aktywacji 
i modyfikacji Quoty. 

%description -l tr
Kota, sistem yöneticisine, bir kullanýcýnýn ya da kullanýcý grubunun disk
kullanýmýný sýnýrlama yeteneði verir. Bu paket içerisindeki yazýlýmlar kota
sistemini kullanmak için gereken kontrol yazýlýmlarýdýr.

%package rquotad
Summary:	Remote quota server
Summary(pl):	Zdalny serwer quota
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Requires:	rc-scripts
Requires:	portmap >= 4.0
Requires:	%{name} = %{version}
Obsoletes:	nfs-utils-rquotad

%description rquotad
rquotad is an rpc(3N) server which returns quotas for a user of a
local file system which is mounted by a remote machine over the NFS.
The results are used by quota(1) to display user quotas for remote
file systems.

%description -l pl rquotad
Zdalny serwer quota.

%prep
%setup -q -n %{name}-3.00
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	RPC=1 \
	RPC_SERVER=1 \
	EXT2_DIRECT=1 \
	OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_bindir},%{_sbindir},%{_mandir}/man{1,2,3,8}}
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

install -s convertquota $RPM_BUILD_ROOT/sbin/convertquota
install -s quotacheck $RPM_BUILD_ROOT/sbin/quotacheck
install -s quotaon $RPM_BUILD_ROOT/sbin/quotaon
ln -s quotaon $RPM_BUILD_ROOT/sbin/quotaoff
install -s quota $RPM_BUILD_ROOT%{_bindir}/quota
install -s edquota $RPM_BUILD_ROOT%{_sbindir}/edquota
install -s quotadebug $RPM_BUILD_ROOT%{_sbindir}/quotadebug
install -s quotastats $RPM_BUILD_ROOT%{_sbindir}/quotastats
install -s repquota $RPM_BUILD_ROOT%{_sbindir}/repquota
install -s setquota $RPM_BUILD_ROOT%{_sbindir}/setquota
install -s rpc.rquotad $RPM_BUILD_ROOT%{_sbindir}/rpc.rquotad

install quota.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install quotactl.2 $RPM_BUILD_ROOT%{_mandir}/man2/
install rquota.3 $RPM_BUILD_ROOT%{_mandir}/man3/
install *.8 $RPM_BUILD_ROOT%{_mandir}/man8/

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/rquotad
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rquotad

echo .so rquotad.8 > $RPM_BUILD_ROOT%{_mandir}/man8/rpc.rquotad.8

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[1238]/*

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

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/*
%attr(755,root,root) %{_sbindir}/edquota
%attr(755,root,root) %{_sbindir}/quotadebug
%attr(755,root,root) %{_sbindir}/quotastats
%attr(755,root,root) %{_sbindir}/repquota
%attr(755,root,root) %{_sbindir}/setquota
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man2/*
%{_mandir}/man8/convertquota.8*
%{_mandir}/man8/edquota.8*
%{_mandir}/man8/quotacheck.8*
%{_mandir}/man8/quotaon.8*
%{_mandir}/man8/quotastats.8*
%{_mandir}/man8/repquota.8*
%{_mandir}/man8/setquota.8*

%files rquotad
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/rquotad
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rquotad
%attr(755,root,root) %{_sbindir}/rpc.rquotad
%{_mandir}/man8/*rquotad.8*
