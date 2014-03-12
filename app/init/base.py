#-----------------------------------------------
# Define root folder
#-----------------------------------------------
if not(defined('MAESTRANO_ROOT')):
    define('MAESTRANO_ROOT', realpath(('%s/../../' % (dirname(XXX("MagicConstant('__FILE__', None)")),))))

#-----------------------------------------------
# Load Libraries & Settings
#-----------------------------------------------
require(('%s/app/init/_lib_loader.php' % (MAESTRANO_ROOT,)), False)
require(('%s/app/init/_config_loader.php' % (MAESTRANO_ROOT,)), False)
