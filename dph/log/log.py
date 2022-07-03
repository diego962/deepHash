import logging
from logging import handlers
from dph.config import osinfo
from os import mkdir

PATH_LOG = osinfo.get_env('TEMP') \
           if osinfo.which_os() == 'Windows' \
           else '/var/log/dph'
LOG_LEVEL = osinfo.get_env("LOG_LEVEL", "INFO").upper()

log = logging.getLogger("DEEPHASH")
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s %(message)s'
)


def get_logger(logfile="dph.log"):
    dirlog = None

    try:
        mkdir(
            PATH_LOG + 
            osinfo.which_dir_format() + 
            "dph" + 
            osinfo.which_dir_format()
        )

        dirlog = PATH_LOG + \
                osinfo.which_dir_format() + \
                 "dph" + \
                osinfo.which_dir_format() 
    except FileExistsError as e:
        dirlog = PATH_LOG + \
                osinfo.which_dir_format() + \
                 "dph" + \
                osinfo.which_dir_format() 
    finally:
        fh = handlers.RotatingFileHandler(
            dirlog + logfile,
            maxBytes=10240,
            backupCount=10
        )
        fh.setLevel(LOG_LEVEL)
        fh.setFormatter(fmt)
        log.addHandler(fh)

        return log