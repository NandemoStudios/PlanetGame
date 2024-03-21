import logging

logfile = open("../log.txt", "a+")
logfile.write("")
logfile.close()


def error(text):
    logging.error(text)
    logfile_ = open("log.txt", "w+")
    logfile_.write("ERROR: " + text)
    logfile_.close()


def log(level, text):
    try:
        logging.log(level, text)
    except ValueError:
        error("Your text wasn't a string, or your level was an invalid value")
