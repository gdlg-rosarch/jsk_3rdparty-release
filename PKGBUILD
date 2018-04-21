# Script generated with Bloom
pkgdesc="ROS - unaccepted patch for collada_urdf"
url='http://ros.org/wiki/collada_urdf_jsk_patch'

pkgname='ros-kinetic-collada-urdf-jsk-patch'
pkgver='2.1.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('collada-dom'
'git'
'gts'
'python2-catkin-tools'
'ros-kinetic-angles'
'ros-kinetic-assimp-devel'
'ros-kinetic-catkin'
'ros-kinetic-class-loader'
'ros-kinetic-cmake-modules'
'ros-kinetic-collada-parser'
'ros-kinetic-collada-urdf'
'ros-kinetic-geometric-shapes'
'ros-kinetic-kdl-parser'
'ros-kinetic-mk'
'ros-kinetic-pluginlib'
'ros-kinetic-resource-retriever'
'ros-kinetic-roscpp'
'ros-kinetic-rostest'
'ros-kinetic-tf'
)

depends=('collada-dom'
'gts'
'python2-catkin-tools'
'ros-kinetic-angles'
'ros-kinetic-assimp-devel'
'ros-kinetic-class-loader'
'ros-kinetic-collada-parser'
'ros-kinetic-collada-urdf'
'ros-kinetic-geometric-shapes'
'ros-kinetic-kdl-parser'
'ros-kinetic-pluginlib'
'ros-kinetic-resource-retriever'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
'ros-kinetic-urdf'
)

conflicts=()
replaces=()

_dir=collada_urdf_jsk_patch
source=()
md5sums=()

prepare() {
    cp -R $startdir/collada_urdf_jsk_patch $srcdir/collada_urdf_jsk_patch
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

