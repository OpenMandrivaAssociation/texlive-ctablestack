Name:		texlive-ctablestack
Version:	38514
Release:	1
Summary:	Catcode table stable support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ctablestack
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctablestack.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctablestack.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctablestack.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a method for defining category code table
stacks in LuaTeX. It builds on code provided by the 2015/10/01
release of LaTeX2e (also available as ltluatex.sty for plain
users). It is required by the luatexbase package (v1.0 onward)
which uses ctablestack to provide a back-compatibility form of
this concept.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/luatex/ctablestack
%{_texmfdistdir}/tex/luatex/ctablestack
%doc %{_texmfdistdir}/doc/luatex/ctablestack

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
