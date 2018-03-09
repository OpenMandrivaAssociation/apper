Name:		apper
Summary:	KDE PackageKit Interface
Group:		System/Configuration/Packaging
Version:	1.0.0
Release:	1
License:	GPLv2+
URL:		http://www.opendesktop.org/content/show.php/Apper?content=84745
Source0:	http://download.kde.org/stable/apper/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	desktop-file-utils
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KDED)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(LibKWorkspace)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5XmlPatterns)

Requires:	packagekit >= 0.6.17
Provides:	packagekit-gui = %{version}-%{release}
%rename		kpackagekit
%rename		kpackagekit-common

%description
KDE interface for PackageKit.

%files -f %{name}.lang
%{_datadir}/dbus-1/services/*.service
%{_kde5_bindir}/apper
%{_qt5_plugindir}/kded_apperd.so
%{_kde5_libdir}/apper/libapper_private.so
%{_kde5_datadir}/apperd/
%{_kde5_datadir}/apper
%{_kde5_libdir}/libexec/apper-pk-session
%{_kde5_datadir}/applications/org.kde.apper*.desktop
%{_kde5_datadir}/metainfo/org.kde.apper.appdata.xml
%{_kde5_services}/kded/apperd.desktop
%{_mandir}/man1/apper.1.*
#--------------------------------------------------------------------
%prep
%setup -q
%apply_patches

%build
%cmake_kde5 -DAUTOREMOVE:BOOL=OFF -DCMAKE_SKIP_RPATH:BOOL=OFF
%ninja

%install
%ninja_install -C build

desktop-file-install --vendor='' \
	--dir %{buildroot}%{_datadir}/applications \
	--remove-category='System' \
	--add-category='Settings' \
	--remove-mime-type='application/x-deb' \
	%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name} --all-name --with-man

%check
for file in org.kde.apper org.kde.apper_installer; do
  desktop-file-validate %{buildroot}%{_datadir}/applications/$file.desktop
done

