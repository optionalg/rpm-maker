class rpm-dep {
  package { 'fedora-packager':
    ensure   => installed,
    provider => yum,
  }
  
  package { 'rpm-build':
    ensure   => installed,
    provider => yum,
  }
  
  package { 'redhat-rpm-config':
    ensure   => installed,
    provider => yum,
  }

}
