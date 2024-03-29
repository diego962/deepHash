import logging
from logging import handlers
from os import mkdir

from dph.config import osinfo

PATH_LOG = (
    osinfo.get_env("TEMP") + "\\dph"
    if osinfo.which_os() == "Windows"
    else osinfo.get_env("HOME") + "/dph"
)
LOG_LEVEL = osinfo.get_env("LOG_LEVEL", "INFO").upper()

log = logging.getLogger("DEEPHASH")
fmt = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")


def get_logger(logfile="dph.log"):
    dirlog = ""

    try:
        mkdir(PATH_LOG)

        dirlog = PATH_LOG + osinfo.which_dir_format()
    except FileExistsError:
        dirlog = PATH_LOG + osinfo.which_dir_format()
    finally:
        fh = handlers.RotatingFileHandler(
            dirlog + logfile, maxBytes=10240, backupCount=10
        )
        fh.setLevel(LOG_LEVEL)
        fh.setFormatter(fmt)
        log.addHandler(fh)

        return log
