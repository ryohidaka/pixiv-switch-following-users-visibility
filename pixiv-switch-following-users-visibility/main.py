from utils.config import get_args
from utils.logger import init_logger
from utils.pixiv import init_api


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
if __name__ == "__main__":
    app = AppClass()
    app.main()
