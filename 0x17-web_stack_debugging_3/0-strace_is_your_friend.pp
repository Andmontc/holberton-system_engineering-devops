# Fixes Apache 500 error
exec {
    '/usr/bin/env sed -i "s/phpp/php/g" /var/www/html/wp-settings.php':
}
