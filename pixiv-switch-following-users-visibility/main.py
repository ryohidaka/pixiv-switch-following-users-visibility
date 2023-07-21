from utils.config import get_args
from utils.logger import init_logger
from utils.pixiv import follow_user, get_following_users, init_api


class AppClass:
    def __init__(self):
        self.logger = init_logger()

    def main(self):
        logger = self.logger

        # Initialize the API.
        self.api = init_api(self)

        args = get_args()

        # Get the type of the source restrict.
        self.source = args["source"]
        source = self.source

        # Get the type of the target restrict.
        self.target = args["target"]
        target = self.target

        if source == target:
            logger.error(
                "The same 'restrict' is specified for both Source and Target. Please specify a different 'restrict'."
            )
            return

        logger.info(f"Direction: {source} => {target}")

        # Get the mode.
        self.mode = args["mode"]
        self.logger.info(f"Mode: {self.mode}")

        # Get the source users.
        source_users = get_following_users(self, source)
        source_users_count = len(source_users)
        logger.info(f"Source['{source}']: {source_users_count} users.")
        if (source_users_count) == 0:
            logger.info(
                f"The process is ending because there is no {source} following users."
            )
            return

        # Get the target users.
        target_users = get_following_users(self, target)
        target_users_count = len(target_users)
        logger.info(f"Target['{target}']: {target_users_count} users.")

        # Get diff
        diff = [x for x in source_users if x not in target_users]
        logger.info(f"Diff: {len(diff)} users.")

        if (len(diff)) == 0:
            logger.info("The process is ending because there is no difference.")
            return

        # Move or Copy users
        follow_user(self, diff)


if __name__ == "__main__":
    app = AppClass()
    app.main()
