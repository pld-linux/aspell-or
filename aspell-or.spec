Summary:	Oriya dictionary for aspell
Summary(pl.UTF-8):   Słownik orija dla aspella
Name:		aspell-or
Version:	0.03
%define	subv	1
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/or/aspell6-or-%{version}-%{subv}.tar.bz2
# Source0-md5:	6c9d702607eaa43ef665007c4b857ba4
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Oriya dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik orija (lista słów) dla aspella.

%prep
%setup -q -n aspell6-or-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
