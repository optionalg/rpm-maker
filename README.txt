To package a simple tarball into an RPM, the following steps will help you get started.

1) Run vagrant up --provision
This will download the necessary dependencies to create the rpm

2) Log into the VM and run "rpmdev-setuptree".  This will setup the basic folder structure needed to create the RPM under ~/rpmbuild (BUILD, BUILDROOT, SPECS, SOURCES, RPM, SRPM).

3) Copy your tarball into the SOURCES folder

4) Create a spec file in the SPECS folder.  You can use the included jenkins-plugins.spec as a starting point.

5) cd into the SPECS folder and run "rpmbuild -ba jenkins-plugins.spec".  This tells rpmbuild to build all the steps in your spec file and will create the rpm in the ~/rpmbuild/RPMS folder.

6) To install the rpm on a test machine
rpm -ivh jenkins-plugins-1-1.fc18.x86_64.rpm

7) To remove an installed rpm on a test machine
rpm -e jenkins-plugins-1-1.fc18.x86_64






