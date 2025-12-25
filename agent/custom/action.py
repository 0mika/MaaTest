import json

from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.context import Context

from utils import logger


@AgentServer.custom_action("Init")
class Init(CustomAction):
    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> bool:

        param = json.loads(argv.custom_action_param or "{}")
        _status.loop_count = param.get("loop_count")
        _status.max_loops = param.get("max_loops")

        logger.info(f"循环次数{_status.max_loops}")
        logger.info(f"开始运行")

        return True


@AgentServer.custom_action("MyCustomAction")
class MyCustomAction(CustomAction):
    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> bool:

        # 计算器递增
        _status.loop_count += 1
        logger.info(f"当前次数{_status.loop_count}")

        return True


@AgentServer.custom_action("LoopControl")
class LoopControl(CustomAction):
    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> bool:

        if _status.loop_count < _status.max_loops:
            # 继续重复整个工作流程
            context.override_next(argv.node_name, ["ProcessStep1"])
        else:
            # 退出循环
            context.override_next(argv.node_name, ["ExitLoop"])

        return True


# 状态保存
class _status:
    loop_count = 0
    max_loops = 0
