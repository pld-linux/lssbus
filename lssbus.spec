Summary:	Simple utility to list sbus/ebus devices
Summary(pl.UTF-8):	Proste narzędzie do wypisywania urządzeń sbus/ebus
Name:		lssbus
Version:	0.1
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://people.redhat.com/tcallawa/lssbus/%{name}-%{version}.tar.gz
# Source0-md5:	b10a7600fa08a0e5894eb9845af2b5bd
URL:		http://people.redhat.com/tcallawa/lssbus/
ExclusiveArch:	sparc sparc64 sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lssbus is a simple Linux/SPARC utility to list sbus/ebus devices.

%description -l pl.UTF-8
lssbus to proste narzędzie dla architektury Linux/SPARC wypisujące
urządzenia sbus/ebus.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -D_GNU_SOURCE" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/lssbus
