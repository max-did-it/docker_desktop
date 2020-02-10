import docker


class DockerClient:
    conn = docker.from_env()
