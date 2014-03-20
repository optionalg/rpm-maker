Vagrant.configure("2") do |config|
  config.vm.box = "fedora-18-x64-vbox4210"
  config.vm.box_url = "http://puppet-vagrant-boxes.puppetlabs.com/fedora-18-x64-vbox4210.box"
  
  config.vm.provision "puppet" do |puppet|
     puppet.manifests_path = "puppet/manifests"
	 puppet.module_path = "puppet/modules"
     puppet.manifest_file  = "site.pp"
	 puppet.options = "--verbose"
  end
  
end
