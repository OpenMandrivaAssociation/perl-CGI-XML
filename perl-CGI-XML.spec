%define module 	CGI-XML
%define version 0.1
%define release %mkrel 9

Summary:	CGI-XML perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/
Source0:	%{module}-%{version}.tar.bz2
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel >= 5.6
Requires:	perl >= 5.6
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Obsoletes:	perl-XML-CGI
Provides:	perl-XML-CGI
Buildarch: noarch

%description
CGI-XML converts CGI.pm variables to XML and vice versa.


%prep

%setup -q -n %{module}-%{version}


%build

CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make


%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__install} -d $RPM_BUILD_ROOT%{perl_archlib}

%makeinstall_std

%{__install} -d $RPM_BUILD_ROOT/%{_datadir}


%clean 
%{__rm} -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README MANIFEST Changes  examples
%{perl_vendorlib}/CGI/*
%{_mandir}/*/*


