import logging

from maestro.config import Config
from maestro.factory import create_bot, create_dispatcher


def main():
    config = Config()
    bot = create_bot(config)
    dispatcher = create_dispatcher(config)

    dispatcher.run_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
