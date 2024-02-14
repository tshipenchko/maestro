from paramiko import SSHClient, AutoAddPolicy
from paramiko.agent import AgentRequestHandler

from maestro.config import Server


def connect_to_server(server: Server) -> SSHClient:
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(
        hostname=server.hostname,
        port=server.port,
        username=server.username,
    )
    AgentRequestHandler(client.get_transport().open_session())
    return client
