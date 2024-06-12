import pytest
import logging
from utils.ui import login, create_post_ui, contact_us

logger = logging.getLogger(__name__)

def test_successful_login(browser, config):
    try:
        logger.info("Testing successful login")
        login(browser, config)
    except Exception as e:
        logger.error("Error during login: %s", str(e))
        raise

def test_add_post_via_ui(browser, config):
    try:
        logger.info("Testing adding post via UI")
        login(browser, config)
        create_post_ui(browser, "Test Post UI", "This is a test post created via UI", "Test post content via UI")
    except Exception as e:
        logger.error("Error adding post via UI: %s", str(e))
        raise

def test_contact_us_form(browser, config):
    try:
        logger.info("Testing Contact Us form")
        login(browser, config)
        alert_text = contact_us(browser, "test@example.com", "Test Subject", "This is a test message.")
        assert "Message sent successfully" in alert_text, "Alert text does not match expected text"
    except Exception as e:
        logger.error("Error in Contact Us form test: %s", str(e))
        raise
