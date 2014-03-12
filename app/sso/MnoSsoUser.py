from MnoSsoBaseUser import MnoSsoBaseUser

#
# Configure App specific behavior for 
# Maestrano SSO
#
class MnoSsoUser(MnoSsoBaseUser):
    # Database connection
    connection = None
    
    #
    # Extend constructor to inialize app specific objects
    #
    # @param OneLogin_Saml_Response $saml_response
    #   A SamlResponse object from Maestrano containing details
    #   about the user being authenticated
    #
    def __init__(self, saml_response, session=[], opts=[]):
        super(MnoSsoBaseUser,self).__init__(saml_response,session)
        #parent.__construct(saml_response, session)
        self.connection = opts['db_connection']