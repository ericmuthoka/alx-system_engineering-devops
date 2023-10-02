# Use Puppet to automate the task of adding a custom HTTP header response

exec { 'update_apt':
  command => '/usr/bin/apt-get update',
}

-> package { 'nginx_install':
  ensure => 'present',
}

-> file_line { 'add_custom_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

-> exec { 'restart_nginx':
  command => '/usr/sbin/service nginx restart',
}
