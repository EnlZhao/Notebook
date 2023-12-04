# Getting started with Git

> [官方文档](https://docs.github.com/en/get-started/getting-started-with-git)

## Set your username

=== "Set for every repository"
    === "config"
        ```bash
        $ git config --global user.name "MoLan"
        ```
    === "check"
        ```bash
        $ git config --global user.name
        > MoLan
        ```
=== "Set for a single repository"
    === "config"
        ```bash
        $ git config user.name "MoLan"
        ```
    === "check"
        ```bash
        $ git config user.name
        > MoLan
        ```

> `email` 设置同理，只需将 `name` 替换为 `email` 即可

## Caching credentials

> 建议直接用 `ssh` 克隆
> 
> - 使用 `HTTPS` 克隆仓库时，可以使用凭据帮助程序在 Git 中缓存 GitHub 凭据
> - 如果是使用 `ssh` 克隆仓库，则不需要凭据帮助程序

[More details](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git?platform=mac)

## Git passordwords

- 一般在使用 `HTTPS` 克隆仓库时，会要求输入 GitHub credentials (用户名和密码)
- 但此时的用户名密码并非 GitHub 账户密码，而是 GitHub personal access token
- 可以通过配置 `Git` cache credentials 来避免每次都要求输入 GitHub credentials
    - 在配置凭据缓存后，当使用 `HTTPS` 拉取或推送时，Git 将自动使用缓存的 personal access token

## SSH and GPG keys

> 配置 `ssh` 公钥，可以在不输入 GitHub credentials 的情况下，与 GitHub 通信

=== "简约版"
    ```
    $ ssh-keygen -t rsa -C "email address"
    # enter, enter ...
    ```

    - 查看公钥 `id_rsa.pub` 文件

    ```bash
    $ cat ~/.ssh/id_rsa.pub
    ```

    - 将其中内容复制到 GitHub 的 `SSH and GPG keys` 中<br>![](../../Images/2023-11-30-15-51-32.png)

=== "官方版"
    [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)


## macOS Keychain credentials

> - 从 macOS 更新密钥链凭据仅使用内置到 macOS 中的 `osxkeychain` 凭据帮助程序手动配置了 personal access token 的用户
> - 还是建议使用 `ssh` 或者 [GCM | Git Credential Manager](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git)

=== "通过 Keychain Access 更新 credentials"
    1. 打开 `Keychain Access` 应用
    2. 在搜索框中输入 `github.com`
    3. 查找 `github.com` 的 `Internet password` 条目
    4. 编辑或删除条目
=== "通过命令行删除 credentials"

    ```bash
    $ git credential-osxkeychain erase
    host=github.com
    protocol=https
    > [Press Return]
    ```

    - 通过命令行删除 credentials 会删除所有 GitHub 凭据，而不仅仅是当前仓库或当前用户的凭据
    - 可以尝试克隆专用仓库，以便在删除凭据后测试是否仍需要输入 GitHub 凭据


## Git workflows ｜ TODO

## <u>About remote repositories</u>

!!! abstract "关于远程仓库"
     * 远程 URL 是 Git 一种指示“您的代码存储位置”的绝佳方式 
     * 只能推送两类 URL 地址:  
         * HTTPS URL (例如 `https://github.com/user/repo.git`)
         * SSH URL   (例如 `git@github.com:user/repo.git`)
     * Git 将远程 URL 与名称相关联，默认远程通常命为 `origin`

### 创建远程仓库

可以使用 `git remote add` 命令将远程 URL 与名称匹配
!!! example
     > git remote add origin <REMOTE_URL>
     
     将 origin 与 `REMOTE_URL` 关联


## <u>Manage remote repositories</u>

### 添加远程仓库

* 使用 `git remote add` 在终端存储存储库的目录中新增远程
* `git remote add` 采用两个参数:
    * 远程名称 (如 `origin`)
    * 远程 URL (如 `https://github.com/user/repo.git`)
??? example
     ```bash
     $ git remote add origin https://github.com/USER/REPO.git
     # Set a new remote

     $ git remote -v
     # Verify new remote
     > origin  https://github.com/USER/REPO.git (fetch)
     > origin  https://github.com/USER/REPO.git (push)
     ```

??? warning "Troubleshooting: Remote origin already exists"
     此错误消息表示尝试添加的远程与本地仓库远程名称相同
     ```bash
     $ git remote add origin https://github.com/octocat/Spoon-Knife.git
     > fatal: remote origin already exists.
     ```
     三种解决方法: 
          1. 对新远程使用不同名称
          2. 在添加新远程时，重命名现有远程仓库
          3. 在添加新远程前，删除现有远程仓库

### 更改远程仓库 URL

* `git remote set-url` 命令更改现有远程仓库 URL
* 该命令采用两个参数: 
    * 现有远程仓库名称。如，`origin` ···
    * 远程仓库的新 URL。如:
        * 若要更新为使用 HTTPS，URL 形如 `https://github.com/USERNAME/REPOSITORY.git`
        * 若要更新为使用 SSH，URL 形如 `git@github.com:USERNAME/REPOSITORY.git`

=== "将远程 URL 从 SSH 切换到 HTTPS"
     
     1. 打开 Git Bash || 终端
     2. 将当前目录更改为本地仓库
     3. 列出现有仓库
     ```bash
     $ git remote -v
     > origin  git@github.com:USERNAME/REPOSITORY.git (fetch)
     > origin  git@github.com:USERNAME/REPOSITORY.git (push)
     ```
     4. 使用 `git remote set-url` 命令将远程 URL 从SSH 更改为 HTTPS
     ```bash
     $ git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
     ```
     5. 验证
     ```bash
     $ git remote -v
     # Verify new remote URL
     > origin  https://github.com/USERNAME/REPOSITORY.git (fetch)
     > origin  https://github.com/USERNAME/REPOSITORY.git (push)
     ```
     > 下次将 `git fetch`、`git pull`、`git push`执行到远程存储库时，系统将要求提供 GitHub 用户名和密码。
     > 可以使用[ GitHub 凭据帮助程序](https://docs.github.com/zh/get-started/getting-started-with-git/caching-your-github-credentials-in-git)，以便 Git 每次与 GitHub 通信时都会记住你的 GitHub 用户名和 personal access token

=== "将远程 URL 从 HTTPS 切换到 SSH"
     
     1. 打开 Git Bash || 终端
     2. 将当前目录更改为本地仓库
     3. 列出现有仓库
     ```bash
     $ git remote -v
     > origin  https://github.com/USERNAME/REPOSITORY.git (fetch)
     > origin  https://github.com/USERNAME/REPOSITORY.git (push)
     ```
     4. 使用 `git remote set-url` 命令将远程 URL 从 HTTPS 更改为 SSH
     ```bash
     $ git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
     ```
     5. 验证
     ```bash
     $ git remote -v
     # Verify new remote URL
     > origin  git@github.com: USERNAME/REPOSITORY.git (fetch)
     > origin  git@github.com: USERNAME/REPOSITORY.git (push)
     ```
     > 下次将 `git fetch`、`git pull`、`git push`执行到远程存储库时，系统将要求提供 GitHub 用户名和密码。
     > 可以使用[ GitHub 凭据帮助程序](https://docs.github.com/zh/get-started/getting-started-with-git/caching-your-github-credentials-in-git)，以便 Git 每次与 GitHub 通信时都会记住你的 GitHub 用户名和 personal access token

### 重命名远程仓库

* 使用 `git remote rename` 命令重命名现有远程
* `git remote rename` 命令采用两个参数:
    * 现有远程名称（如 original）
    * 远程的新名称（如 destination）

### 删除远程仓库

* 使用 `git remote rm` 命令从存储库中删除远程 URL。
* 该命令采用一个参数：
    * 远程名称（例如 destination）

> 从存储库中删除远程 URL 只会取消本地和远程存储库的链接。 它不会删除远程存储库

### `git push`

- `git push` 会将本地仓库的内容推送到远程仓库
- `git push` 命令采用两个参数:
    - 远程仓库的名称 (如 `origin`)
    - 要推送的分支的名称 (如 `main`)
- `git push` 命令的默认行为是将本地分支推送到与之关联的远程分支
- 例如，如果本地分支为 `main`，则 `git push` 将自动推送到远程分支 `origin/main`
- 可以使用 `git push` 命令的 `--set-upstream` 标志将本地分支与远程分支关联起来
    - `git push --set-upstream origin main`
- 可以使用 `git push` 命令的 `--force` 标志强制推送到远程分支
    - `git push --force origin main`
- 可以使用 `git push` 命令的 `--all` 标志推送所有分支
    - `git push --all origin`

## Associate text editors

- 配置 `git config` 中的 `core.editor` 选项，可以将文本编辑器与 Git 关联

=== "Mac | Linux"
    === "VS Code"
        ```bash
        $ git config --global core.editor "code --wait"
        ```
    === "Sublime Text"
        ```bash
        $ git config --global core.editor "subl -n -w"
        ```
=== "Windows"
    === "VS Code"
        ```bash
        $ git config --global core.editor "code --wait"
        ```
    === "Sublime Text"
        ```bash
        $ git config --global core.editor "'C:/Program Files/Sublime Text 3/subl.exe' -w"
        ```

## Handle line endings | TODO

> [To avoid problems in your diffs, you can configure Git to properly handle line endings.](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings?platform=mac)

## Ignoring files

> - 即配置 `.gitignore` 文件
> - 如果在配置前已经提交了某些文件，那么这些文件将会被追踪，即使在 `.gitignore` 中配置了忽略它们
> 可以使用 `git rm --cached FILENAME` 命令来取消追踪这些文件

`.gitignore` 中使用正则表达式匹配文件

在 .gitignore 文件中，每一行的忽略规则的语法如下：

1. 空格不匹配任意文件，可作为分隔符，可用反斜杠转义
2. `#` 标识注释，可以使用反斜杠进行转义
3. 可以使用标准的 glob 模式匹配。所谓的 glob 模式是指 shell 所使用的简化了的正则表达式。
4. 以斜杠 "/" 开头表示目录；"/" 结束的模式只匹配文件夹以及在该文件夹路径下的内容，但是不匹配该文件；
      1. "/" 开始的模式匹配项目跟目录；
      2. 如果一个模式不包含斜杠，则它匹配相对于当前 `.gitignore` 文件路径的内容，如果该模式不在 `.gitignore` 文件中，则相对于项目根目录
5. "*" 通配多个字符
      - 使用两个星号"**" 表示匹配任意中间目录，比如 `root/**/file` 可以匹配 `root/file`, `root/dir1/file` 或 `root/dir1/dir2/file` ...
6. "?" 通配单个字符
7. "[]" 匹配任何 **一个** 列在方括号中的字符。比如 `[abc]` 表示 a 或 b 或 c；
      - 如果在方括号中使用短划线分隔两个字符，表示所有在这两个字符范围内的都可以匹配。比如 `[0-9]` 表示匹配所有 0 到 9 的数字，`[a-z]` 表示匹配任意的小写字母
8. "!" 表示不忽略(跟踪)匹配到的文件或目录，即要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号（!）取反
      - 如果文件的父目录已经被前面的规则排除掉了，那么对这个文件用 "!" 规则是不起作用的

??? info "不使用 .gitignore 文件"
    - [Excluding local files without creating a .gitignore file](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files#excluding-local-files-without-creating-a-gitignore-file)
    - 不太建议这个

## Trivial commands | TODO

> 基本都可以用 `-h` 查看手册

??? note "diff"
    - `git diff` 查看工作区和暂存区之间所有的文件差异

    > [CSDN - git diff](https://blog.csdn.net/qq_39505245/article/details/119899171?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522170001375316800225519804%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=170001375316800225519804&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-119899171-null-null.142^v96^pc_search_result_base4&utm_term=git%20diff&spm=1018.2226.3001.4187)

??? note "fetch & pull"
    - `git pull` = `git fetch` + `git merge`
    - 建议优先使用 `git fetch`，因为 `git pull` 会自动合并，可能会导致冲突
    - `pull`
        - `git pull` 会将远程仓库的内容拉取到本地
        - `git pull <remote>` 会将远程仓库的 `<remote>` 分支拉取到本地
        - `git pull <远程主机名> <远程分支名>:<本地分支名>` 会将远程仓库的 `<远程主机名>` 的 `<远程分支名>` 分支拉取到本地的 `<本地分支名>` 分支并合并 (e.g. `git pull origin main:version1`)
        - ...
    - `fetch` 操作与 `pull` 类似

    !!! success "一个较安全的拉取流程"
        ```bash
        $ git fetch origin main:tmp
        $ git diff tmp
        $ git merge tmp
        ```

??? note "clone"
    - `git clone <url>` 会将远程仓库克隆到本地
    - `git clone <url> <dir>` 会将远程仓库克隆到本地的 `<dir>` 目录下
    - `git clone <url> -b <branch>` 会将远程仓库的 `<branch>` 分支克隆到本地
    - `git clone <url> -b <branch> <dir>` 会将远程仓库的 `<branch>` 分支克隆到本地的 `<dir>` 目录下
    - `git clone <url> -b <branch> --single-branch` 会将远程仓库的 `<branch>` 分支克隆到本地，且只克隆该分支
    - `depth` 选项:
        - `git clone <url> --depth <depth>` 会将远程仓库克隆到本地，但是只克隆最近的 `<depth>` 个提交
    - `shallow` 选项:
        - `git clone <url> --shallow-since=<date>` 会将远程仓库克隆到本地，但是只克隆最近的 `<date>` 之后的提交
        - `git clone <url> --shallow-exclude=<revision>` 会将远程仓库克隆到本地，但是不克隆 `<revision>` 之前的提交
    ...

??? note "branch & checkout"
    - `branch`
        - `git branch` 或 `git branch -l` 列出本地分支
        - `git branch -r` 列出远程分支
        - `git branch -a` 列出本地分支和远程分支
        - `git branch <branch>` 创建分支
        - `git branch -d <branch>` 删除分支; `-D` 强制删除
        - `git branch -m <old> <new>` 重命名分支; `-M` 强制重命名
        - `git branch -u <remote>/<branch>` 设置本地分支跟踪远程分支
        - ...
    - `checkout`
        - `git checkout <branch>` 切换分支
        - `git checkout -b <branch>` 创建并切换到分支
        - `git checkout -b <branch> origin/<remote branch>` 创建并切换到分支，且跟踪远程分支
        - ...


<center><font face="JetBrains Mono" size=6 color=grey size=18>To Be Continued</font></center>
