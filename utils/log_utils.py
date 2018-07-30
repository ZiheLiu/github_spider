import logging

import constants

formatter = '%(asctime)s - %(levelname)s - %(message)s'

logging.basicConfig(filename=constants.LOGGING_FILENAME,
                    level=logging.INFO,
                    format=formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(formatter))
logging.getLogger().addHandler(console_handler)

LOGGER = logging
