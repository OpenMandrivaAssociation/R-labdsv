%global packname  labdsv
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.6.1
Release:          2
Summary:          Ordination and Multivariate Analysis for Ecology
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/labdsv_1.6-1.tar.gz
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

