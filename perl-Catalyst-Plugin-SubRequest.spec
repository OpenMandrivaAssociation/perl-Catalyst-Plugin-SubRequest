%define upstream_name    Catalyst-Plugin-SubRequest
%define upstream_version 0.21

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Make subrequests to actions in Catalyst
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://dev.catalyst.perl.org/repos/Catalyst/trunk/Catalyst-Plugin-SubRequest
Source0:	https://cpan.metacpan.org/authors/id/J/JJ/JJNAPIORK/Catalyst-Plugin-SubRequest-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Make subrequests to actions in Catalyst. Uses the catalyst dispatcher, so
it will work like an external url call.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

