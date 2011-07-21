Summary:	IBus front-end for fbterm
Name:		ibus-fbterm
Version:	0.9.1
Release:	0.1
License:	GPL v3
Group:		Applications/System
Source0:	http://ibus-fbterm.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	966e4f275500979b78dd1303e96ca32d
Patch0:		%{name}-uni-shell.patch
URL:		http://code.google.com/p/ibus-fbterm
BuildRequires:	ibus-devel >= 1.2
Requires:	ibus >= 1.2
Requires:	fbterm >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ibus-fbterm is a input method for FbTerm based on iBus.

%prep
%setup -q
%patch0 -p1

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
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/ibus-fbterm
%attr(755,root,root) %{_bindir}/ibus-fbterm-launch
