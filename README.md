# Habitica Party Management Automation

## 简介

该仓库包含了用于自动化管理Habitica派对的脚本和配置。Habitica是一款游戏化的任务管理应用，而派对是一群可以协作和支持彼此的玩家。自动化处理包括邀请新成员、移除不活跃成员以及更新派对描述等任务。

## 功能

- **成员管理**：自动添加或移除派对成员。
- **活动监控**：跟踪成员活动。
- **派对描述更新**：定期更新派对描述以包含相关信息。

## 使用方法

该自动化设置通过GitHub Actions运行。必要的流程和脚本包含在此仓库中。要使用此自动化，您需要根据特定需求配置GitHub Actions工作流程。

## 仓库结构

- `scripts/`：包含用于管理Habitica派对的Python脚本。
- `documents/`：包含模板。
- `logs/`：包含脚本的日志。
- `.github/workflows/`：包含定义自动化任务的GitHub Actions工作流程文件。

## 要求

- 仓库已启用GitHub Actions。
- Habitica API凭据用于认证。

## 许可证

该项目在MIT许可证下授权 - 详见LICENSE文件。

## 注意

GitHub Actions工作流程的实际实现未包含在此README中，应在仓库的`.github/workflows`目录中单独配置。

---

此README提供了仓库目的和结构的简要概述。有关详细设置和配置说明，请参考仓库内的文档。
