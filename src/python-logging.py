import logging      
logging.basicConfig(level=logging.DEBUG,filename="logfile.log", filemode="a",
format="%(asctime)s %(levelname)s %(message)s %(filename)s %(lineno)s %(name)s")
logging.debug("Variable a is assigned with 10")
logging.info("This is a log function")
logging.warning("There might be unexpected error")