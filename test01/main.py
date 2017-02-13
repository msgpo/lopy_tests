# main file (started after boot)
#

import machine
from machine import  reset
print( "Main: started.")

print("Main: setting up wifi.")
import wifi

#import loratest
#loratest.run()
