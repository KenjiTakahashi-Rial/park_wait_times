import json
import os
import sys

CONFIG_DIR: str = os.path.dirname(sys.modules[__name__].__file__ or "")
CONFIG_FILE_NAME: str = "config.json"
CONFIG_PATH: str = os.path.join(CONFIG_DIR, CONFIG_FILE_NAME)
with open(CONFIG_PATH) as f:
    CONFIG: dict = json.load(f)
