%define		_name	qingy
Summary:	Qingy themepack
Summary(pl):	Motywy do Qingy
Name:		%{_name}-themes
Version:	1.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://dl.sourceforge.net/qingy/%{_name}_0.3_themepack_%{version}.tar.bz2
# Source0-md5:	578413ba5861c667674b6d65976a0370
URL:		http://qingy.sourceforge.net/themes.php
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	quingy >= 0.9.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Themepack for qingy. Empty main directory.

%description -l pl
Motywy do qingy. Pusty katalog g³ówny.

%package -n %{_name}-theme-aquaish
Summary:	Qingy theme aquaish
Summary(pl):	Motyw aquaish dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-aquaish
Aquaish is an aqua-like theme for qingy.

%description -n %{_name}-theme-aquaish -l pl
Aquaish jest motywem dla qingy w stylu aqua.

%package -n %{_name}-theme-biohazard
Summary:	Qingy theme biohazard
Summary(pl):	Motyw biohazard dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-biohazard
Biohazard is an theme for qingy.

%description -n %{_name}-theme-biohazard -l pl
Biohazard jest motywem dla qingy.

%package -n %{_name}-theme-casablanca
Summary:	Qingy theme casablanca
Summary(pl):	Motyw kasablanka dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-casablanca
Casablanca is an theme for qingy.

%description -n %{_name}-theme-casablanca -l pl
Casablanca jest motywem dla qingy w stylu kasablanki.

%package -n %{_name}-theme-ComputerRoom
Summary:	Qingy theme ComputerRoom
Summary(pl):	Motyw ComputerRoom dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-ComputerRoom
ComputerRoom is an theme for qingy.

%description -n %{_name}-theme-ComputerRoom -l pl
ComputerRoom jest motywem dla qingy.

%package -n %{_name}-theme-fireplace
Summary:	Qingy theme fireplace
Summary(pl):	Motyw fireplace dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-fireplace
Fireplace is an theme for qingy.

%description -n %{_name}-theme-fireplace -l pl
Fireplace jest motywem dla qingy.

%package -n %{_name}-theme-frag
Summary:	Qingy theme frag
Summary(pl):	Motyw frag dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-frag
Frag is an theme for qingy.

%description -n %{_name}-theme-frag -l pl
Frag jest motywem dla qingy.

%package -n %{_name}-theme-gentoo
Summary:	Qingy theme gentoo
Summary(pl):	Motyw gentoo dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-gentoo
An gentoo-like theme for qingy.

%description -n %{_name}-theme-gentoo -l pl
Motyw dla qingy w stylu gentoo.

%package -n %{_name}-theme-gentoo_box
Summary:	Qingy theme gentoo_box
Summary(pl):	Motyw gentoo_box dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-gentoo_box
Another gentoo theme for qingy.

%description -n %{_name}-theme-gentoo_box -l pl
Kolejny motyw dla qingy w stylu gentoo.

%package -n %{_name}-theme-kitten
Summary:	Qingy theme kitten
Summary(pl):	Motyw kitten dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-kitten
Kitten is an theme for qingy.

%description -n %{_name}-theme-kitten -l pl
Kitten jest motywem dla qingy.

%package -n %{_name}-theme-lambretta
Summary:	Qingy theme lambretta
Summary(pl):	Motyw lambretta dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-lambretta
Lambretta is an theme for qingy.

%description -n %{_name}-theme-lambretta -l pl
lambretta jest motywem dla qingy.

%package -n %{_name}-theme-matrix
Summary:	Qingy theme matrix
Summary(pl):	Motyw matrix dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-matrix
An matrix-like theme for qingy.

%description -n %{_name}-theme-matrix -l pl
Motyw dla qingy w stylu matriksa.

%package -n %{_name}-theme-vendetta
Summary:	Qingy theme vendetta
Summary(pl):	Motyw vendetta dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-vendetta
Vendetta is an theme for qingy.

%description -n %{_name}-theme-vendetta -l pl
Vendetta jest motywem dla qingy.

%package -n %{_name}-theme-vendetta2
Summary:	Qingy theme vendetta2
Summary(pl):	Motyw vendetta2 dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-vendetta2
Another vendetta theme for qingy.

%description -n %{_name}-theme-vendetta2 -l pl
Kolejny motyw dla qingy w stylu vendetta.

%package -n %{_name}-theme-vendetta3
Summary:	Qingy theme vendetta3
Summary(pl):	Motyw vendetta3 dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-vendetta3
Another vendetta theme for qingy.

%description -n %{_name}-theme-vendetta3 -l pl
Kolejny motyw dla qingy w stylu vendetta.

%prep
%setup -q -n %{_name}_0.3_themepack_%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/qingy/themes/{aquaish,biohazard,casablanca,ComputerRoom,fireplace,frag,gentoo,gentoo_box,kitten,lambretta,matrix,vendetta,vendetta2,vendetta3}
for i in `ls |grep -v README`; do install $i/* $RPM_BUILD_ROOT%{_datadir}/qingy/themes/$i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_datadir}/qingy/themes

%files -n %{_name}-theme-aquaish
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/aquaish
%{_datadir}/qingy/themes/aquaish

%files -n %{_name}-theme-biohazard
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/biohazard
%{_datadir}/qingy/themes/biohazard

%files -n %{_name}-theme-casablanca
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/casablanca
%{_datadir}/qingy/themes/casablanca

%files -n %{_name}-theme-ComputerRoom
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/ComputerRoom
%{_datadir}/qingy/themes/ComputerRoom

%files -n %{_name}-theme-fireplace
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/fireplace
%{_datadir}/qingy/themes/fireplace

%files -n %{_name}-theme-frag
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/frag
%{_datadir}/qingy/themes/frag

%files -n %{_name}-theme-gentoo
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/gentoo
%{_datadir}/qingy/themes/gentoo

%files -n %{_name}-theme-gentoo_box
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/gentoo_box
%{_datadir}/qingy/themes/gentoo_box

%files -n %{_name}-theme-kitten
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/kitten
%{_datadir}/qingy/themes/kitten

%files -n %{_name}-theme-lambretta
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/lambretta
%{_datadir}/qingy/themes/lambretta

%files -n %{_name}-theme-matrix
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/matrix
%{_datadir}/qingy/themes/matrix

%files -n %{_name}-theme-vendetta
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/vendetta
%{_datadir}/qingy/themes/vendetta

%files -n %{_name}-theme-vendetta2
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/vendetta2
%{_datadir}/qingy/themes/vendetta2

%files -n %{_name}-theme-vendetta3
%defattr(644,root,root,755)
%dir %{_datadir}/qingy/themes/vendetta3
%{_datadir}/qingy/themes/vendetta3
