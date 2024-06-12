from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

def login(browser, config):
    try:
        browser.get(config['login_url'])
        browser.find_element(By.NAME, "username").send_keys(config['username'])
        browser.find_element(By.NAME, "password").send_keys(config['password'])
        browser.find_element(By.XPATH, "//button[text()='Login']").click()
        WebDriverWait(browser, 10).until(EC.url_contains(config['site_url']))
        logger.info("Login successful")
    except Exception as e:
        logger.error("Error during login: %s", str(e))
        raise

def create_post_ui(browser, title, description, content):
    try:
        browser.find_element(By.XPATH, "//a[text()='Create Post']").click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.NAME, "title")))
        browser.find_element(By.NAME, "title").send_keys(title)
        browser.find_element(By.NAME, "description").send_keys(description)
        browser.find_element(By.NAME, "content").send_keys(content)
        browser.find_element(By.XPATH, "//button[text()='Create']").click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, f"//h2[text()='{title}']")))
        logger.info("Post created successfully with title: %s", title)
    except Exception as e:
        logger.error("Error during post creation via UI: %s", str(e))
        raise

def contact_us(browser, email, subject, message):
    try:
        browser.find_element(By.XPATH, "//a[text()='Contact Us']").click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.NAME, "contact-email")))
        browser.find_element(By.NAME, "contact-email").send_keys(email)
        browser.find_element(By.NAME, "contact-subject").send_keys(subject)
        browser.find_element(By.NAME, "contact-message").send_keys(message)
        browser.find_element(By.XPATH, "//button[text()='Send']").click()
        WebDriverWait(browser, 10).until(EC.alert_is_present())
        alert = browser.switch_to.alert
        alert_text = alert.text
        logger.info("Alert text: %s", alert_text)
        alert.accept()
        return alert_text
    except Exception as e:
        logger.error("Error during Contact Us form submission: %s", str(e))
        raise
