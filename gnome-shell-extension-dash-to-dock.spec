Name:           gnome-shell-extension-dash-to-dock
Version:        95
Release:        1
Summary:        Dock for the Gnome Shell by micxgx@gmail.com
Group:          Graphical desktop/GNOME
License:        GPLv2+
URL:            https://micheleg.github.io/dash-to-dock
Source0:        https://github.com/micheleg/dash-to-dock/archive/extensions.gnome.org-v%{version}/dash-to-dock-extensions.gnome.org-v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  sassc
BuildRequires:  pkgconfig(glib-2.0)

Requires:       gnome-shell-extensions-common

%description
This extension enhances the dash moving it out of the overview and
transforming it in a dock for an easier launching of applications
and a faster switching between windows and desktops without having
to leave the desktop view.

%prep
%autosetup -n dash-to-dock-extensions.gnome.org-v%{version} -p 1

%build
%make_build

%install
%make_install

# Remove not needed
rm -fr %{buildroot}%{_datadir}/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com/{COPYING*,README*,locale,schemas}

%find_lang %{name} --all-name

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_datadir}/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com/
%{_datadir}/glib-2.0/schemas/*gschema.xml
