#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Math
%define		pnam	Int128
Summary:	Math::Int128 - Manipulate 128 bits integers in Perl
Summary(pl.UTF-8):	Math::Int128 - operowanie na 128-bitowych liczbach całkowitych w Perlu
Name:		perl-Math-Int128
Version:	0.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	626603153c162a3fb95b76c68db9ea2b
URL:		https://metacpan.org/dist/Math-Int128
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Math-Int64 >= 0.51
BuildRequires:	perl-Test-Simple >= 0.96
%endif
# __int128 available only in -m64 mode
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds support for 128 bit integers, signed and unsigned, to
Perl.

In order to compile this module, your compiler must support one of
either the "__int128" or "int __attribute__ ((__mode__ (TI)))" types.
Both GCC and Clang have supported one or the other type for some time,
but they may only do so on 64-bit platforms.

%description -l pl.UTF-8
Ten moduł dodaje do Perla obsługę 128-bitowych liczb całkowitych -
zarówno ze znakiem, jak i bez.

Moduł polega na obsłudze przez kompilator jednego z typów "__int128"
lub "int __attribute__ ((__mode__ (TI)))". Zarówno GCC i Clang
obsługują przynajmniej jeden z nich od jakiegoś czasu, ale być może
tylko na platformach 64-bitowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Math/Int128.pm
%{perl_vendorarch}/Math/Int128
%dir %{perl_vendorarch}/auto/Math/Int128
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Int128/Int128.so
%{_mandir}/man3/Math::Int128.3pm*
%{_mandir}/man3/Math::Int128::die_on_overflow.3pm*
