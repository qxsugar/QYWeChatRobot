企业微信机器人接口封装
===================

企业微信提供了微信群机器人
用微信机器人来做警报系统也是个不错的选择。
特别是日常监控

![企业机器人API](https://work.weixin.qq.com/help?person_id=1&doc_id=13376)

企业微信已经提供了很好的api给我们了。
有时候运维监控要调用这些接口不是那么方便。
所以用python写了一层包转发消息。
方便bash调用

### 安装
> pip install git+https://github.com/qxsugar/QYWeChatRobot.git

### 使用
> python -c 'from QYWeChatRobot import send_text_message; send_text_message("你的key", "ping")'
> python -c 'from QYWeChatRobot import send_markdown_message; send_markdown_message("你的key", "### ping\n > cmd")'
> python -c 'from QYWeChatRobot import send_image_message; send_image_message("你的key", "图片二进制")'
> python -c 'from QYWeChatRobot import send_image_message_by_file; send_image_message_by_file("你的key", "图片路径")'
> python -c 'from QYWeChatRobot import send_news_message; send_news_message("你的key", python字典结构)'


### wx_robot 提供的接口
1. send_text_message            # 发送文本消息
2. send_markdown_message        # 发送markdown消息
3. send_image_message           # 发送图片 < 2M
4. send_image_message_by_file   # 发送文件图片 图片要 < 2M
5. send_news_message            # 发送图文类型

### key哪里来
> 企业微信群，点击右上角，添加群机器人，copy url，url最后有个key=xxx

