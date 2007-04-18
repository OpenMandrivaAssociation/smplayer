Summary:	SMplayer is a new front-end for mplayer
Name:		smplayer
Version:	0.3.27
Release:	%mkrel 1
License:	GPL
Group:		Video
Url:		http://smplayer.sourceforge.net/
Source0:	http://smplayer.sourceforge.net/download/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
BuildRequires:	libqt-devel	>= 3.3.7
Requires:	mplayer
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
SMplayer is a new front-end for mplayer. It intends to be a much more 
complete front-end than the existing ones, for instance options to manage 
filters. SMplayer is multi-platform as it is being developed with the 
Qt toolkit. It works both in windows and linux, and it could be 
compile in other OS.

%prep
%setup -q

%build

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,22x22,32x32,64x64}/apps
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/%{name}/translations

install src/%{name} %{buildroot}%{_bindir}
install %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install src/*.qm %{buildroot}%{_datadir}/%{name}/translations
install src/*.conf %{buildroot}%{_datadir}/%{name}
install icons/smplayer_icon16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install icons/smplayer_icon22.png %{buildroot}%{_iconsdir}/hicolor/22x22/apps/%{name}.png
install icons/smplayer_icon32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install icons/smplayer_icon64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png

%post
%{update_menus}
%if %mdkversion >= 200700
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%postun
%{clean_menus}
%if %mdkversion >= 200700
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc Changelog *.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/*.conf
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%lang(es) %{_datadir}/%{name}/translations/smplayer_es.qm
%lang(de) %{_datadir}/%{name}/translations/smplayer_de.qm
%lang(en_US) %{_datadir}/%{name}/translations/smplayer_en_US.qm
%lang(fr) %{_datadir}/%{name}/translations/smplayer_fr.qm
%lang(hu) %{_datadir}/%{name}/translations/smplayer_hu.qm
%lang(it) %{_datadir}/%{name}/translations/smplayer_it.qm
%lang(ja) %{_datadir}/%{name}/translations/smplayer_ja.qm
%lang(ka) %{_datadir}/%{name}/translations/smplayer_ka.qm
%lang(nl) %{_datadir}/%{name}/translations/smplayer_nl.qm
%lang(pl) %{_datadir}/%{name}/translations/smplayer_pl.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/smplayer_pt_BR.qm
%lang(ru_RU) %{_datadir}/%{name}/translations/smplayer_ru_RU.qm
%lang(sk) %{_datadir}/%{name}/translations/smplayer_sk.qm
%lang(uk_UA) %{_datadir}/%{name}/translations/smplayer_uk_UA.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/smplayer_zh_CN.qm
