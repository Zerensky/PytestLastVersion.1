import pytest
import logging
from utils.api import create_post, get_posts

logger = logging.getLogger(__name__)

def test_check_post_title(auth_token, config):
    try:
        logger.info("Testing presence of post title")
        posts = get_posts(auth_token, config['site_url'], owner="notMe")
        post_titles = [post['title'] for post in posts]
        assert "Post Title 1" in post_titles, "Post with title 'Post Title 1' not found."
        logger.info("Post title 'Post Title 1' found.")
    except Exception as e:
        logger.error("Error checking post title: %s", str(e))
        raise

def test_create_and_check_post(auth_token, config):
    try:
        logger.info("Creating and checking new post")
        post_data = {
            "title": "Test Post",
            "description": "This is a test post",
            "content": "Test post content"
        }
        create_post(auth_token, config['site_url'], **post_data)
        posts = get_posts(auth_token, config['site_url'], owner="me")
        post_descriptions = [post['description'] for post in posts]
        assert post_data['description'] in post_descriptions, f"Post with description '{post_data['description']}' not found."
        logger.info("Post with description '%s' found", post_data['description'])
    except Exception as e:
        logger.error("Error creating or checking post: %s", str(e))
        raise
