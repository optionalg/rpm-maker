Name:           jenkins-plugins
Version:        1.532.2
Release:        1
Summary:        The package is used to manage and update Jenkins plugins
License:        GPLv3+
Source0:        jenkins-plugins-1.tar.gz
      
%description 
The package is used to manage and update Jenkins plugins

%prep
rm -rf $RPM_BUILD_DIR/*
tar -xvf $RPM_SOURCE_DIR/jenkins-plugins-1.tar.gz

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/lib/jenkins/plugins/
cp -r $RPM_BUILD_DIR/*.jpi $RPM_BUILD_ROOT/var/lib/jenkins/plugins 

%clean
rm -rf $RPM_BUILD_ROOT

%files
/var/lib/jenkins/plugins/ant.jpi
/var/lib/jenkins/plugins/credentials.jpi
/var/lib/jenkins/plugins/cvs.jpi
/var/lib/jenkins/plugins/external-monitor-job.jpi
/var/lib/jenkins/plugins/git-client.jpi
/var/lib/jenkins/plugins/git.jpi
/var/lib/jenkins/plugins/github-api.jpi
/var/lib/jenkins/plugins/github.jpi
/var/lib/jenkins/plugins/javadoc.jpi
/var/lib/jenkins/plugins/ldap.jpi
/var/lib/jenkins/plugins/mailer.jpi
/var/lib/jenkins/plugins/maven-plugin.jpi
/var/lib/jenkins/plugins/pam-auth.jpi
/var/lib/jenkins/plugins/parameterized-trigger.jpi
/var/lib/jenkins/plugins/scm-api.jpi
/var/lib/jenkins/plugins/ssh-credentials.jpi
/var/lib/jenkins/plugins/ssh-slaves.jpi
/var/lib/jenkins/plugins/subversion.jpi
/var/lib/jenkins/plugins/translation.jpi
