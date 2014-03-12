#!/usr/bin/python

import inspect, os, sys, traceback


#print "Content-type: text/html\r\n\r\n"

#print os.environ

try:
    #global MAESTRANO_ROOT
    MAESTRANO_ROOT = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()) + '/../../'))

    execfile(MAESTRANO_ROOT + '/app/init/auth.py')
    from onelogin.saml import AuthRequest
    from MaestranoService import MaestranoService
    
    maestrano = MaestranoService.getInstance()
    
    auth_request_url = AuthRequest.create(**(maestrano.getSettings().getSamlSettings()))
    #print auth_request_url
    #self.send_response(301)
    #self.send_header("Location", url)
    #self.end_headers()
    print "Location: " + auth_request_url
    print

    #print MAESTRANO_ROOT
    #print "Hello world"
    #from init import auth

except Exception as inst:
    print inst
    print '<br/><br/><br/>'
    print traceback.print_exc(file=sys.stdout)
