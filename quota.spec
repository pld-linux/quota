Summary:	Quota administration package
Summary(de):	Quotenverwaltungspaket 
Summary(fr):	Paquetage de gestion des quotas
Summary(pl):	Pakiet administaracyjny Quota
Summary(tr):	Kota denetleme paketi
Name:		quota
Version:	1.55
Release:	11d
URL:		ftp://sunsite.unc.edu/pub/Linux/system/Admin
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}.sh
Copyright:	BSD
Group:		Utilities/System
Group(pl):	U¿ytki/System
Patch0:		%{name}-misc.patch
Patch1:		%{name}-glibc.patch
Patch2:		%{name}-nfs.patch
Patch3:		%{name}-dbtob.patch
Buildroot:	/tmp/%{name}-%{version}-%{release}-root

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

%prep
%setup -q -c

(cd utils; tar xzf %{name}-%{version}.tar.gz )

%patch0 -p1 
%patch1 -p1 
%patch2 -p1 
%patch3 -p1 

%build
cd utils
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{sbin,usr/{bin,sbin,man/{man1,man2,man3,man8}}}

cd utils
make ROOTDIR=$RPM_BUILD_ROOT BIN_GROUP=`id -g` SUPER_OWNER=`id -u` \
    BIN_OWNER=`id -u` install

mv $RPM_BUILD_ROOT/usr/sbin/quota $RPM_BUILD_ROOT/usr/bin/quota

echo .so rquotad.8 > $RPM_BUILD_ROOT%{_mandir}/man8/rpc.rquotad.8

bzip2 -9 $RPM_BUILD_ROOT%{_mandir}/man[1238]/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) /sbin/quotacheck
%attr(755,root,root) /sbin/quotaon
%attr(755,root,root) /sbin/quotaoff
%attr(755,root,root) /usr/bin/quota
%attr(755,root,root) /usr/sbin/edquota
%attr(755,root,root) /usr/sbin/repquota
%attr(755,root,root) /usr/sbin/warnquota
%attr(755,root,root) /usr/sbin/quotastats
%attr(750,root,root) /usr/sbin/rpc.rquotad

%{_mandir}/man[1238]/*

%changelog
* Tue Jan 26 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.55-11d]
- rebuild on linux-2.2.0,
- compressed man pages,
- minor changes.

* Tue Aug 11 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.55-9d]
- translation modified for pl,
- build against glibc-2.1,
- moved %changelog at the end of spec,
- fixed files permisions,
- removed all patches and added quota.patch,
- changed quota-1.55.spec to quota.spec,
- build from non root's account.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- removed patch for mntent

* Tue Jan 13 1998 Erik Troan <ewt@redhat.com>
- builds rquotad
- installs rpc.rquotad.8 symlink

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- removed /usr/include/rpcsvc/* from filelist
- uses a buildroot and %attr

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Moved /usr/sbin/quota to /usr/bin/quota
