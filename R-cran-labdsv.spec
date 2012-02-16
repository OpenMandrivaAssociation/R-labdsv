%define modulename labdsv
%define realver 1.3-1
%define r_library %{_libdir}/R/library

Summary:	R ordination and multivariate analysis for ecology
Name:		R-cran-%{modulename}
Version:	%(echo %realver|tr '-' '.')
Release:	%mkrel 3
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
BuildRequires:	gcc-gfortran
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A variety of ordination and vegetation analyses useful in 
analysis of datasets in community ecology.Includes many of 
the common ordination methods, with graphical routines to 
facilitate their interpretation, as well as several novel 
analyses.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
