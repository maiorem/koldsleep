import sys
import os
from pathlib import Path

CONFIG = None

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')

class Dev_config:

    env_name="DEV"

    debug = True
    
    from eunjeon import Mecab
    
    mecab = Mecab


    staticfiles_dirs = [
        BASE_DIR / "static"
    ]

    static_root = ''


class Live_config:

    env_name="LIVE"

    debug = False

    from konlpy.tag import Mecab

    mecab = Mecab

    staticfiles_dirs = [
        STATIC_DIR
    ]

    static_root = os.path.join(BASE_DIR, 'static')


if len(sys.argv) > 1 and sys.argv[1] =='LIVE':
    CONFIG = Live_config()
else:
    CONFIG = Dev_config()