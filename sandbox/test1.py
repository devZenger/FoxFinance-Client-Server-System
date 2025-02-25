import logging

import module
from bla import Logtest


logger = logging.getLogger(__name__)

def main():
    logger.info("Programm gestartet")
    module.some_function()
    
    start = Logtest()
    start.logtest1()
    
    
    

def setup_logging():
    logging.basicConfig(
        filename="server.log",
        level = logging.DEBUG,
        style = "{",
        format = "{asctime} [{levelname:8}] {message}"
    )


if __name__ == "__main__":
    setup_logging()
    main()