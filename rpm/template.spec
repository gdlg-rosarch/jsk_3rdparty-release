Name:           ros-indigo-jsk-3rdparty
Version:        2.0.3
Release:        0%{?dist}
Summary:        ROS jsk_3rdparty package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_3rdparty
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-assimp-devel
Requires:       ros-indigo-bayesian-belief-networks
Requires:       ros-indigo-downward
Requires:       ros-indigo-ff
Requires:       ros-indigo-ffha
Requires:       ros-indigo-julius
Requires:       ros-indigo-libsiftfast
Requires:       ros-indigo-mini-maxwell
Requires:       ros-indigo-nlopt
Requires:       ros-indigo-opt-camera
Requires:       ros-indigo-rospatlite
Requires:       ros-indigo-rosping
Requires:       ros-indigo-rostwitter
Requires:       ros-indigo-sklearn
Requires:       ros-indigo-voice-text
BuildRequires:  ros-indigo-catkin

%description
Metapackage that contains commonly used 3rdparty toolset for jsk-ros-pkg

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Aug 02 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Mon Jun 29 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

