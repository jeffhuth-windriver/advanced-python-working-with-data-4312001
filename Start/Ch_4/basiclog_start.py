# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging
from datetime import datetime

# TODO: Use basicConfig to configure logging
logging.basicConfig(level=logging.DEBUG, filename="output_1.log", filemode="w")

# TODO: Try out each of the log levels
logging.debug("debug level")
logging.info("info level")
logging.warning("warning level")
logging.error("error level")
logging.critical("critical level")

# TODO: Output formatted strings to the log
nm = "Jeff Huth"
dttm_now = datetime.now()
dttm_str = datetime.strftime(dttm_now, "%Y-%m-%dT%H:%M:%SZ")
logging.info(f"{dttm_str}: {nm} was here.")