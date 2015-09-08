Name:           ros-jade-downward
Version:        2.0.6
Release:        0%{?dist}
Summary:        ROS downward package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/downward
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  glibc-static
BuildRequires:  libstdc++-devel
BuildRequires:  libstdc++-static
BuildRequires:  mercurial
BuildRequires:  python-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-mk
BuildRequires:  ros-jade-roslib
BuildRequires:  ros-jade-rospack

%description
fast downward: PDDL Planner (http://www.fast-downward.org)

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

* Mon Jun 22 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.1-1
- Autogenerated by Bloom

* Sun Jun 21 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

