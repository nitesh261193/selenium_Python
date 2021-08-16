import configparser
from pathlib import Path

rootDir = str(Path(__file__).parent.parent)
config = configparser.RawConfigParser()
config.read(rootDir + "\configuration\config.ini")


class readConfig:

    @staticmethod
    def getBaseURL():
        url = config.get("common info", "baseURL")
        return url
