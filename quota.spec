Summary:	Quota administration package
Summary(de):	Quotenverwaltungspaket 
Summary(fr):	Paquetage de gestion des quotas
Summary(pl):	Pakiet administaracyjny Quota
Summary(tr):	Kota denetleme paketi
Name:		quota
Version:	3.00
Release:	1
Source0:	ftp://ftp.cistron.nl/pub/people/mvw/quota/%{name}-2.00-pre4.tar.gz
Source1:	quota.sh
Copyright:	BSD
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Patch0:		quota-Makefile.patch
Patch1:		quota-man.patch
Patch2:		quota-rsquash.patch
Patch3:		quota-sparc.patch
Patch4:		quota-reiserfs.patch
BuildRequires:	e2fsprogs-devel
BuildRequires:	libwrap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quotas allow the system administrator to limit disk usage by a user and/or
group per filesystem. This package contains the tools which are needed to
enable, modify, and update quotas.

%description -l de
Quotas gestatten es dem Systemadministrator, die Festplattennutzung durch 
einen Anwender und/oder Gruppen pro Dateisystem zu beschr�nken. Es 
enth�lt die Tools, die zur Aktivierung, Modifikation und zum Aktualisieren 
von Quoten erforderlich sind."

%description -l fr
Les quotas permettant � l'administrateur syst�me de limiter l'utilisation
disque par un utilisateur et/ou un groupe par syst�me de fichiers. Ce paquetage
contient les outils n�cessaires � la mise en place, la modification et la mise
� jour des quotas.

%description -l pl
Quota pozwala administaratorowi systemu na ograniczanie wielko�ci miejsca 
na dysku dla u�ytkownika/grupy. Pakiet ten zawiera narz�dzia do aktywacji 
i modyfikacji Quoty. 

%description -l tr
Kota, sistem y�neticisine, bir kullan�c�n�n ya da kullan�c� grubunun disk
kullan�m�n� s�n�rlama yetene�i verir. Bu paket i�erisindeki yaz�l�mlar kota
sistemini kullanmak i�in gereken kontrol yaz�l�mlar�d�r.

%prep
%setup -q -n %{name}-2.00-pre4

%patch0 -p1
%patch1 -p2 
%patch2 -p2 
#%patch3 -p2 
#%patch4 -p1

%build
%{__make} OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/sbin,%{_bindir},%{_sbindir},%{_mandir}/man{1,2,3,8}}

%{__make} install \
	ROOTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir}

echo .so rquotad.8 > $RPM_BUILD_ROOT%{_mandir}/man8/rpc.rquotad.8

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[18]/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) /sbin/*
%attr(755,root,root) %{_sbindir}/edquota
%attr(755,root,root) %{_sbindir}/quotastats
%attr(755,root,root) %{_sbindir}/repquota
%attr(755,root,root) %{_sbindir}/setquota
%attr(755,root,root) %{_sbindir}/warnquota
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
%{_mandir}/man8/edquota.8*
%{_mandir}/man8/quotacheck.8*
%{_mandir}/man8/quotaon.8*
%{_mandir}/man8/repquota.8*
%{_mandir}/man8/setquota.8*
