Summary:	guiftp - a simple FTP client using the GTK+ toolkit
Summary(pl):	guiftp - prosty klient FTP u¿ywaj±cy narzêdzi GTK+
Name:		guiftp
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ordiluc.net/guiftp/%{name}-%{version}.tar.bz2
# Source0-md5: 2587b3c216b4d0b24280b73230f4b7f8
URL:		http://ordiluc.net/guiftp
Buildrequires:	gtk+-devel >= 1.2.10
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
guiftp is a simple FTP client using the GTK+ toolkit.

%description -l pl
guiftp jest prostym klientem FTP u¿ywaj±cym narzêdzi GTK+.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT 

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
