Summary:	Quota administration package
Summary(de):	Quotenverwaltungspaket 
Summary(fr):	Paquetage de gestion des quotas
Summary(pl):	Pakiet administaracyjny Quota
Summary(tr):	Kota denetleme paketi
Name:		quota
Version:	1.70
Release:	1
Source0:	ftp://ftp.cistron.nl/pub/people/mvw/quota/%{name}-%{version}.tar.gz
Source1:	quota.sh
Copyright:	BSD
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Patch0:		quota-Makefile.patch
Patch1:		quota-glibc.patch
Patch2:		quota-man.patch
Patch3:		quota-dbtob.patch
Patch4:		quota-rsquash.patch
Patch5:		quota-sparc.patch
Patch6:		quota-setquota.patch
BuildRequires:	e2fsprogs-devel
Buildroot:	/tmp/%{name}-%{version}-root

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
%setup -q -n %{name}

%patch0 -p1 -b .pld 
%patch1 -p2 
%patch2 -p2 
%patch3 -p2 
%patch4 -p2 
%patch5 -p2 
%patch6 -p1

%build
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/sbin,%{_bindir},%{_sbindir},%{_mandir}/man{1,2,3,8}}

make \
    ROOTDIR=$RPM_BUILD_ROOT \
    mandir=%{_mandir} \
    install

echo .so rquotad.8 > $RPM_BUILD_ROOT%{_mandir}/man8/rpc.rquotad.8

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[18]/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) /sbin/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man[18]/*
