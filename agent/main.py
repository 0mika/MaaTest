import sys

from maa.agent.agent_server import AgentServer
from maa.toolkit import Toolkit


def main():
    import custom
    from utils import logger

    Toolkit.init_option("./")

    if len(sys.argv) < 2:
        logger.error("缺少必要的 socket_id 参数")
        return

    socket_id = sys.argv[-1]
    logger.debug(f"socket_id: {socket_id}")

    AgentServer.start_up(socket_id)
    logger.info("AgentServer启动")
    AgentServer.join()
    AgentServer.shut_down()
    logger.info("AgentServer关闭")


if __name__ == "__main__":
    main()
