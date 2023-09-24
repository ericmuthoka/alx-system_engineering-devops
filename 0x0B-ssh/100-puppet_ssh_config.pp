#!/usr/bin/env puppet
# Puppet manifest to configure SSH client

file { '/home/ubuntu/.ssh':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0700',
}

file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "IdentityFile ~/.ssh/school\nPasswordAuthentication no\n",
  mode    => '0600',
}
