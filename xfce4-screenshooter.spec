%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Screen capture tool for Xfce
Name:		xfce4-screenshooter
Version:	1.8.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/xfce4-screenshooter
Source0:	http://archive.xfce.org/src/apps/xfce4-screenshooter/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	libcurl-devel
BuildRequires:	libsoup-devel
Obsoletes:	xfce-screenshooter-plugin
Obsoletes:	xfce4-screenshooter-plugin < 1.4.90.0
Provides:	xfce4-screenshooter-plugin
Requires:	xfce4-panel >= 4.4.2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This application allows you to capture the entire screen, 
the active window or a selected region. You can set the delay 
that elapses before the screenshot is taken and the action that 
will be done with the screenshot: save it to a PNG file, copy 
it to the clipboard, or open it using another application.
 
A plugin for the Xfce panel is also available.
 
%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/*
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/*.desktop
%{_datadir}/applications/xfce4-screenshooter.desktop
%{_iconsdir}/hicolor/*/apps/*.*g
%{_mandir}/man1/*
%{_datadir}/xfce4/doc/*/images/*.png
%{_datadir}/xfce4/doc/*/*.html
