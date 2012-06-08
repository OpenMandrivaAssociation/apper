%define git 0
# use a fix date
%define gitdate 20111129

Name:		apper
Summary:	KDE PackageKit Interface
Group:		System/Configuration/Packaging
Version:	0.7.2
%if %git
Release:	0.git%{gitdate}.1
%else
Release:	1
%endif
License:	GPLv2+
URL:		http://www.opendesktop.org/content/show.php/Apper?content=84745
Source0:	http://download.kde.org/stable/apper/%version/src/%name-%version.tar.bz2
BuildRequires:	chrpath
BuildRequires:	desktop-file-utils
BuildRequires:	kdelibs4-devel
BuildRequires:	qt4-qtdbus
BuildRequires:	pkgconfig(packagekit-glib2) >= 0.6.17
BuildRequires:	pkgconfig(polkit)
Requires:	packagekit >= 0.6.17
Provides:	packagekit-gui = %{version}-%{release}
%rename		kpackagekit
%rename		kpackagekit-common

%description
KDE interface for PackageKit.

%files -f %name.lang
%{_datadir}/dbus-1/services/*.service
%{_kde_bindir}/apper
%{_kde_libdir}/kde4/*apper*.so
%{_kde_libdir}/apper/libapper.so
%{_kde_appsdir}/?pper*/
%{_kde_libdir}/kde4/libexec/apper-sentinel
%{_kde_applicationsdir}/apper*.desktop
%{_kde_services}/kcm_apper.desktop
%{_kde_services}/kded/apperd.desktop
%{_kde_mandir}/man1/apper.1.*

#--------------------------------------------------------------------
%prep
%if %git
%setup -q -n %name
%else
%setup -q
%endif

%build
%cmake_kde4 -DAUTOREMOVE:BOOL=OFF -DCMAKE_SKIP_RPATH:BOOL=OFF
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

chrpath --list %{buildroot}%{_kde_bindir}/apper
chrpath --replace %{_kde_libdir}/apper %{buildroot}%{_kde_bindir}/apper

%find_lang %name || touch %name.lang

%check
for file in apper apper_installer; do
  desktop-file-validate %{buildroot}%{_kde_datadir}/applications/kde4/$file.desktop
done
