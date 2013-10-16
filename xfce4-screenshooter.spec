%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	Screen capture tool for Xfce
Name:		xfce4-screenshooter
Version:	1.8.1
Release:	4
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/xfce4-screenshooter
Source0:	http://archive.xfce.org/src/apps/xfce4-screenshooter/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		xfce4-screenshooter-1.8.0-fix-linkage.patch
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	libxfce4ui-devel >= 4.9.1
BuildRequires:	exo-devel >= 0.7.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	libcurl-devel
BuildRequires:	libsoup-devel
Obsoletes:	xfce-screenshooter-plugin
Obsoletes:	xfce4-screenshooter-plugin < 1.4.90.0
Provides:	xfce4-screenshooter-plugin
Requires:	xfce4-panel >= 4.9.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This application allows you to capture the entire screen,
the active window or a selected region. You can set the delay
that elapses before the screenshot is taken and the action that
will be done with the screenshot: save it to a PNG file, copy
it to the clipboard, or open it using another application.

%prep
%setup -q
%patch0 -p1

%build
# (tpg) for new automake
sed -i -e 's,AM_CONFIG_HEADER,AC_CONFIG_HEADERS,g' configure.*

# (tpg) needed for patch 0
NOCONFIGURE=1 xdt-autogen

%configure2_5x \
	--disable-static \
	--enable-xfixes

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README
%{_bindir}/*
%{_libdir}/xfce4/panel/plugins/*
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/applications/xfce4-screenshooter.desktop
%{_iconsdir}/hicolor/*/apps/*.*g
%{_mandir}/man1/*
%{_datadir}/xfce4/doc/*/images/*.png
%{_datadir}/xfce4/doc/*/*.html


%changelog
* Tue Aug 21 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.1-1
+ Revision: 815560
- fix file list
- update to new version 1.8.1

* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 1.8.0-3
+ Revision: 791571
- Rebuild

* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.0-2
+ Revision: 789814
- Patch0: add missing linking
- rebuild
- drop old stuff from spec file

* Mon Aug 15 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.0-1
+ Revision: 694600
- add buildrequires on exo-devel
- add buildrequires on libxfce4ui-devel
- update to new version 1.8.0

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.9-3
+ Revision: 633055
- rebuild for new Xfce 4.8.0

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.9-2mdv2011.0
+ Revision: 579672
- rebuild for new xfce 4.7.0

* Tue Feb 09 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.9-1mdv2011.0
+ Revision: 503431
- update to new version 1.7.9

* Sun Jun 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.0-1mdv2010.0
+ Revision: 385920
- update to new version 1.6.0
- add buildrequires on libcurl-devel and libxmlrpc-c-devel to enable ZimageZ support

* Wed Feb 25 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5.1-1mdv2009.1
+ Revision: 344753
- update to new version 1.5.1

* Sun Jan 18 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5.0-1mdv2009.1
+ Revision: 331021
- fix file list
- update to new version 1.5.0

* Fri Jan 02 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.90.0-1mdv2009.1
+ Revision: 323345
- update to new version 1.4.90.0
- add provides/obsoletes on old name
- upstream has changed name

* Sun Nov 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.0-1mdv2009.1
+ Revision: 303602
- update to new version 1.4.0

* Fri Nov 14 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.9.3-1mdv2009.1
+ Revision: 303339
- update to new version 1.3.9.3

* Thu Nov 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.9.2-1mdv2009.1
+ Revision: 302802
- update to new version 1.3.9.2

* Tue Nov 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.9.1-1mdv2009.1
+ Revision: 302305
- update to new version 1.3.9.1

* Wed Nov 05 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.9.0-1mdv2009.1
+ Revision: 300085
- fix file list
- update to new version 1.3.9.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.2-2mdv2009.1
+ Revision: 295007
- rebuild for new Xfce4.6 beta1

* Mon Aug 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.2-1mdv2009.0
+ Revision: 275612
- update to new version 1.3.2

* Fri Jul 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.1-1mdv2009.0
+ Revision: 237849
- update to new version 1.3.1

* Sun Jun 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.0-1mdv2009.0
+ Revision: 230090
- fix file list
- update to new version 1.2.0
- update url and description
- update to new version 1.1.0
- drop both patches
- fix file list

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-2mdv2009.0
+ Revision: 194676
- Patch0: fix filename generation
- Patch1: do not save file when cancel button has been pressed
- fix file list

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-1mdv2008.1
+ Revision: 110131
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING and INSTALL files
- use upstream name

* Thu May 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.0-5mdv2008.0
+ Revision: 33254
- spec file clean

