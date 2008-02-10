Summary:	GNOME BitTorrent downloader
Summary(pl.UTF-8):	Narzędzie do ściągania protokołem BitTorrent dla GNOME
Name:		gnome-btdownload
Version:	0.0.32
Release:	0.2
License:	BSD
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnome-bt/%{name}-%{version}.tar.gz
# Source0-md5:	893268ec4ff1d64439e8c5cfbc6db0c7
Patch0:		%{name}-desktop.patch
URL:		http://gnome-bt.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python-gnome-devel >= 2.10.0
BuildRequires:	python-pygtk-devel >= 1:2.6.0
BuildRequires:	rpmbuild(macros) >= 1.197
%pyrequires_eq	python
Requires:	BitTorrent >= 3.3
#Requires:	python-gnome-extras-applet >= 2.10.0
Requires:	python-gnome-gconf >= 2.10.0
Requires:	python-gnome-ui >= 2.10.0
Requires:	python-pygtk-gtk >= 1:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A work-in-progress GNOME "mime-sink" for BitTorrent files. It's not
meant to be an entire front-end, just a program that pops up when you
"execute" the torrent files.

%description -l pl.UTF-8
Jest to nadal tworzony "mime-sink" GNOME dla plików BitTorrent. Nie ma
być całym frontendem, a tylko programem wyskakującym przy
"wykonywaniu" plików torrent.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/{application-registry,mime-info}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%post
%gconf_schema_install gnome-btdownload.schemas
%update_desktop_database_post

%preun
%gconf_schema_uninstall gnome-btdownload.schemas

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/gconf/schemas/gnome-btdownload.schemas
%{py_sitescriptdir}/gnomebtdownload
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
