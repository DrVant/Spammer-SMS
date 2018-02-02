#!/usr/bin/python

# - Spammer SMS
# | Description: spams a phone number by sending it a lot of sms by using Grab API
# | Author: DrVant
# | - Added support for phone number with +xxxxxx format 


import spammer_class
spammer = spammer_class.Spammer()
spammer.author = "DrVant"
try:
    spammer.main()
except KeyboardInterrupt:
    print spammer_class.color.FAIL+spammer_class.color.REVERSE+"\r[!][except] KeyboardInterrupt detected! Exiting . . ."+spammer_class.color.ENDC
    exit()
