Name:		texlive-hyphen-french
Version:	20111102
Release:	1
Summary:	French hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-french.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-hyphen-base
Requires:	texlive-hyph-utf8
Conflicts:	texlive-texmf <= 20110705-3
Requires(post):	texlive-hyphen-base

%description
Hyphenation patterns for French in T1/EC and UTF-8 encodings.

%pre
    %_texmf_language_dat_pre
    %_texmf_language_def_pre
    %_texmf_language_lua_pre

%post
    %_texmf_language_dat_post
    %_texmf_language_def_post
    %_texmf_language_lua_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_pre
	%_texmf_language_def_pre
	%_texmf_language_lua_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_post
	%_texmf_language_def_post
	%_texmf_language_lua_post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-french
%_texmf_language_def_d/hyphen-french
%_texmf_language_lua_d/hyphen-french

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-french <<EOF
%% from hyphen-french:
french loadhyph-fr.tex
=patois
=francais
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-french <<EOF
%% from hyphen-french:
\addlanguage{french}{loadhyph-fr.tex}{}{2}{3}
\addlanguage{patois}{loadhyph-fr.tex}{}{2}{3}
\addlanguage{francais}{loadhyph-fr.tex}{}{2}{3}
EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-french <<EOF
-- from hyphen-french:
	['french'] = {
		loader = 'loadhyph-fr.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = { 'patois', 'francais' },
		patterns = 'hyph-fr.pat.txt',
		hyphenation = '',
	},
EOF
