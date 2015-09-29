Name:           ros-hydro-downward
Version:        2.0.9
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
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-roslib
BuildRequires:  ros-hydro-rospack

%description
fast downward: PDDL Planner (http://www.fast-downward.org)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Sep 29 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.9-0
- Autogenerated by Bloom

* Wed Sep 16 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.8-0
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

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-14
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-13
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-12
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-11
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-10
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-9
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-8
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-7
- Autogenerated by Bloom

* Sun Aug 02 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-6
- Autogenerated by Bloom

* Sat Aug 01 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-5
- Autogenerated by Bloom

* Sat Aug 01 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-4
- Autogenerated by Bloom

* Sat Aug 01 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-3
- Autogenerated by Bloom

* Sat Aug 01 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-2
- Autogenerated by Bloom

* Sat Aug 01 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-1
- Autogenerated by Bloom

* Sat Aug 01 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.3-0
- Autogenerated by Bloom

* Mon Jun 29 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.2-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 2.0.0-0
- Autogenerated by Bloom

