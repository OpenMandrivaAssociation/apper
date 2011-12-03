%define git 1
# use a fix date
%define gitdate 20111111

Name:		apper
Summary:	KDE interface for PackageKit
Group:		System/Configuration/Packaging
Version:	0.7.1
Release:	0.git%{gitdate}.2
License:	GPLv2+
URL:		http://www.opendesktop.org/content/show.php/Apper?content=84745
Source0: 	http://dl.dropbox.com/u/37314029/%{name}%{!?git:-%{version}}.tar.%{?git:xz}%{!?git:bz2}
BuildRequires:	desktop-file-utils
BuildRequires:	kdelibs4-devel
BuildRequires:	qt4-qtdbus
BuildRequires:	packagekit-devel >= 0.6.17
BuildRequires:	polkit-devel
Obsoletes:	kpackagekit < 0.7.0
Provides:	kpackagekit = %{version}-%{release}
Requires:	packagekit >= 0.6.17
Provides:	packagekit-gui
Obsoletes:	kpackagekit
Obsoletes:	kpackagekit-common

%description
KDE interface for PackageKit.

%files -f %name.lang
%{_datadir}/dbus-1/services/*.service
%{_kde_bindir}/apper
%{_kde_libdir}/kde4/*apper*.so
%{_kde_libdir}/apper/libapper.so
%{_kde_appsdir}/?pper*/
%{_kde_libdir}/kde4/libexec/apper-sentinel
%{_kde_datadir}/applications/kde4/apper*.desktop
%{_kde_services}/kcm_apper.desktop
%{_kde_services}/kded/apperd.desktop
%{_kde_mandir}/man1/apper.1.*

#--------------------------------------------------------------------
%prep
%setup -q%{?git:n %{name}}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build
%find_lang %{name}

# hack around gnome-packagekit conflict
mv %{buildroot}%{_datadir}/dbus-1/services/org.freedesktop.PackageKit.service \
%{buildroot}%{_datadir}/dbus-1/services/kde-org.freedesktop.PackageKit.service 

%check
pushd %{buildroot}%{_kde_datadir}/applications/kde4/
for file in apper apper_installer; do
desktop-file-validate $file.desktop
done
popd

