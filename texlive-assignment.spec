# revision 20431
# category Package
# catalog-ctan /macros/latex/contrib/assignment
# catalog-date 2006-10-12 15:12:24 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-assignment
Version:	20061012
Release:	5
Summary:	A class file for typesetting homework and lab assignments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/assignment
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/assignment.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/assignment.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A class file for typesetting homework and lab assignments.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/assignment/assignment.cls
%doc %{_texmfdistdir}/doc/latex/assignment/Changelog
%doc %{_texmfdistdir}/doc/latex/assignment/LICENSE
%doc %{_texmfdistdir}/doc/latex/assignment/README
%doc %{_texmfdistdir}/doc/latex/assignment/assignment.pdf
%doc %{_texmfdistdir}/doc/latex/assignment/assignment.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061012-2
+ Revision: 749356
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061012-1
+ Revision: 717863
- texlive-assignment
- texlive-assignment
- texlive-assignment
- texlive-assignment
- texlive-assignment

