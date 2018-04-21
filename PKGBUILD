# Script generated with Bloom
pkgdesc="ROS - opt_camera"
url='http://ros.org/wiki/opt_camera'

pkgname='ros-kinetic-opt-camera'
pkgver='2.1.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-camera-calibration-parsers'
'ros-kinetic-catkin'
'ros-kinetic-compressed-image-transport'
'ros-kinetic-cv-bridge'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-image-proc'
'ros-kinetic-roslang'
'ros-kinetic-rospack'
'ros-kinetic-sensor-msgs'
)

depends=('ros-kinetic-camera-calibration-parsers'
'ros-kinetic-compressed-image-transport'
'ros-kinetic-cv-bridge'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-image-proc'
'ros-kinetic-rospack'
'ros-kinetic-sensor-msgs'
)

conflicts=()
replaces=()

_dir=opt_camera
source=()
md5sums=()

prepare() {
    cp -R $startdir/opt_camera $srcdir/opt_camera
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

