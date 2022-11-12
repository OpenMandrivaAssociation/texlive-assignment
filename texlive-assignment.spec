Name:		texlive-assignment
Version:	20431
Release:	1
Summary:	A class file for typesetting homework and lab assignments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/assignment
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/assignment.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/assignment.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
