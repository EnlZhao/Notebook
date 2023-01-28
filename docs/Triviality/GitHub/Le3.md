# Getting started with Git

## Set your username

## Caching credentials

## Git passordwords

## macOS Keychain credentials

## Git workflows

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
    * 现有远程名称（如 origin）
    * 远程的新名称（如 destination）

### 删除远程仓库

* 使用 `git remote rm` 命令从存储库中删除远程 URL。
* 该命令采用一个参数：
    * 远程名称（例如 destination）

> 从存储库中删除远程 URL 只会取消本地和远程存储库的链接。 它不会删除远程存储库

## Associate text editors



## Handle line endings

## Ignoring files
