import logging

logger = logging.getLogger(__name__)


import module


class Logtest:
    def logtest1(self):
        print("Test1")
        logger.debug("Dies ist eine Debug Klasse")
         
        module.some_function()
        