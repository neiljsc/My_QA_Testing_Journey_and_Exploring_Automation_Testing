from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import logging
import os

def is_element_visible_and_clickable(driver, locator, timeout=10):
    try:
        # Wait for visibility
        element = WebDriverWait(driver, timeout).until(ec.visibility_of_element_located(locator))

        # Wait for clickability
        WebDriverWait(driver, timeout).until(ec.element_to_be_clickable(locator))

        return element
    except (NoSuchElementException, ElementNotInteractableException) as e:
        raise Exception(f"Element not found or not interactable: {locator}. Error: {str(e)}")

# Logger
class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        # Console handler to log to terminal
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        # File handler to log to a file in Utilities directory
        log_file_path = os.path.join("Utilities", "logfile.log")  # Directly use Utilities folder

        # Check if the Utilities directory exists, if not, create it
        if not os.path.exists("Utilities"):
            os.makedirs("Utilities")

        fh = logging.FileHandler(log_file_path, mode='a')  # Open file in append mode
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
    def get_logger(self):
        return self.logger