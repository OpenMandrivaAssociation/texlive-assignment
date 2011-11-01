Name:		texlive-assignment
Version:	20061012
Release:	1
Summary:	A class file for typesetting homework and lab assignments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/assignment
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/assignment.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/assignment.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A class file for typesetting homework and lab assignments.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
