%define oname smplayer

Summary:	SMPlayer is a complete front-end for mplayer written in Qt4
Name:		smplayer-qt4
Version:	0.5.62
Release:	%mkrel 2
License:	GPLv2+
Group:		Video
Url:		http://smplayer.sourceforge.net
Source0:	http://smplayer.sourceforge.net/porting/%{oname}-%{version}.tar.bz2
BuildRequires:	qt4-devel	>= 4.2.0
BuildRequires:	qt4-linguist	>= 4.2.0
Requires:	mplayer		>= 1.0-1.rc1
Conflicts:	smplayer
Suggests:	smplayer-themes
Obsoletes:	%{oname}-qt4
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
SMPlayer intends to be a complete front-end for MPlayer,
from basic features like playing videos, DVDs, and VCDs 
to more advanced features like support for MPlayer filters and more.

One of the most interesting features of SMPlayer: it remembers the 
settings of all files you play. So you start to watch a movie but you 
have to leave... don't worry, when you open that movie again it will 
resume at the same point you left it, and with the same settings: 
audio track, subtitles, volume...

Other additional interesting features:

* New GUI. Now there are toolbars, the control at the bottom is different 
  (and it changes if the window is made smaller), the icons can be changed 
  (several icon themes are available). In fullscreen mode the floating 
  control that appears when you move the mouse to the bottom of the screen 
  is new too and this time the video doesn't resize when it shows.
* Configurable key shortcuts. A shortcut editor has been added, it's 
  located at "Preferences->Mouse & keyboard". Please read 
  Configurable_shortcuts.txt.
* Support for VCD. Now you can also play VCD discs.
* System tray icon. Now it's possible to leave SMPlayer running in the 
  system tray. This feature requires Qt 4.2.
* Added some new functions, like pan&scan, stay on top, set the size 
  of the window...
* Improved support for subtitles. For instance, now you can load a idx/sub 
  file and you'll be able to select among all languages that the file 
  provides. You can have a mkv file with embedded subtitles, load an 
  idx/sub file (or srt, sub...) and all subtitles will be available.
* New translations. SMPlayer 0.5.0 is translated (totally or partially) to 
  the following languages: Bulgarian, Czech, German, Spanish, French, 
  Hungarian, Italian, Japanese, Georgian, Dutch, Polish, Brazilian Portuguese, 
  Russian, Slovak, Serbian, Swedish, Turkish, Ukrainian, Simplified-Chinese 
  and Traditional Chinese. By the way, now it's possible to change the language 
  at run-time.
				
SMPlayer supports themes which can be found in smplayer-themes package.

This is SMplayer port for QT4 toolkit, which is under heavy development right now. 
Do NOT expect that everything will be working out of box.

%prep
%setup -qn %{oname}-%{version}

%build
%make PREFIX=%{_prefix} QMAKE=%{qt4bin}/qmake LRELEASE=%{qt4bin}/lrelease
#KDE_SUPPORT=1

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std PREFIX=%{_prefix}

# remove wrongly put docs
rm -rf %{buildroot}%{_datadir}/doc

desktop-file-install \
	--remove-key='Encoding' \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

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
%dir %{_datadir}/%{oname}
%dir %{_datadir}/%{oname}/shortcuts
%dir %{_datadir}/%{oname}/translations
%attr(755,root,root) %{_bindir}/%{oname}
%{_datadir}/%{oname}/*.conf
%{_iconsdir}/hicolor/*/apps/%{oname}.png
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/%{oname}/shortcuts/*
%{_datadir}/%{oname}/translations/qt_fr.qm
%lang(bg) %{_datadir}/%{oname}/translations/smplayer_bg.qm
%lang(cs) %{_datadir}/%{oname}/translations/smplayer_cs.qm
%lang(de) %{_datadir}/%{oname}/translations/smplayer_de.qm
%lang(el_GR) %{_datadir}/%{oname}/translations/smplayer_el_GR.qm
%lang(en_US) %{_datadir}/%{oname}/translations/smplayer_en_US.qm
%lang(es) %{_datadir}/%{oname}/translations/smplayer_es.qm
%lang(fr) %{_datadir}/%{oname}/translations/smplayer_fr.qm
%lang(hu) %{_datadir}/%{oname}/translations/smplayer_hu.qm
%lang(it) %{_datadir}/%{oname}/translations/smplayer_it.qm
%lang(ja) %{_datadir}/%{oname}/translations/smplayer_ja.qm
%lang(ka) %{_datadir}/%{oname}/translations/smplayer_ka.qm
%lang(nl) %{_datadir}/%{oname}/translations/smplayer_nl.qm
%lang(pl) %{_datadir}/%{oname}/translations/smplayer_pl.qm
%lang(pt_BR) %{_datadir}/%{oname}/translations/smplayer_pt_BR.qm
%lang(pt_pt) %{_datadir}/%{oname}/translations/smplayer_pt_PT.qm
%lang(ro_RO) %{_datadir}/%{oname}/translations/smplayer_ro_RO.qm
%lang(ru_RU) %{_datadir}/%{oname}/translations/smplayer_ru_RU.qm
%lang(sk) %{_datadir}/%{oname}/translations/smplayer_sk.qm
%lang(sr) %{_datadir}/%{oname}/translations/smplayer_sr.qm
%lang(sv) %{_datadir}/%{oname}/translations/smplayer_sv.qm
%lang(tr) %{_datadir}/%{oname}/translations/smplayer_tr.qm
%lang(uk_UA) %{_datadir}/%{oname}/translations/smplayer_uk_UA.qm
%lang(zh_CN) %{_datadir}/%{oname}/translations/smplayer_zh_CN.qm
%lang(zh_TW) %{_datadir}/%{oname}/translations/smplayer_zh_TW.qm
