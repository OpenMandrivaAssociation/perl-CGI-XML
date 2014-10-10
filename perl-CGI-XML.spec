%define upstream_name 	 CGI-XML
%define upstream_version 0.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	CGI-XML perl module
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)

BuildArch:  noarch

%rename	perl-XML-CGI

%description
CGI-XML converts CGI.pm variables to XML and vice versa.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
%make

%install
install -d %{buildroot}%{perl_archlib}
%makeinstall_std
install -d %{buildroot}%{_datadir}

%files 
%doc README MANIFEST Changes  examples
%{perl_vendorlib}/CGI/*
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 680701
- mass rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 504608
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1-9mdv2010.0
+ Revision: 430317
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.1-8mdv2009.0
+ Revision: 241169
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.1-6mdv2008.0
+ Revision: 67609
- use %%mkrel


* Fri Sep 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.1-6mdk
- rebuild

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 0.1-5mdk
- Fix summary and description
- macroize
- %%makeinstall_std

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1-4mdk
- rebuild for new auto{prov,req}

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.1-3mdk
- rebuild

* Mon Jul 22 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.1-2mdk
- rebuild with new perl

* Mon Jul 16 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1-1mdk
- updated by Christian Zoffoli <czoffoli@linux-mandrake.com> :
	- 0.1
	- changed name

* Tue Feb 20 2001 Christian Zoffoli <czoffoli@linux-mandrake.com> 0.02-2mdk
- little changes in licence

* Tue Feb 20 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.02-1mdk
- added in contribs by Christian Zoffoli <czoffoli@linux-mandrake.com>:
	- First Mandrake release

