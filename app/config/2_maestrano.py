# Get Maestrano SSO Host
mno_sso_host = 'http://localhost:3000'

# Endpoint to reach for SSO Identification
mno_settings.sso_url = ('%s/api/v1/auth/saml' % (mno_sso_host,))

# Endpoint to reach for session information (/api/v1/auth/saml/user-xyz?session=df4sd4g3fd345sfgd534)
mno_settings.sso_session_check_url = ('%s/api/v1/auth/saml' % (mno_sso_host,))

# Access unauthorized page
mno_settings.sso_access_unauthorized_url = ('%s/app_access_unauthorized' % (mno_sso_host,))

# Access Logout page
mno_settings.sso_access_logout_url = ('%s/app_logout' % (mno_sso_host,))

# Intranet Mode - If enabled then ALL pages require authentication
mno_settings.sso_intranet_mode = False

# Maestrano X509 Certificate
mno_settings.sso_x509_certificate = '01:06:15:89:25:7d:78:12:28:a6:69:c7:de:63:ed:74:21:f9:f5:36'
