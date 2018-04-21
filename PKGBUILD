# Script generated with Bloom
pkgdesc="ROS - The bayesian_belief_networks package form https://github.com/eBay/bayesian-belief-networks, Authored by Neville Newey, Anzar Afaq, Copyright 2013 eBay Software Foundation"
url='https://github.com/eBay/bayesian-belief-networks'

pkgname='ros-kinetic-bayesian-belief-networks'
pkgver='2.1.7_1'
pkgrel=1
arch=('any')
license=('Apache License, Version 2.0'
)

makedepends=('git'
'ros-kinetic-catkin'
'ros-kinetic-message-generation'
'ros-kinetic-mk'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
)

depends=('ros-kinetic-message-runtime'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
)

conflicts=()
replaces=()

_dir=bayesian_belief_networks
source=()
md5sums=()

prepare() {
    cp -R $startdir/bayesian_belief_networks $srcdir/bayesian_belief_networks
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

