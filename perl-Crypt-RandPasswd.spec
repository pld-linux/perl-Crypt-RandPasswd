#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	RandPasswd
Summary:	Crypt::RandPasswd Perl module - pronounceable passwords generator
Summary(pl):	Modu³ Perla Crypt::RandPasswd - generator wymawialnych hase³
Name:		perl-Crypt-RandPasswd
Version:	0.02
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c266c6f10b59945d7dddc58ecef6e13b
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

%description -l pl
Ten modu³ jest perlow± implementacj± standardu automatycznego
generatora hase³, takiego jak program opisany w "A Random Word
Generator For Pronounceable Passwords" (generator losowych s³ów na
potrzeby wymawialnych hase³). Ten kod jest ponown± implementacj±
programu zawartego w za³±czniku A o publikacji FIPS numer 181 "Standard
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
