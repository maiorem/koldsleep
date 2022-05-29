import sys

CONFIG = None

class Dev_config:

    env_name="DEV"
    debug = True
    

class Live_config:

    env_name="LIVE"
    debug = False


if sys.argv[1] =='runserver' or sys.argv[1] == 'makemigrations' or sys.argv[1] == 'migrate' or sys.argv[1] == 'createsuperuser':
    CONFIG = Dev_config()
else:
    CONFIG = Live_config()