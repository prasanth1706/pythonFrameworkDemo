from venv import logger

from playwright.sync_api import Page, expect
from time import sleep
from pathlib import Path
import logging


#Create the log folder
logfolder = Path.cwd() / "logs"
# this line actially checks for folder existence and creates it if it doesn't exist. The parents=True argument allows the creation of parent directories if they don't exist, and exist_ok=True prevents an error if the folder already exists.
logfolder.mkdir(parents=True, exist_ok=True)  
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',filename=logfolder / 'test_multiwindow.log', filemode='a')
logfile = logfolder / 'test_multiwindow.log'
logger = logging.getLogger("Multi window test")

logger.setLevel(logging.INFO)
logger.propagate = False  # Prevent log messages from being propagated to the root logger

handler = logging.FileHandler(logfile)
handler.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter) 

logger.addHandler(handler)

def test_multiwindow(page: Page):
    page.goto("https://the-internet.herokuapp.com/windows")
    page.get_by_role("link", name="Click Here").click()
    sleep(2)  # Wait for 2 seconds to ensure the new window is fully
    page.wait_for_load_state("load")  # Wait for the new window to fully load
     # Get the last opened page (new
    logger.info(f"Number of open pages: {len(page.context.pages)}")  # Print the number of open pages
    new_page = page.context.pages[-1] 
    logger.error("parent URL: %s", page.url)  # Print the URL of the parent page
    logger.info("child URL: %s", new_page.url)  # Print the URL of the new page



for handler in logger.handlers:
    handler.flush()  

