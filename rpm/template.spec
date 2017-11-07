Name:           ros-lunar-find-object-2d
Version:        0.6.2
Release:        0%{?dist}
Summary:        ROS find_object_2d package

Group:          Development/Libraries
License:        BSD
URL:            http://find-object.googlecode.com
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-cv-bridge
Requires:       ros-lunar-image-transport
Requires:       ros-lunar-message-filters
Requires:       ros-lunar-qt-gui-cpp
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-rospy
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-std-srvs
Requires:       ros-lunar-tf
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cv-bridge
BuildRequires:  ros-lunar-genmsg
BuildRequires:  ros-lunar-image-transport
BuildRequires:  ros-lunar-message-filters
BuildRequires:  ros-lunar-qt-gui-cpp
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rospy
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-std-srvs
BuildRequires:  ros-lunar-tf

%description
The find_object_2d package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Tue Nov 07 2017 Mathieu Labbe <matlabbe@gmail.com> - 0.6.2-0
- Autogenerated by Bloom

