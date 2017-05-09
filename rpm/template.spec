Name:           ros-jade-pgm-learner
Version:        2.0.20
Release:        0%{?dist}
Summary:        ROS pgm_learner package

Group:          Development/Libraries
License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-message-runtime
Requires:       ros-jade-rospy
Requires:       scipy
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-rospy
BuildRequires:  ros-jade-rostest
BuildRequires:  scipy

%description
Parameter/Structure Estimation and Inference for Bayesian Belief Network

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
* Tue May 09 2017 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.0.20-0
- Autogenerated by Bloom

* Thu Feb 23 2017 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.0.19-0
- Autogenerated by Bloom

* Sat Oct 22 2016 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.0.17-0
- Autogenerated by Bloom

* Mon Oct 17 2016 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.0.16-0
- Autogenerated by Bloom

* Sun Mar 20 2016 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.0.14-0
- Autogenerated by Bloom

* Wed Dec 16 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.0.13-0
- Autogenerated by Bloom

* Thu Nov 26 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 2.0.12-1
- Autogenerated by Bloom

