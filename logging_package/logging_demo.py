import logging_package.custom_logger as cl
import logging


class LoggingDemo:

    log = cl.custom_logging(logging.INFO)

    def demo1(self):
        self.log.debug("DEBUG")
        self.log.info("INFO")
        self.log.warning("WARNING")
        self.log.error("ERROR")
        self.log.critical("CRITICAL")

    def demo2(self):
        log1 = cl.custom_logging(logging.DEBUG)
        log1.debug("DEBUG")
        log1.info("INFO")
        log1.warning("WARNING")
        log1.error("ERROR")
        log1.critical("CRITICAL")


obj = LoggingDemo()
obj.demo1()
obj.demo2()
