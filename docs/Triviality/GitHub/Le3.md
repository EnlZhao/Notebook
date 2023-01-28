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

!!! warning "Troubleshooting: Remote origin already exists"
     此错误消息表示尝试添加的远程与本地仓库远程名称相同
     ```bash
     $ git remote add origin https://github.com/octocat/Spoon-Knife.git
     > fatal: remote origin already exists.
     ```

     ??? question "Solution"
         * 对新远程使用不同名称
         * 在添加新远程时，重命名现有远程仓库
         * 在添加新远程前，删除现有远程仓库

### 更改远程仓库 URL



## Associate text editors

## Handle line endings

## Ignoring files
