import os
from logging import *

basicConfig(level={
    'debug': 10,
    'info': 20,
    'warning': 30,
    'error': 40,
    'fatal': 50,
}[os.environ.get('LOG_LEVEL', 'info')])
