from aiogram import Router


def setup_routers(router: Router) -> None:
    from . import start
    from . import deploy

    router.include_routers(
        start.router,
        deploy.router,
    )
