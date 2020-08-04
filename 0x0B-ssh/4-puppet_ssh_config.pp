#SSH configuration file to connect to a server without typing a password

file_line { 'Identityfile':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'Identityfile ~/.ssh/holberton'
}

file_line { ' password off':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
  match  => 'PasswordAuthentication yes'
}