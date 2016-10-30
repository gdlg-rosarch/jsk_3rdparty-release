Name:           ros-kinetic-rosping
Version:        2.0.18
Release:        1%{?dist}
Summary:        ROS rosping package

Group:          Development/Libraries
License:        Boost Software License, Version 1.0
URL:            http://ros.org/wiki/rosping
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-mk
BuildRequires:  ros-kinetic-rosboost-cfg
BuildRequires:  ros-kinetic-rosbuild
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-std-msgs

%description
rosping is the tool to send ICMP ECHO_REQUEST to network hosts where roscore is
running, and send back to you as rostopic message. For echoing ROS node, use
rosnode.

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
* Sun Oct 30 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.18-1
- Autogenerated by Bloom

* Sat Oct 29 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.18-0
- Autogenerated by Bloom

