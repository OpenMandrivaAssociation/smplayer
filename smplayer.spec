Summary:	SMPlayer is a complete front-end for mplayer
Name:		smplayer
Version:	0.4.29
Release:	%mkrel 1
License:	GPL
Group:		Video
Url:		http://smplayer.sourceforge.net/
Source0:	http://smplayer.sourceforge.net/download/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs-devel	>= 3.5.7
Requires:	mplayer		>= 1.0-1.rc1
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

* Configurable subtitles. You can choose font and size, and even colors 
  for the subtitles.
* Audio track switching. You can choose the audio track you want to listen. 
  Works with avi and mkv. And of course with DVDs.
* Seeking by mouse wheel. You can use your mouse wheel to go forward or 
  backward in the video.
* Video equalizer, allows you to adjust the brightness, contrast, hue, 
  saturation and gamma of the video image.
* Multiple speed playback. You can play at 2X, 4X... and even in slow motion.
* Filters. Several filters are available: deinterlace, postprocessing, denoise... 
  and even a karaoke filter (voice removal).
* Audio and subtitles delay adjustment. Allows you to sync audio and subtitles.
* Advanced options, such as selecting a demuxer or video & audio codecs.
* Playlist. Allows you to enqueue several files to be played one after each other.
  Autorepeat and shuffle supported too.
* Preferences dialog. You can easily configure every option of SMPlayer by using 
  a nice preferences dialog.

SMPlayer supports themes which can be found in smplayer-themes package.

%prep
%setup -q

%build

%make PREFIX=%{_prefix} KDE_SUPPORT=1

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std PREFIX=%{_prefix}

desktop-file-install --vendor="" \
	--add-category="X-MandrivaLinux-Multimedia-Video" \
	--add-only-show-in="KDE" \
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
%doc %{_datadir}/doc/packages/smplayer/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/shortcuts
%dir %{_datadir}/%{name}/translations
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/*.conf
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/shortcuts/*
%lang(bg) %{_datadir}/%{name}/translations/smplayer_bg.qm
%lang(cs) %{_datadir}/%{name}/translations/smplayer_cs.qm
%lang(de) %{_datadir}/%{name}/translations/smplayer_de.qm
%lang(en_US) %{_datadir}/%{name}/translations/smplayer_en_US.qm
%lang(es) %{_datadir}/%{name}/translations/smplayer_es.qm
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
%lang(sr) %{_datadir}/%{name}/translations/smplayer_sr.qm
%lang(sv) %{_datadir}/%{name}/translations/smplayer_sv.qm
%lang(tr) %{_datadir}/%{name}/translations/smplayer_tr.qm
%lang(uk_UA) %{_datadir}/%{name}/translations/smplayer_uk_UA.qm
%lang(zh_CN) %{_datadir}/%{name}/translations/smplayer_zh_CN.qm
