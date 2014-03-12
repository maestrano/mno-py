

class MnoSettings(object, ):
    
    # The name of the application.
    app_name = 'myapp'
    
    # Is SSO enabled for this application
    sso_enabled = False
    
    # If enabled then public access will be completely
    # denied (ALL pages will require authentication)
    sso_intranet_mode = False
    
    # Maestrano Single Sign On url
    sso_url = ''
    
    # The URL where the SSO request should be initiated.
    sso_init_url = ''
    
    # The URL where the SSO response will be posted.
    sso_return_url = ''
    
    # The URL where the application should redirect if
    # user is not given access.
    sso_access_unauthorized_url = ''
    
    # The URL where the application should redirect when
    # user logs out
    sso_access_logout_url = ''
    
    # The x509 certificate used to authenticate the request
    sso_x509_certificate = ''
    
    # Specifies what format to return the identification token (Maestrano user UID)
    sso_name_id_format = OneLogin_Saml_Settings::NAMEID_PERSISTENT;
    
    # The Maestrano endpoint in charge of providing session information
    sso_session_check_url = ''
    
    # Return a settings object for php-saml
    def getSamlSettings(self):
        settings = OneLogin_Saml_Settings()
        
        # Configure SAML
        settings.idpSingleSignOnUrl = self.sso_url
        settings.idpPublicCertificate = self.sso_x509_certificate
        settings.spReturnUrl = self.sso_return_url
        settings.spIssuer = self.app_name
        settings.requestedNameIdFormat = self.sso_name_id_format
        
        return settings
