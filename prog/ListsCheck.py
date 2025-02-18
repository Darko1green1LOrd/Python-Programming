from random import randrange
import logging
#this is just to test out logging,zip and if __name__ == "__main__"
""" 
CRITICAL (50)
ERROR    (40)
WARNING  (30)
INFO     (20)
DEBUG    (10)
NOTSET   (0)
"""

def logger_start():
    global logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) #Doesnt show levels below

    #handler = logging.FileHandler('file.txt') For logging to file
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(name)s (%(asctime)s - %(levelname)s) > %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

if __name__ == "__main__": #this wont run if the scrip is imported
    logger_start()

    size = 50
    list1 = [randrange(1,size) for i in range(size)]
    list2 = [randrange(1,size) for i in range(size)]

    for i,(l1,l2) in enumerate(zip(list1,list2)):
        if l1 == l2:
            logger.info(f"Match found at {i} ({l1} {l2})")

    if logger.getEffectiveLevel() == logging.DEBUG:
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')