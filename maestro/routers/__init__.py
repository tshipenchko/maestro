from aiogram import Router


def setup_routers(router: Router) -> None:
    from . import start

    router.include_routers(
        start.router,
    )
