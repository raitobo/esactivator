import os
import sys
  
WORKDIR             = os.getcwd()
UTIL_DIR            = WORKDIR + '/main/util/'
DATA_DIR            = WORKDIR + '/main/data/'
LOGO_DIR            = WORKDIR + '/main/img/logo/'
BUTTON_DIR          = WORKDIR + '/main/img/button/'
MACHINE_DEVICE      = '/dev/ttyUSB0'

WORK_OFFSET_FILE    = UTIL_DIR + 'workoffset.ini'
TOOL_OFFSET_FILE    = UTIL_DIR + 'tooloffset.ini'

APP_WIDTH           = 800 #800
APP_HEIGHT          = 1215 #1215
NOTEBOOK_HEIGHT     = 600 #1215
APP_TITLE           = "G Code Sender - ES Activator Series"

STATE_ALARM         = ""
DEFAULT_PROFILE     = "G54"         # Default profile to load at first run
CHECK_PERIOD        = 200           # Get grbl message periodically (in millisecond)
BUFFER_LIMIT        = 128