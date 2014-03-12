#-----------------------------------------------
# Require dependencies
#-----------------------------------------------
define('PHP_SAML_XMLSECLIBS_DIR', ('%s/lib/php-saml/ext/xmlseclibs/' % (MAESTRANO_ROOT,)))
require(('%sxmlseclibs.php' % (PHP_SAML_XMLSECLIBS_DIR,)), False)

define('PHP_SAML_DIR', ('%s/lib/php-saml/src/OneLogin/Saml/' % (MAESTRANO_ROOT,)))
require(('%sAuthRequest.php' % (PHP_SAML_DIR,)), False)
require(('%sResponse.php' % (PHP_SAML_DIR,)), False)
require(('%sSettings.php' % (PHP_SAML_DIR,)), False)
require(('%sXmlSec.php' % (PHP_SAML_DIR,)), False)

#-----------------------------------------------
# Require Maestrano library
#-----------------------------------------------
define('MNO_PHP_DIR', ('%s/lib/mno-php/src/' % (MAESTRANO_ROOT,)))
require(('%sMnoSettings.php' % (MNO_PHP_DIR,)), False)
require(('%sMaestranoService.php' % (MNO_PHP_DIR,)), False)
require(('%ssso/MnoSsoBaseUser.php' % (MNO_PHP_DIR,)), False)
require(('%ssso/MnoSsoSession.php' % (MNO_PHP_DIR,)), False)

#-----------------------------------------------
# Require Maestrano app files
#-----------------------------------------------
define('MNO_APP_DIR', ('%s/app/' % (MAESTRANO_ROOT,)))
require(('%s/sso/MnoSsoUser.php' % (MNO_APP_DIR,)), False)
