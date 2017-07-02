Name:           ros-jade-collada-urdf-jsk-patch
Version:        2.1.0
Release:        0%{?dist}
Summary:        ROS collada_urdf_jsk_patch package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/collada_urdf_jsk_patch
Source0:        %{name}-%{version}.tar.gz

Requires:       collada-dom-devel
Requires:       gts
Requires:       python-catkin_tools
Requires:       ros-jade-angles
Requires:       ros-jade-assimp-devel
Requires:       ros-jade-class-loader
Requires:       ros-jade-collada-parser
Requires:       ros-jade-collada-urdf
Requires:       ros-jade-geometric-shapes
Requires:       ros-jade-kdl-parser
Requires:       ros-jade-pluginlib
Requires:       ros-jade-resource-retriever
Requires:       ros-jade-roscpp
Requires:       ros-jade-tf
Requires:       ros-jade-urdf
BuildRequires:  collada-dom-devel
BuildRequires:  git
BuildRequires:  gts
BuildRequires:  python-catkin_tools
BuildRequires:  ros-jade-angles
BuildRequires:  ros-jade-assimp-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-class-loader
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-collada-parser
BuildRequires:  ros-jade-collada-urdf
BuildRequires:  ros-jade-geometric-shapes
BuildRequires:  ros-jade-kdl-parser
BuildRequires:  ros-jade-mk
BuildRequires:  ros-jade-pluginlib
BuildRequires:  ros-jade-resource-retriever
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-tf

%description
unaccepted patch for collada_urdf

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun Jul 02 2017 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.1.0-0
- Autogenerated by Bloom

* Tue May 09 2017 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.20-0
- Autogenerated by Bloom

* Thu Feb 23 2017 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.19-0
- Autogenerated by Bloom

* Sat Oct 22 2016 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.17-0
- Autogenerated by Bloom

* Mon Oct 17 2016 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.16-0
- Autogenerated by Bloom

* Sun Mar 20 2016 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.14-0
- Autogenerated by Bloom

* Wed Dec 16 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.13-0
- Autogenerated by Bloom

* Thu Nov 26 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.12-1
- Autogenerated by Bloom

* Tue Oct 13 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.11-0
- Autogenerated by Bloom

* Wed Oct 07 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.10-0
- Autogenerated by Bloom

* Tue Sep 29 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.9-0
- Autogenerated by Bloom

* Tue Sep 15 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.7-0
- Autogenerated by Bloom

* Tue Sep 08 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.6-0
- Autogenerated by Bloom

* Mon Aug 24 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.5-0
- Autogenerated by Bloom

* Wed Aug 19 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.4-1
- Autogenerated by Bloom

* Tue Aug 18 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.4-0
- Autogenerated by Bloom

* Mon Aug 03 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Mon Jun 29 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

