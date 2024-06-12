import requests
import logging

logger = logging.getLogger(__name__)

def get_auth_token(username, password, login_url):
    try:
        response = requests.post(login_url, data={"username": username, "password": password})
        response.raise_for_status()
        return response.json().get('token')
    except Exception as e:
        logger.error("Error during getting auth token: %s", str(e))
        raise

def create_post(auth_token, site_url, title, description, content):
    try:
        headers = {
            "X-Auth-Token": auth_token,
            "Content-Type": "application/json"
        }
        post_data = {
            "title": title,
            "description": description,
            "content": content
        }
        response = requests.post(f"{site_url}/api/posts", headers=headers, json=post_data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error("Error during post creation: %s", str(e))
        raise

def get_posts(auth_token, site_url, owner):
    try:
        headers = {
            "X-Auth-Token": auth_token
        }
        response = requests.get(f"{site_url}/api/posts", headers=headers, params={"owner": owner})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error("Error getting posts: %s", str(e))
        raise
