Name:           ros-indigo-libsegwayrmp
Version:        0.2.10
Release:        0%{?dist}
Summary:        ROS libsegwayrmp package

Group:          Development/Libraries
License:        BSD
URL:            http://segwayrmp.github.com/libsegwayrmp/
Source0:        %{name}-%{version}.tar.gz

Requires:       SDL-devel
Requires:       boost-devel
Requires:       qt
Requires:       ros-indigo-catkin
Requires:       ros-indigo-serial
BuildRequires:  SDL-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  qt-devel
BuildRequires:  ros-indigo-serial

%description
This is a C++ library for interfacing with Segway's RMP line of robotic
platforms.

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
* Wed Mar 25 2015 William Woodall <wjwwood@gmail.com> - 0.2.10-0
- Autogenerated by Bloom

