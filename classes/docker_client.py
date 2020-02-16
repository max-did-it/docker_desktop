import docker


class DockerClient:
    """This is a class for docker
    client
    """
    conn = docker.from_env()
