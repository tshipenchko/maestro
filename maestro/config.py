from __future__ import annotations

from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    bot_token: SecretStr

    # alias -> server
    servers: dict[str, dict | Server] = {}
    # who can use the bot
    allowed_chat_ids: list[int] = []

    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=".env",
        env_nested_delimiter="_",
        env_file_encoding="utf-8",
    )

    def __post_init__(self):
        for key, value in self.servers.items():
            self.servers[key] = Server.model_validate(value)


class Server(BaseModel):
    host: str
    port: int = 22
    user: str = "root"

    # empty list means everyone can use it
    allowed_chat_ids: list[int] = []
    actions: dict[str, Action | str] = {}

    def __post_init__(self):
        for key, value in self.actions.items():
            if isinstance(value, str):
                self.actions[key] = Action(command=value)


class Action(BaseModel):
    command: str
    description: str = ""
    allowed_chat_ids: list[int] = []


if __name__ == "__main__":
    server_raw = """
    {
        "host": "130.61.222.225",
        "user": "zxc",
        "allowed_chat_ids": [1845910466],
        "actions": {
            "ping": "ping -c 3 ip.zxc.sx"
        }
    }
    """
    server = Server.model_validate_json(server_raw)
