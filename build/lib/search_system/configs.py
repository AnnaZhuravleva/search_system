import logging


LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
fh = logging.FileHandler("logs.log")
fh.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
LOGGER.addHandler(fh)
