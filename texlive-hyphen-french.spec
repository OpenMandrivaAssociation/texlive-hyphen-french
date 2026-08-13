%global tl_name hyphen-french
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	French hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-french
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-french.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for French in T1/EC and UTF-8 encodings.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-french:
french loadhyph-fr.tex
=patois
=francais
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-french:
\addlanguage{french}{loadhyph-fr.tex}{}{2}{2}
\addlanguage{patois}{loadhyph-fr.tex}{}{2}{2}
\addlanguage{francais}{loadhyph-fr.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-french:
['french'] = {
	loader = 'loadhyph-fr.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = { 'patois', 'francais' },
	patterns = 'hyph-fr.pat.txt',
},
TL_HYPHEN_EOF
