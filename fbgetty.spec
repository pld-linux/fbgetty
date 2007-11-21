Summary:	getty program for Linux framebuffer console
Summary(pl.UTF-8):	Program getty dla linuksowej konsoli z framebufferem
Name:		fbgetty
Version:	0.1.698
Release:	5
License:	GPL v2+
Group:		Applications/System
Source0:	http://projects.meuh.org/fbgetty/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	1705bc0f8f1e03fe50d324ba84ac4e56
Patch0:		%{name}-info.patch
Patch1:		%{name}-debian.patch
URL:		http://projects.meuh.org/fbgetty/
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

%description -l pl.UTF-8
fbgetty to nowy program getty w pełni obsługujący możliwości
linuksowej konsoli. Aktualnie działa tylko pod Linuksem.

Możliwości:
- wyświetlanie rozszerzonego issue (kody specjalne, zmienne powłoki)
- obsługa framebuffera (wyświetlanie logo) [jeszcze nie działa]
- odświeżanie przy aktywacji VT (czas, liczba użytkowników, uptime)
- wyświetlanie daty i czasu zgodnie z ustawieniami lokalnymi
- wyświetlanie wyjścia dowolnego programu
- dołączanie wielu plików do issue.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* config
CPPFLAGS="-Doffsetof=__builtin_offsetof"; export CPPFLAGS
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
