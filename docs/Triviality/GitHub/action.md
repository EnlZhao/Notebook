# GitHub Actions

## GitHub Actions 是什么？

!!! abstract
    - GitHub Actions 是一种持续集成和持续交付 (CI/CD) 平台，可用于自动执行生成、测试和部署管道。 您可以创建工作流程来构建和测试存储库的每个拉取请求，或将合并的拉取请求部署到生产环境。
    - GitHub Actions 不仅仅是 DevOps，还允许您在存储库中发生其他事件时运行工作流程。 例如，您可以运行工作流程，以便在有人在您的存储库中创建新问题时自动添加相应的标签。
    - GitHub 提供 Linux、Windows 和 macOS 虚拟机来运行工作流程，或者您可以在自己的数据中心或云基础架构中托管自己的自托管运行器。

首先，一个持续集成会由很多操作组成，比如抓取代码、运行测试、登录远程服务器，发布到第三方服务等等。GitHub 把这些操作就称为 actions。

用户可以在 [官方市场](https://github.com/marketplace?type=actions) 或 [awesome actions](https://github.com/sdras/awesome-actions) 搜索到别人提交的 actions 脚本

因为，每个 action 就是一个独立脚本，因此可以做成代码仓库，可以使用 `userName/repoName` 的语法引用 `action`。比如， `actions/setup-node` 就表示 `github.com/actions/setup-node` 这个仓库，它代表一个 `action`，作用是安装 `Node.js`。

!!! success
    事实上，GitHub 官方的 actions 都放在 [github.com/actions](https://github.com/actions) 里面

## Workflow 文件

!!! abstract "Workflow 文件"
    - `GitHub Actions` 的配置文件叫做 `workflow` 文件，存放在代码仓库的 `.github/workflows/` 目录下
    - `workflow/` 下的文件采用 `YAML` 格式，文件名可以任意取，但是后缀名统一为 `yml` 或者 `yaml`
    - 一个库可以有多个 `workflow` 文件。GitHub 只要发现 `.github/workflows` 目录下里面有 `yml`/`yaml` 文件，就会自动运行该文件。

下面简单介绍 `workflow` 文件的字段：








??? quote "reference"
    - https://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html
    - https://docs.github.com/zh/actions/learn-github-actions/understanding-github-actions