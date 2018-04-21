# Script generated with Bloom
pkgdesc="ROS - lpg_planner: LPGL Planner (http://zeus.ing.unibs.it/lpg/)"
url='http://ros.org/wiki/downward'

pkgname='ros-kinetic-lpg-planner'
pkgver='2.1.7_1'
pkgrel=1
arch=('any')
license=('GPL'
)

makedepends=('ros-kinetic-catkin'
)

depends=()

conflicts=()
replaces=()

_dir=lpg_planner
source=()
md5sums=()

prepare() {
    cp -R $startdir/lpg_planner $srcdir/lpg_planner
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

