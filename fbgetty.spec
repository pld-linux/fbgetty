Summary:	getty program for Linux framebuffer console
Summary(pl.UTF-8):	Program getty dla linuksowej konsoli z framebufferem
Name:		fbgetty
Version:	0.1.698
Release:	6
License:	GPL v2+
Group:		Applications/System
Source0:	http://projects.meuh.org/fbgetty/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	1705bc0f8f1e03fe50d324ba84ac4e56
Patch0:		%{name}-info.patch
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
%patch -P0 -p1

%build
cp -f /usr/share/automake/config.* config
export CPPFLAGS="%{rpmcppflags} -Doffsetof=__builtin_offsetof"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO docs/*.txt
%attr(755,root,root) %{_sbindir}/fbgetty
%{_mandir}/man8/fbgetty.8*
%{_infodir}/fbgetty.info*
