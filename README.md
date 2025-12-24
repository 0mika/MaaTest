# 描述

- 克隆你自己的仓库到本地，并拉取子模块 
  
        git clone --recursive https://github.com/0mika/MaaTest.git
    如已克隆但发现资源缺失，可运行：

        git submodule update --init --recursive

- python环境为开发环境，运行 `uv sync` 自动搭建环境

- 下载maaframework解压至deps文件夹中

- assets\MaaCommonAssets文件夹中放置通用模型，使用模型时导入到model\ocr中
