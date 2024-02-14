from io import BytesIO

from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, BufferedInputFile

from maestro.config import Server, Action, Config
from maestro.ssh_client import connect_to_server
from maestro.text_to_png import text_to_png

router = Router()


def run_action(server: Server, action: Action) -> BytesIO:
    client = connect_to_server(server)
    stdin, stdout, stderr = client.exec_command(action.command)

    text = f"{stdout.read().decode()}\n{stderr.read().decode()}"
    png_file = text_to_png(text)
    client.close()

    return png_file


@router.message(
    Command(commands=["d", "deploy"]),
)
async def handle_command_deploy(
    message: Message, command: CommandObject, config: Config
) -> None:
    args = command.args.split()
    if len(args) == 0:
        # here we will show the list of servers
        servers = "\n".join(name for name in config.servers)
        await message.reply(
            f"Usage: /deploy <server> <action>\nAvailable servers:\n{servers}"
        )
        return
    if len(args) == 1:
        # here we will show the list of actions
        server = config.servers.get(args[0])
        if not server:
            await message.reply("Server not found")
            return
        actions = "\n".join(name for name in server.actions)
        await message.reply(
            f"Usage: /deploy {args[0]} <action>\nAvailable actions:\n{actions}"
        )
        return
    if len(args) != 2:
        await message.reply("Usage: /deploy <server> <action>")
        return

    server, action = args
    server = config.servers.get(server)

    if not server:
        await message.reply("Server not found")
        return

    action = server.actions.get(action)
    if not action:
        await message.reply("Action not found")
        return

    png_file = run_action(server, action)

    await message.reply_photo(
        photo=BufferedInputFile(png_file.read(), filename=png_file.name),
        caption=f"Result of action {action.name} on {server.name}",
    )
