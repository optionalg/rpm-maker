Vagrant.configure("2") do |config|
  config.vm.box = "fedora-18-x64-vbox4210"
  config.vm.box_url = "http://puppet-vagrant-boxes.puppetlabs.com/fedora-18-x64-vbox4210.box"
  config.vm.provision "shell", inline: "yum -y install fedora-packager rpm-build redhat-rpm-config"
end
