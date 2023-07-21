from utils.logger import init_logger


class AppClass:
    def __init__(self):
        self.logger = init_logger()

    def main(self):
        logger = self.logger


if __name__ == "__main__":
    app = AppClass()
    app.main()
