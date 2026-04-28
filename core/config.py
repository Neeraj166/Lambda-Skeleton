
"""
Configuration module
"""

from os import getenv

DB_NAME = getenv('DB_NAME')
CHUNK = int(getenv('CHUNK', 1000))