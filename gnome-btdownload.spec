Summary:	GNOME BitTorrent Downloader
Summary(pl):	Narz�dzie do �ci�gania protoko�em BitTorrent dla GNOME
Name:		gnome-btdownload
Version:	0.0.20
Release:	2
License:	BSD
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnome-bt/%{name}-%{version}.tar.gz
# Source0-md5:	dd7ad29c9c5689dc73a736d44dde2bef
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

%description -l pl
Jest to nadal tworzony "mime-sink" GNOME dla plik�w BitTorrent. Nie ma
by� ca�ym frontendem, a tylko programem wyskakuj�cym przy
"wykonywaniu" plik�w torrent.

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
