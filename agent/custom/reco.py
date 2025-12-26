from maa.agent.agent_server import AgentServer
from maa.custom_recognition import CustomRecognition
from maa.context import Context
from typing import Union, Optional
from maa.define import RectType

@AgentServer.custom_recognition("MyCustomRecognition")
class MyCustomRecognition(CustomRecognition):
    def analyze(
        self,
        context: Context,
        argv: CustomRecognition.AnalyzeArg,
    ) -> Union[CustomRecognition.AnalyzeResult, Optional[RectType]]:
        # 实现识别逻辑
        x, y, w, h = 100, 100, 50, 50  # 示例坐标
        return CustomRecognition.AnalyzeResult(box=[x, y, w, h], detail={})