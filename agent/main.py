import sys

from maa.agent.agent_server import AgentServer
from maa.toolkit import Toolkit
import custom


def main():
    try:
        from utils import logger

        Toolkit.init_option("./")

        if len(sys.argv) < 2:
            logger.error("缺少必要的 socket_id 参数")
            return

        socket_id = sys.argv[-1]
        logger.debug(f"socket_id: {socket_id}")

        AgentServer.start_up(socket_id)
        AgentServer.join()
        AgentServer.shut_down()
    except ImportError as e:
        logger.error(f"导入模块失败: {e}")
        logger.error("考虑重新配置环境")
        sys.exit(1)
    except Exception as e:
        logger.exception("agent运行过程中发生异常:{e}")
        raise


if __name__ == "__main__":
    main()
