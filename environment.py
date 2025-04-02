from selenium import webdriver
import logging
import os

def before_all(context):
    # Define the log file path
    log_file_path = os.path.join("Utilities", "Logs", "logfile.log")

    # Set up logging
    logging.basicConfig(
        level=logging.INFO,  # Set the logging level (INFO, DEBUG, etc.)
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file_path, mode ='a'),
            logging.StreamHandler()
        ]
    )
    context.logger = logging.getLogger()

    # Start WebDriver
    context.logger.info("Starting WebDriver...")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_all(context):
    # To Close and quit browser after all scenarios have run
    context.logger.info("Closing WebDriver...")
    context.driver.quit()