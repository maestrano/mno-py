# Get full host (protocal + server host)
protocol = ('https://' if (('HTTPS' in _SERVER) and (_SERVER['HTTPS'] != 'off')) else 'http://')
full_host = ('%s%s' % (protocol, _SERVER['HTTP_HOST']))

# Name of your application
mno_settings.app_name = 'my-app'

# Enable Maestrano SSO for this app
mno_settings.sso_enabled = True

# SSO initialization URL
mno_settings.sso_init_url = ('%s/maestrano/auth/saml/index.php' % (full_host,))

# SSO processing url
mno_settings.sso_return_url = ('%s/maestrano/auth/saml/consume.php' % (full_host,))
