# Niputv动漫视频网



### 项目介绍
该视频网本来是我自己开发的一个视频网站 在线上运作了两个月 由于缺乏资金 自己也没有时间去继续完善功能因此荒废
- 该项目由于后期更新到一半终止 后台并非完全开发完成 暂时只供参考 如果需要使用需要自行完善



### 网站首页（右键打开图片有大图）
- 首页
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/index1.jpg)
- 分区页面
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/index2.jpg)
- 细分分区
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/index3.png)


### 技术层
[python3]
- 该项目使用elasticsearch储存视频记录 并使用elasticsearch作为视频id 部分接口和功能使用了redis
- 基于python flask tornado jinja jquery 播放器基于h5video标签开发 使用数据库为Mariadb 视频储存于七牛云存储（包括视频的转码 储存 调用 删除 详情见项目内的自创七牛orm模块）
- 登录基于flask-login



### 关于视频播放器
- 播放器基于H5开发 是本项目的专用播放器 使用文档见子项目内
https://github.com/ShenVi/Niputv-H5player


### 网站开发
- 前端 我
- 后端 我
- 设计 我
- 架构 我
行了不讲了 自己体会吧


### 网站功能
- 稿件类 - 上传 编辑视频资料 删除视频
- 视频播放类 - 视频点赞 视频分享 视频评论 播放量统计 视频举报
- 番剧类 - 追番 取消追番 番剧推送
- 后台 - 审核视频 上传视频 修改指定视频资料 下架视频 上传番剧 编辑番剧 修改番剧资料 上传番剧剧集 修改番剧集数 创建用户账户 删除用户账户 管理用户账户
- 账户类 - 注册 登录 修改个人资料 上传头像
- 评论 - 发表评论 回复评论 删除评论 查看评论 举报评论
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/project.png)

### 项目目录结构
- niputv 主站
- niputv-account 账户系统
- niputv-activity 分析（统计网站播放量 浏览量 并且进行数据提交更新）
- niputv-creation 用户个人创作中心（上传视频 编辑视频 删除视频）
- niputv-management 网站后台
- niputv-space 用户空间
- niputv-templates 网站模板


### 更多图片介绍（右键打开图片可看大图）

- 登录页面
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/login2.jpg)

- 视频播放页面
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/playpage1.jpg)
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/playpage2.jpg)

#### 投稿类
- 视频投稿页面
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/uploadvideo.png)

#### 管理
- 视频管理页面
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/videoadmin.png)

#### 功能
- 视频评论区 以及 部分视频功能
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/comment.png)

#### 番剧类
- 番剧详情页
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/bangumi1.jpg)
番剧播放页
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/bangumiplay.jpg)

### 后台
- 发布番剧
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/uploadbangumi.jpg)
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/uploadbangumi2.png)

番剧资料
![Image text](https://github.com/ShenVi/Niputv/blob/master/img/bangumiinfo.png)