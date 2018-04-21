# Script generated with Bloom
pkgdesc="ROS - <p>Metapackage that contains commonly used 3rdparty toolset for jsk-ros-pkg</p>"
url='http://ros.org/wiki/jsk_3rdparty'

pkgname='ros-kinetic-jsk-3rdparty'
pkgver='2.1.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-assimp-devel'
'ros-kinetic-bayesian-belief-networks'
'ros-kinetic-downward'
'ros-kinetic-ff'
'ros-kinetic-ffha'
'ros-kinetic-julius'
'ros-kinetic-julius-ros'
'ros-kinetic-libcmt'
'ros-kinetic-libsiftfast'
'ros-kinetic-mini-maxwell'
'ros-kinetic-nlopt'
'ros-kinetic-opt-camera'
'ros-kinetic-pgm-learner'
'ros-kinetic-rospatlite'
'ros-kinetic-rosping'
'ros-kinetic-slic'
'ros-kinetic-voice-text'
)

conflicts=()
replaces=()

_dir=jsk_3rdparty
source=()
md5sums=()

prepare() {
    cp -R $startdir/jsk_3rdparty $srcdir/jsk_3rdparty
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

