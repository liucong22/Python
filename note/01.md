- git 将代码提交到远程分支上
```
# 如没有，建立本地仓库
git init

# 如没有，有需要，建立本地分支
git branch [branch_name]

# 切换到指定分支
git checkout

# 将代码提交到本地仓库
git add .
git commit -m "practice_day01"

# 本地代码提交到远程仓库上
git push -u origin [branch_name]
```
- git 将分支代码合并到master
```
# 在分支路径下切换到主干
git checkout master

# pull远程master的代码
git pull origin master

# 如有冲突，手动解决，没有则合并
git merge [branch_name]

# 推送到远程master
git push origin master

# 删除分支
git push origin --delete [branch_name]

```
- git 提交时遇到的问题
```
# 提交时意外终止，再次提交时锁定文件未解除，无法继续提交，需要手动删除锁
del .git\index.lock   // windows
rm -f ./.git/index.lock    // linux
```
- 查看分支
```
# 查看分支
git branch

# 查看分支详细信息
git branch -v

# 查看分支与远程的关联
git branch -vv

# 查看所有分支（本地和远程）
git branch -a
```