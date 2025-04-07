from selenium import webdriver
from Utilities.helper import Logger  # Import the Logger class

def before_all(context):
    # Set up the logger
    context.logger = Logger("behave_logger").get_logger()  # Pass the logger name and get the logger instance
    context.logger.info("Logger initialized successfully.")  # This should print immediately to terminal and log file
    context.logger.info("Starting WebDriver...")

    # Start WebDriver
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_all(context):
    # Close and quit the browser after all scenarios have run
    context.logger.info("Closing WebDriver...")
    context.driver.quit()