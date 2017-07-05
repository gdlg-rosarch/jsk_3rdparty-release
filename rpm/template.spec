Name:           ros-kinetic-slic
Version:        2.1.1
Release:        0%{?dist}
Summary:        ROS slic package

Group:          Development/Libraries
License:        N/A
Source0:        %{name}-%{version}.tar.gz

Requires:       opencv-devel
BuildRequires:  ca-certificates
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  opencv-devel
BuildRequires:  openssl
BuildRequires:  ros-kinetic-cmake-modules

%description
SLIC-Superpizel ROS Wrapper This file contains the class elements of the class
Slic. This class is an implementation of the SLIC Superpixel algorithm by
Achanta et al. [PAMI'12, vol. 34, num. 11, pp. 2274-2282]. This implementation
is created for the specific purpose of creating over-segmentations in an OpenCV-
based environment.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Jul 05 2017 Kei Okada <k-okada@jsk.imi.i.u-tokyo.ac.jp> - 2.1.1-0
- Autogenerated by Bloom

* Sun Jul 02 2017 Kei Okada <k-okada@jsk.imi.i.u-tokyo.ac.jp> - 2.1.0-0
- Autogenerated by Bloom

* Tue May 09 2017 Kei Okada <k-okada@jsk.imi.i.u-tokyo.ac.jp> - 2.0.20-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Kei Okada <k-okada@jsk.imi.i.u-tokyo.ac.jp> - 2.0.19-0
- Autogenerated by Bloom

* Sun Oct 30 2016 Kei Okada <k-okada@jsk.imi.i.u-tokyo.ac.jp> - 2.0.18-1
- Autogenerated by Bloom

* Sat Oct 29 2016 Kei Okada <k-okada@jsk.imi.i.u-tokyo.ac.jp> - 2.0.18-0
- Autogenerated by Bloom

