import time
from utils.config import REFRESH_TOKEN, USER_ID
from pixivpy3 import AppPixivAPI


def init_api(self) -> AppPixivAPI:
    """
    Initialize the API.

    Returns:
        AppPixivAPI: The API client.
    """

    self.logger.info("[Start] Initialize the API client.")

    refresh_token = REFRESH_TOKEN

    api = AppPixivAPI()
    api.auth(refresh_token=refresh_token)
    time.sleep(2)

    self.logger.info("[End] Initialize the API client.")

    return api


def get_following_users(self, restrict):
    """
    Get the list of users who the target user is following.
    """
    api = self.api
    logger = self.logger
    logger.info("[Start] Get the list of users who the target user is following.")

    # Define a list of users.
    users = []

    # Get the list of users who the target user is following.
    res = self.api.user_following(USER_ID, restrict=restrict)
    time.sleep(5)

    while True:
        try:
            user_ids = [d["user"]["id"] for d in res.user_previews]

            users.extend(user_ids)

            next_url = res.next_url

            if next_url:
                next_qs = api.parse_qs(next_url)
                logger.info(f"Next : {next_qs}")
                time.sleep(2)
                res = api.user_following(**next_qs)
                time.sleep(2)
            else:
                break

        except Exception as e:
            logger.error("Failed to get the user.:", str(e))
            break

    logger.info("[End] Get the list of users who the target user is following.")

    return users


def follow_user(self, user_ids):
    """
    Follow a list of users.
    """
    api = self.api
    logger = self.logger

    is_move = self.mode == "move"

    while True:
        try:
            for user_id in user_ids:
                if is_move:
                    api.user_follow_delete(user_id, self.target)
                    time.sleep(2)

                    api.user_follow_add(user_id, self.target)
                    time.sleep(2)

                    logger.info(f"Move User: {user_id}")
                else:
                    api.user_follow_add(user_id, self.target)
                    time.sleep(2)

                    logger.info(f"Follow User: {user_id}")

        except Exception as e:
            logger.error("Failed to follow or unfollow the user.:", str(e))
            break
