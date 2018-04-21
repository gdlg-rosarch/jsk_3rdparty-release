# Script generated with Bloom
pkgdesc="ROS - laser_filters_jsk_patch"
url='http://ros.org/wiki/laser_filters_jsk_patch'

pkgname='ros-kinetic-laser-filters-jsk-patch'
pkgver='2.1.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('git'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-filters'
'ros-kinetic-laser-filters'
'ros-kinetic-laser-geometry'
'ros-kinetic-mk'
)

depends=('ros-kinetic-filters'
'ros-kinetic-laser-filters'
)

conflicts=()
replaces=()

_dir=laser_filters_jsk_patch
source=()
md5sums=()

prepare() {
    cp -R $startdir/laser_filters_jsk_patch $srcdir/laser_filters_jsk_patch
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

