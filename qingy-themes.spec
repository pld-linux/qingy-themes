%define		_name	qingy
Summary:	Qingy themepack
Summary(pl.UTF-8):   Motywy do Qingy
Name:		%{_name}-themes
Version:	1.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://dl.sourceforge.net/qingy/%{_name}_0.3_themepack_%{version}.tar.bz2
# Source0-md5:	578413ba5861c667674b6d65976a0370
URL:		http://qingy.sourceforge.net/themes.php
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	qingy >= 0.9.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Themepack for qingy. Empty main directory.

%description -l pl.UTF-8
Motywy do qingy. Pusty katalog główny.

%package -n %{_name}-theme-aquaish
Summary:	Qingy theme aquaish
Summary(pl.UTF-8):   Motyw aquaish dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-aquaish
Aquaish is an aqua-like theme for qingy.

%description -n %{_name}-theme-aquaish -l pl.UTF-8
Aquaish jest motywem dla qingy w stylu aqua.

%package -n %{_name}-theme-biohazard
Summary:	Qingy theme biohazard
Summary(pl.UTF-8):   Motyw biohazard dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-biohazard
Biohazard is an theme for qingy.

%description -n %{_name}-theme-biohazard -l pl.UTF-8
Biohazard jest motywem dla qingy.

%package -n %{_name}-theme-casablanca
Summary:	Qingy theme casablanca
Summary(pl.UTF-8):   Motyw kasablanka dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-casablanca
Casablanca is an theme for qingy.

%description -n %{_name}-theme-casablanca -l pl.UTF-8
Casablanca jest motywem dla qingy w stylu kasablanki.

%package -n %{_name}-theme-ComputerRoom
Summary:	Qingy theme ComputerRoom
Summary(pl.UTF-8):   Motyw ComputerRoom dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-ComputerRoom
ComputerRoom is an theme for qingy.

%description -n %{_name}-theme-ComputerRoom -l pl.UTF-8
ComputerRoom jest motywem dla qingy.

%package -n %{_name}-theme-fireplace
Summary:	Qingy theme fireplace
Summary(pl.UTF-8):   Motyw fireplace dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-fireplace
Fireplace is an theme for qingy.

%description -n %{_name}-theme-fireplace -l pl.UTF-8
Fireplace jest motywem dla qingy.

%package -n %{_name}-theme-frag
Summary:	Qingy theme frag
Summary(pl.UTF-8):   Motyw frag dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-frag
Frag is an theme for qingy.

%description -n %{_name}-theme-frag -l pl.UTF-8
Frag jest motywem dla qingy.

%package -n %{_name}-theme-gentoo
Summary:	Qingy theme gentoo
Summary(pl.UTF-8):   Motyw gentoo dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-gentoo
An gentoo-like theme for qingy.

%description -n %{_name}-theme-gentoo -l pl.UTF-8
Motyw dla qingy w stylu gentoo.

%package -n %{_name}-theme-gentoo_box
Summary:	Qingy theme gentoo_box
Summary(pl.UTF-8):   Motyw gentoo_box dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-gentoo_box
Another gentoo theme for qingy.

%description -n %{_name}-theme-gentoo_box -l pl.UTF-8
Kolejny motyw dla qingy w stylu gentoo.

%package -n %{_name}-theme-kitten
Summary:	Qingy theme kitten
Summary(pl.UTF-8):   Motyw kitten dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-kitten
Kitten is an theme for qingy.

%description -n %{_name}-theme-kitten -l pl.UTF-8
Kitten jest motywem dla qingy.

%package -n %{_name}-theme-lambretta
Summary:	Qingy theme lambretta
Summary(pl.UTF-8):   Motyw lambretta dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-lambretta
Lambretta is an theme for qingy.

%description -n %{_name}-theme-lambretta -l pl.UTF-8
lambretta jest motywem dla qingy.

%package -n %{_name}-theme-matrix
Summary:	Qingy theme matrix
Summary(pl.UTF-8):   Motyw matrix dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-matrix
An matrix-like theme for qingy.

%description -n %{_name}-theme-matrix -l pl.UTF-8
Motyw dla qingy w stylu matriksa.

%package -n %{_name}-theme-vendetta
Summary:	Qingy theme vendetta
Summary(pl.UTF-8):   Motyw vendetta dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-vendetta
Vendetta is an theme for qingy.

%description -n %{_name}-theme-vendetta -l pl.UTF-8
Vendetta jest motywem dla qingy.

%package -n %{_name}-theme-vendetta2
Summary:	Qingy theme vendetta2
Summary(pl.UTF-8):   Motyw vendetta2 dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-vendetta2
Another vendetta theme for qingy.

%description -n %{_name}-theme-vendetta2 -l pl.UTF-8
Kolejny motyw dla qingy w stylu vendetta.

%package -n %{_name}-theme-vendetta3
Summary:	Qingy theme vendetta3
Summary(pl.UTF-8):   Motyw vendetta3 dla qingy
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description -n %{_name}-theme-vendetta3
Another vendetta theme for qingy.

%description -n %{_name}-theme-vendetta3 -l pl.UTF-8
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
