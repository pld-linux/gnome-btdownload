Summary:	GNOME BitTorrent downloader
Summary(pl.UTF-8):	Narzędzie do ściągania protokołem BitTorrent dla GNOME
Name:		gnome-btdownload
Version:	0.0.22
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnome-bt/%{name}-%{version}.tar.gz
# Source0-md5:	b52df0c8b0c28aa0cc8814ff4754cef9
Patch0:		%{name}-desktop.patch
URL:		http://gnome-bt.sourceforge.net/
BuildRequires:	python-gnome-devel >= 2.10.0
BuildRequires:	python-pygtk-devel >= 1:2.6.0
BuildRequires:	rpmbuild(macros) >= 1.197
%pyrequires_eq	python
Requires:	BitTorrent >= 3.3
Requires:	python-gnome-extras-applet >= 2.10.0
Requires:	python-gnome-gconf >= 2.10.0
Requires:	python-gnome-ui >= 2.10.0
Requires:	python-pygtk-gtk >= 1:2.6.0
BuildArch:	noarch
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
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
