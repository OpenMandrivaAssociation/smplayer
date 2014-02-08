Name:		smplayer
Summary:	Complete front-end for mplayer written in Qt4
Version:	0.8.5
Release:	2
License:	GPLv2+
Group:		Video
Url:		http://smplayer.sourceforge.net
Source0:	http://downloads.sourceforge.net/smplayer/%{name}-%{version}.tar.bz2
Patch0:		smplayer-0.8.4-optflags.patch
BuildRequires:	qt4-devel
BuildRequires:	desktop-file-utils
Requires:	mplayer
Suggests:	smplayer-themes
Obsoletes:	smplayer-qt4 < 0.5.62-1
Provides:	smplayer-qt4 = %{version}-%{release}

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

%prep
%setup -q
%patch0 -p1

%build
# (tpg) don't use kde dialogs
#KDE_SUPPORT=1
%setup_compile_flags
%make PREFIX=%{_prefix} 'DOC_PATH=\"%{_docdir}/%{name}\"'

%install
%makeinstall_std PREFIX=%{_prefix}

# Allow html docs
mv %{buildroot}%{_docdir}/packages/%{name} %{buildroot}%{_docdir}/%{name}
rm -fr %{buildroot}%{_docdir}/packages

desktop-file-install \
	--remove-key='Encoding' \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%files
%doc Changelog *.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/shortcuts
%dir %{_datadir}/%{name}/translations
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_datadir}/%{name}/*.conf
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.svg
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/shortcuts/*
%lang(ar_SY) %{_datadir}/%{name}/translations/smplayer_ar_SY.qm
%lang(bg) %{_datadir}/%{name}/translations/smplayer_bg.qm
%lang(ca) %{_datadir}/%{name}/translations/smplayer_ca.qm
%lang(cs) %{_datadir}/%{name}/translations/smplayer_cs.qm
%lang(de) %{_datadir}/%{name}/translations/smplayer_de.qm
%lang(da) %{_datadir}/%{name}/translations/smplayer_da.qm
%lang(el_GR) %{_datadir}/%{name}/translations/smplayer_el_GR.qm
%lang(en_US) %{_datadir}/%{name}/translations/smplayer_en_US.qm
%lang(es) %{_datadir}/%{name}/translations/smplayer_es.qm
%lang(et) %{_datadir}/%{name}/translations/smplayer_et.qm
%lang(eu) %{_datadir}/%{name}/translations/smplayer_eu.qm
%lang(fi) %{_datadir}/%{name}/translations/smplayer_fi.qm
%lang(fr) %{_datadir}/%{name}/translations/smplayer_fr.qm
%lang(gl) %{_datadir}/%{name}/translations/smplayer_gl.qm
%lang(he_IL) %{_datadir}/%{name}/translations/smplayer_he_IL.qm
%lang(hr) %{_datadir}/%{name}/translations/smplayer_hr.qm
%lang(hu) %{_datadir}/%{name}/translations/smplayer_hu.qm
%lang(it) %{_datadir}/%{name}/translations/smplayer_it.qm
%lang(ja) %{_datadir}/%{name}/translations/smplayer_ja.qm
%lang(ka) %{_datadir}/%{name}/translations/smplayer_ka.qm
%lang(ko) %{_datadir}/%{name}/translations/smplayer_ko.qm
%lang(ku) %{_datadir}/%{name}/translations/smplayer_ku.qm
%lang(lt) %{_datadir}/%{name}/translations/smplayer_lt.qm
%lang(mk) %{_datadir}/%{name}/translations/smplayer_mk.qm
%lang(nl) %{_datadir}/%{name}/translations/smplayer_nl.qm
%lang(pl) %{_datadir}/%{name}/translations/smplayer_pl.qm
%lang(pt) %{_datadir}/%{name}/translations/smplayer_pt.qm
%lang(pt_BR) %{_datadir}/%{name}/translations/smplayer_pt_BR.qm
%lang(ro_RO) %{_datadir}/%{name}/translations/smplayer_ro_RO.qm
%lang(ru_RU) %{_datadir}/%{name}/translations/smplayer_ru_RU.qm
%lang(sk) %{_datadir}/%{name}/translations/smplayer_sk.qm
%lang(sl) %{_datadir}/%{name}/translations/smplayer_sl_SI.qm
%lang(sr) %{_datadir}/%{name}/translations/smplayer_sr.qm
%lang(sv) %{_datadir}/%{name}/translations/smplayer_sv.qm
%lang(th) %{_datadir}/%{name}/translations/smplayer_th.qm
%lang(tr) %{_datadir}/%{name}/translations/smplayer_tr.qm
%lang(uk_UA) %{_datadir}/%{name}/translations/smplayer_uk_UA.qm
%lang(vi) %{_datadir}/%{name}/translations/smplayer_vi_VN.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/smplayer_zh_CN.qm
%lang(zh_TW) %{_datadir}/%{name}/translations/smplayer_zh_TW.qm
%lang(my_MY) %{_datadir}/%{name}/translations/smplayer_ms_MY.qm
