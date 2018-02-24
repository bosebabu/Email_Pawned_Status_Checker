# install hibp module using pip: pip install hibp

from hibp import HIBP, AsyncHIBP
import json

email=raw_input("Enter email: ")

req = HIBP.get_account_breaches(email)
req.execute()
output=str(json.dumps(req.response, indent=4, sort_keys=True))

if output!="\"object has not been pwned.\"":
    print "\nOOPS!!! You've been pawned. "+str(len(req.response))+" entrie(s) found."
    print "========================================"
    print "              Pawn Results"
    print "========================================\n"
    print output
else:
    print "\nCongrats!!! not pawned.\n"
