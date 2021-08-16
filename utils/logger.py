import logging

class LogGen:

    @staticmethod
    def logGen():
        logging.basicConfig(filename="D:\Assessment\logs\logger.log",
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            level=logging.INFO)
        logger = logging.getLogger()
        return logger


