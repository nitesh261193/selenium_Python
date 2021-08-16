import configparser

config = configparser.RawConfigParser()
config.read("D:\Assessment\configuration\config.ini")


class readConfig:

    @staticmethod
    def getBaseURL():
        url = config.get("common info", "baseURL")
        return url


