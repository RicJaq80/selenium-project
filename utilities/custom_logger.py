import logging
import inspect

def customLogger(logLevel=logging.DEBUG):
    # get the name of the class/method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # by default, log all messages
    logger.setLevel(logging.DEBUG)

    # use automation.log to create just one log instead of {0}.log that will
    # create separate log files every time it is run
    fileHandler = logging.FileHandler("automation.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s -%(name)s %(levelname)s: %(message)s', 
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    return logger