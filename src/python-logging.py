# import logging      
# logging.basicConfig(level=logging.DEBUG,filename="logfile.log", filemode="a",
# format="%(asctime)s %(levelname)s %(message)s %(filename)s %(lineno)s %(name)s")
# logging.debug("Variable a is assigned with 10")
# logging.info("This is a log function")
# logging.warning("There might be unexpected error")
# try:
#     logging.info("default value giving")
 
#     value=10
#     a=int(input("enter the number:"))
 
#     logging.debug("dividing value by a ")
#     print(value/a)
 
# except ZeroDivisionError as e:
#     logging.warning("zero division log message")
#     logging.error("cannot divisible by zero")
 
# finally:
#     print("done divisible by zero")
#     logging.info("Divison complete")

# import logging
# logger=logging.getLogger("Pooja")
# logging.basicConfig(level=logging.ERROR,filename="logfile.log", filemode="a",
# format="%(asctime)s %(levelname)s %(message)s %(filename)s %(lineno)s %(name)s")
# try:
#     a=10/0
# except Exception:
#     logger.exception("Exception occured")

# import logging
# logger = logging.getLogger("Pooja")
# file_handler = logging.FileHandler("app.log")
# logger.addHandler(file_handler)

