#!/usr/bin/python

# - Spammer V alpha
# | Description: spams a phone number by sending it a lot of sms by using Grab API
# | Author: DrVant
# | Date: 18/11/2017
# | Disclaimer: Editing author will not make you the real coder
# | What's New?
# | - Added coloring
# | - Added support multiple proxies (BETA)
# | - Added feature to create a new separate thread for each proxy in order to increase spam speed (BETA)
# | - Added support for phone number with +xxxxxx format 
# | - And another fixes

import spammer_class
spammer = spammer_class.Spammer()
spammer.author = "DrVant"
try:
    spammer.main()
except KeyboardInterrupt:
    print spammer_class.color.FAIL+spammer_class.color.REVERSE+"\r[!][except] KeyboardInterrupt detected! Exiting . . ."+spammer_class.color.ENDC
    exit()
