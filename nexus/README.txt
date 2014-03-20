rpmdev-setuptree

cp /vagrant/nexus-2.7.2-03-bundle.tar.gz ~/rpmbuild/SOURCES
cp /vagrant/nexus/nexus.spec ~/rpmbuild/SPECS
cd ~/rpmbuild/SPECS
rpmbuild -ba nexus.spec
tar -xvf /home/vagrant/rpmbuild/SOURCES/nexus-2.7.2-03-bundle.tar.gz

Don't include any directories on the %files section