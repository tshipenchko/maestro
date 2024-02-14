from aiogram import Bot, Dispatcher, enums

from maestro.config import Config
from maestro.routers import setup_routers


def create_bot(config: Config) -> Bot:
    return Bot(
        token=config.bot_token.get_secret_value(),
        parse_mode=enums.ParseMode.HTML,
    )


def create_dispatcher(config: Config) -> Dispatcher:
    dispatcher = Dispatcher()

    dispatcher["config"] = config
    setup_routers(dispatcher)

    return dispatcher
