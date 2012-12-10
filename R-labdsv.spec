%global packname  labdsv
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.4_1
Release:          1
Summary:          Ordination and Multivariate Analysis for Ecology
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-1.tar.gz
Requires:         R-mgcv
Requires:         R-MASS 
Requires:         R-rgl 
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex
BuildRequires:    R-mgcv
BuildRequires:    R-MASS
BuildRequires:    R-rgl 
BuildRequires:    pkgconfig(lapack)
%rename R-cran-labdsv

%description
A variety of ordination and vegetation analyses useful in analysis of
datasets in community ecology.  Includes many of the common ordination
methods, with graphical routines to facilitate their interpretation, as
well as several novel analyses.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
#%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4_1-1
+ Revision: 775051
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3_1-1
+ Revision: 774862
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-3mdv2011.0
+ Revision: 616449
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.3.1-2mdv2010.0
+ Revision: 433082
- rebuild

* Wed Jun 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.1-1mdv2009.0
+ Revision: 228956
- add buildrequires on gcc-gfortran
- import R-cran-labdsv

