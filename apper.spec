Name:		apper
Summary:	KDE PackageKit Interface
Group:		System/Configuration/Packaging
Version:	0.8.0
Release:	1
License:	GPLv2+
URL:		http://www.opendesktop.org/content/show.php/Apper?content=84745
Source0:	http://download.kde.org/stable/apper/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	desktop-file-utils
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	qt4-qtdbus
BuildRequires:	packagekit-qt-devel >= 0.8.5
Requires:	packagekit >= 0.6.17
Provides:	packagekit-gui = %{version}-%{release}
%rename		kpackagekit
%rename		kpackagekit-common

%description
KDE interface for PackageKit.

%files -f %{name}.lang
%{_datadir}/dbus-1/services/*.service
%{_kde_bindir}/apper
%{_kde_libdir}/kde4/*apper*.so
%{_kde_libdir}/kde4/plasma_applet_updater.so
%{_kde_libdir}/apper/libapper.so
%{_kde_appsdir}/?pper*/
%{_kde_datadir}/apps/plasma/packages
%{_kde_libdir}/kde4/libexec/apper-pk-session
%{_kde_applicationsdir}/apper*.desktop
%{_kde_services}/kcm_apper.desktop
%{_kde_services}/kded/apperd.desktop
%{_kde_services}/plasma-applet-updater.desktop
%{_kde_mandir}/man1/apper.1.*

#--------------------------------------------------------------------
%prep
%setup -q

%build
%cmake_kde4 -DAUTOREMOVE:BOOL=OFF -DCMAKE_SKIP_RPATH:BOOL=OFF
%make

%install
%makeinstall_std -C build

desktop-file-install --vendor='' \
	--dir %{buildroot}%{_kde_datadir}/applications/kde4 \
	--remove-category='System' \
	--add-category='Settings' \
	--remove-mime-type='application/x-deb' \
	%{buildroot}%{_kde_datadir}/applications/kde4/*.desktop

%find_lang %{name} --all-name

%check
for file in apper apper_installer; do
  desktop-file-validate %{buildroot}%{_kde_datadir}/applications/kde4/$file.desktop
done


%changelog
* Sat Jun 09 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.7.2-1
+ Revision: 803684
- Update to 0.7.2
- Build in current environment

* Sat Dec 31 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.7.1-0.git20111129.1
+ Revision: 748340
- Fix apper to be able to run (thanks to zemo)
- Add rename for a smooth upgrade

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove use of  find_lang
    - Fix BuildRequires
    - Rebuild against new kde

* Fri Nov 11 2011 Zé <ze@mandriva.org> 0.7.1-0.git20111111.1
+ Revision: 729947
- fix checks
- use a fix date
- the new KPackageKit generation
- check all .desktop files
- imported package apper


* Thu Nov 10 2011 Zé <ze@mandriva.org> 0.7.1-0.git20111110.1
- first package (from git source SHA a7c4c7e7154da16719a3a41fa34fa374d2336367)
