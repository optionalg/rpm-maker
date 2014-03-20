include rpm-dep

# don't do this in prod
package { "puppet": ensure => latest, }