%define upstream_name 	 CGI-XML
%define upstream_version 0.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	CGI-XML perl module
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(XML::Parser)

Buildarch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Obsoletes:	perl-XML-CGI
Provides:	perl-XML-CGI

%description
CGI-XML converts CGI.pm variables to XML and vice versa.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
