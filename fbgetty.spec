Summary:	getty program for Linux framebuffer console
Summary(pl):	Program getty dla linuksowej konsoli z framebufferem
Name:		fbgetty
Version:	0.1.698
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://fbgetty.meuh.eu.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	1705bc0f8f1e03fe50d324ba84ac4e56
Patch0:		%{name}-info.patch
URL:		http://fbgetty.meuh.eu.org/
BuildRequires:	automake
BuildRequires:	texinfo
Requires:	login
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fbgetty is a new getty program that supports fully capabilities of the
Linux console. For the moment it run only under Linux.

Features:
- extended issue display (escape codes, shell variables)
- framebuffer support (display logo) [not yet]
- refresh issue when VT is activated (time, user, uptime)
- display date/time according to locale
- display the output of any program
- include many files in issue

%description -l pl
fbgetty to nowy program getty w pe³ni obs³uguj±cy mo¿liwo¶ci
linuksowej konsoli. Aktualnie dzia³a tylko pod Linuksem.

Mo¿liwo¶ci:
- wy¶wietlanie rozszerzonego issue (kody specjalne, zmienne pow³oki)
- obs³uga framebuffera (wy¶wietlanie logo) [jeszcze nie dzia³a]
- od¶wie¿anie przy aktywacji VT (czas, liczba u¿ytkowników, uptime)
- wy¶wietlanie daty i czasu zgodnie z ustawieniami lokalnymi
- wy¶wietlanie wyj¶cia dowolnego programu
- do³±czanie wielu plików do issue.

%prep
%setup -q
%patch -p1

%build
cp -f /usr/share/automake/config.* config
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO docs/*.txt
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%{_infodir}/*.info*
