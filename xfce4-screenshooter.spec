%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_rebuild_configure 1

Summary:	Screen capture tool for Xfce
Name:		xfce4-screenshooter
Version:	1.11.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/applications/xfce4-screenshooter
Source0:	https://archive.xfce.org/src/apps/xfce4-screenshooter/%{url_ver}/%{name}-%{version}.tar.bz2
Source1:	%{name}.rpmlintrc
BuildRequires:	meson
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2) 
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	perl(XML::Parser)
BuildRequires:	curl-devel
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(wayland-protocols)
%rename		xfce-screenshooter-plugin
%rename		xfce4-screenshooter-plugin
Requires:	xfce4-panel >= 4.9.0

%description
This application allows you to capture the entire screen,
the active window or a selected region. You can set the delay
that elapses before the screenshot is taken and the action that
will be done with the screenshot: save it to a PNG file, copy
it to the clipboard, or open it using another application.

%prep
%autosetup -p1

%build
%meson \
		-Dxfixes=enabled \
		-Dx11=enabled \
		-Dwayland=enabled

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README*
%{_bindir}/*
%{_libdir}/xfce4/panel/plugins/*
%{_libexecdir}/xfce4/screenshooter/scripts/imgur-upload.sh
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/applications/xfce4-screenshooter.desktop
%{_iconsdir}/hicolor/*/apps/*.*g
%{_mandir}/man1/*
%{_datadir}/metainfo/xfce4-screenshooter.appdata.xml 
