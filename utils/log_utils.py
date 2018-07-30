import logging

import constants

logging.basicConfig(filename=constants.LOGGING_FILENAME,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

LOGGER = logging
