from maa.agent.agent_server import AgentServer

from utils import logger

@AgentServer.custom_action("MyCustomAction")
class MyCustomAction:
    def run(self, context, argv):
        logger.info("自定义行为")
        logger.info(argv)
        return True