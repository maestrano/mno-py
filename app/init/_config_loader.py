# Initialize mno_settings variable
mno_settings = MnoSettings()

# Require Config files
require(('%s/app/config/1_app.php' % (MAESTRANO_ROOT,)), False)
require(('%s/app/config/2_maestrano.php' % (MAESTRANO_ROOT,)), False)

# Configure Maestrano Service
MaestranoService.configure(mno_settings)
