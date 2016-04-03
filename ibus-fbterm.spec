Summary:	IBus front-end for fbterm
Summary(pl.UTF-8):	Interfejs platformy IBus dla fbterma
Name:		ibus-fbterm
Version:	1.0.1
Release:	1
License:	GPL v3
Group:		Applications/System
#Source0Download: https://github.com/fujiwarat/ibus-fbterm/releases
Source0:	https://github.com/fujiwarat/ibus-fbterm/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3ea4c7385567765b73002a48f98503f3
URL:		https://github.com/fujiwarat/ibus-fbterm
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	ibus-devel >= 1.5.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	vala >= 2:0.20
Requires:	glib2 >= 1:2.32.0
Requires:	ibus >= 1.5.0
Requires:	fbterm >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
ibus-fbterm is a input method for FbTerm based on IBus.

%description -l pl.UTF-8
ibus-fbterm to oparta na platformie IBus metoda wprowadzania znaków
dla FbTerma.

%prep
%setup -q

%{__sed} -i -e 's,/usr/libexec/,%{_libexecdir}/,g' ibus-fbterm

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/ibus-fbterm
%attr(755,root,root) %{_libexecdir}/ibus-fbterm-backend
%{_mandir}/man1/ibus-fbterm.1*
