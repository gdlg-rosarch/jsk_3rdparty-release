# Script generated with Bloom
pkgdesc="ROS - SLIC-Superpizel ROS Wrapper This file contains the class elements of the class Slic. This class is an implementation of the SLIC Superpixel algorithm by Achanta et al. [PAMI'12, vol. 34, num. 11, pp. 2274-2282]. This implementation is created for the specific purpose of creating over-segmentations in an OpenCV-based environment."


pkgname='ros-kinetic-slic'
pkgver='2.1.7_1'
pkgrel=1
arch=('any')
license=('N/A'
)

makedepends=('ca-certificates'
'cmake'
'git'
'opencv'
'openssl'
'ros-kinetic-cmake-modules'
)

depends=('opencv'
)

conflicts=()
replaces=()

_dir=slic
source=()
md5sums=()

prepare() {
    cp -R $startdir/slic $srcdir/slic
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

