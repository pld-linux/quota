Summary:	Quota administration package
Summary(de):	Quotenverwaltungspaket 
Summary(fr):	Paquetage de gestion des quotas
Summary(pl):	Pakiet administaracyjny Quota
Summary(tr):	Kota denetleme paketi
Name:		quota
Version:	3.01
Release:	0.pre5.1
Epoch:		1
License:	BSD
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://prdownloads.sourceforge.net/linuxquota/%{name}-%{version}-pre5.tar.gz
URL:		http://sourceforge.net/projects/linuxquota/
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-man.patch
Patch2:		%{name}-defaults.patch
Patch3:		%{name}-fixfree.patch
Patch4:		%{name}-infinite.patch
Patch5:		%{name}-libwrap.patch
BuildRequires:	e2fsprogs-devel
BuildRequires:	libwrap-devel
BuildRequires:	autoconf
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

%description -l fr
Les quotas permettant à l'administrateur système de limiter
l'utilisation disque par un utilisateur et/ou un groupe par système de
fichiers. Ce paquetage contient les outils nécessaires à la mise en
place, la modification et la mise à jour des quotas.

%description -l pl
Quota pozwala administaratorowi systemu na ograniczanie wielko¶ci
miejsca na dysku dla u¿ytkownika/grupy. Pakiet ten zawiera narzêdzia
do aktywacji i modyfikacji Quoty.

%description -l tr
Kota, sistem yöneticisine, bir kullanýcýnýn ya da kullanýcý grubunun
disk kullanýmýný sýnýrlama yeteneði verir. Bu paket içerisindeki
yazýlýmlar kota sistemini kullanmak için gereken kontrol
yazýlýmlarýdýr.

%prep
%setup -q -n quota-tools
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2
%patch5 -p1

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

echo .so rquotad.8 > $RPM_BUILD_ROOT%{_mandir}/man8/rpc.rquotad.8

gzip -9 doc/{quota4th.fig,quotas-1.eps,quotas.ms}

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
%{_mandir}/man8/convertquota.8*
%{_mandir}/man8/edquota.8*
%{_mandir}/man8/quot.8*
%{_mandir}/man8/quotacheck.8*
%{_mandir}/man8/quotaon.8*
%{_mandir}/man8/repquota.8*
%{_mandir}/man8/setquota.8*
%{_mandir}/man8/warnquota.8*
