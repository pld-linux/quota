Summary:	Quota administration package
Summary(de):	Quotenverwaltungspaket 
Summary(fr):	Paquetage de gestion des quotas
Summary(pl):	Pakiet administaracyjny Quota
Summary(tr):	Kota denetleme paketi
Name:		quota
Version:	1.66
Release:	1
URL:		ftp://sunsite.unc.edu/pub/Linux/system/Admin
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}.sh
Copyright:	BSD
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-glibc.patch
Patch2:		%{name}-man.patch
Patch3:		%{name}-dbtob.patch
BuildRequires:	e2fsprogs-static
Buildroot:	/tmp/%{name}-%{version}-root

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

install -d $RPM_BUILD_ROOT/{sbin,usr/{bin,sbin,share/man/{man{1,2,3,8}}}}

cd utils
make \
    ROOTDIR=$RPM_BUILD_ROOT \
    BIN_GROUP=`id -g` \
    SUPER_OWNER=`id -u` \
    BIN_OWNER=`id -u` \
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
