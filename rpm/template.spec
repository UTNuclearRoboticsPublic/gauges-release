Name:           ros-indigo-gauges
Version:        1.0.4
Release:        0%{?dist}
Summary:        ROS gauges package

Group:          Development/Libraries
License:        See License.txt
URL:            http://wiki.ros.org/gauges
Source0:        %{name}-%{version}.tar.gz

Requires:       qt-devel
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
BuildRequires:  qt-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs

%description
Launch virtual gauges for ROS topics.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Nov 30 2016 andyz <andyz@utexas.edu> - 1.0.4-0
- Autogenerated by Bloom

* Wed Nov 30 2016 andyz <andyz@utexas.edu> - 1.0.3-0
- Autogenerated by Bloom

* Fri Nov 11 2016 andyz <andyz@utexas.edu> - 1.0.2-0
- Autogenerated by Bloom

* Wed Nov 09 2016 andyz <andyz@utexas.edu> - 1.0.1-2
- Autogenerated by Bloom

