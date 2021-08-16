import logging
import os
from pathlib import Path
rootDir = str(Path(__file__).parent.parent)


class LogGen:

    @staticmethod
    def logGen():
        filename = os.path.join(rootDir, '../logs/logger.log')
        logging.basicConfig(filename=filename,
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            level=logging.INFO)
        logger = logging.getLogger()
        return logger




