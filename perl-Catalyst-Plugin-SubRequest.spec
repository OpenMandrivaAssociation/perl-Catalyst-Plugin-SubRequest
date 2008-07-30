%define realname   Catalyst-Plugin-SubRequest
%define version    0.13
%define release    %mkrel 3

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Make subrequests to actions in Catalyst
Source:     http://www.cpan.org/modules/by-module/Catalyst/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(Test::More)
BuildArch: noarch

%description

Make subrequests to actions in Catalyst. Uses the catalyst dispatcher, so
it will work like an external url call.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*

