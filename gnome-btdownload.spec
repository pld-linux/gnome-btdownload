Summary:	Gnome BitTorrent Downloader
Name:		gnome-btdownload
Version:	0.0.20
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnome-bt/%{name}-%{version}.tar.gz
# Source0-md5:	dd7ad29c9c5689dc73a736d44dde2bef
URL:		http://gnome-bt.sourceforge.net/
BuildRequires:	python-pygtk-devel >= 1.99
BuildRequires:  python-gnome-devel
Requires(post):	GConf2
%pyrequires_eq	python
Requires:	BitTorrent
Requires:	python-gnome-gconf
Requires:	python-gnome-applet
Requires:	python-gnome-ui
Requires:	python-pygtk-gtk >= 1.99
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A work-in-progress Gnome "mime-sink" for BitTorrent files. It's not meant to be an entire front-end, just a program that pops up when you "execute" the torrent files

%prep
%setup -q

%build
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/mime-info/*


%clean
rm -rf $RPM_BUILD_ROOT
