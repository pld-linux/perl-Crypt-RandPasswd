#
# Conditional build:
%bcond_with	tests	# perform "make test"

%define		pdir	Crypt
%define		pnam	RandPasswd
Summary:	Crypt::RandPasswd Perl module - pronounceable passwords generator
Summary(pl.UTF-8):	Moduł Perla Crypt::RandPasswd - generator wymawialnych haseł
Name:		perl-Crypt-RandPasswd
Version:	0.02
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c266c6f10b59945d7dddc58ecef6e13b
URL:		http://search.cpan.org/dist/Crypt-RandPasswd/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This code is a Perl language implementation of the Automated Password
Generator standard, like the program described in "A Random Word
Generator For Pronounceable Passwords". This code is a re-engineering
of the program contained in Appendix A of FIPS Publication 181,
"Standard for Automated Password Generator".

%description -l pl.UTF-8
Ten moduł jest perlową implementacją standardu automatycznego
generatora haseł, takiego jak program opisany w "A Random Word
Generator For Pronounceable Passwords" (generator losowych słów na
potrzeby wymawialnych haseł). Ten kod jest ponowną implementacją
programu zawartego w załączniku A publikacji FIPS numer 181 "Standard
for Automated Password Generator".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

# it may hang on a machine that does not receive enough random events
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/RandPasswd.pm
%{_mandir}/man3/*
