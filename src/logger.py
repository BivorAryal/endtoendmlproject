import logging  #A built-in Python module for tracking events that happen while the software runs (like printing messages, errors, etc.).
import os #A module to interact with the operating system, useful for file and path handling.
from datetime import datetime  #work with dates and times.

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #creates a log file name based on the current date and time.('10_24_2024_15_35_50.log.')
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #constructs a file path in the current working directory (os.getcwd()) inside a folder named logs
os.makedirs(logs_path,exist_ok=True) #reates the logs directory if it doesn't already exist, so your log files will be stored in that folder.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #This creates the full path for where the log file will be stored by joining the directory path (logs_path) with the log file name (LOG_FILE).

#Setting up the logging configuration:
logging.basicConfig(
    filename=LOG_FILE_PATH, # tells Python where to save the log messages (the path we created earlier)
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", #specifies how the log messages will look. 
    level=logging.INFO, #This sets the logging level to INFO, meaning it will log informational messages and anything more severe (like warnings or errors).


)

'''
if __name__=="__main__":
    logging.info("Loggin has started")

'''
'''

This checks if the script is being run directly (not imported as a module).
logging.info("Logging has started"): 
This logs a message saying "Logging has started" at the INFO level, meaning this message will be written to the log file.

'''