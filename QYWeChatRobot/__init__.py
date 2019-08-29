# coding=utf-8
import requests
import base64
from hashlib import md5

"""
企业微信机器人的简单包装
方便命令行使用，快速发送消息
api documents: https://work.weixin.qq.com/help?person_id=1&doc_id=13376
"""


class WeChatRobot(object):
    def __init__(self, default_key):
        self.tag = "[WeChatRobot]"
        self.base_urls = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send"
        self.keys = dict(default_key=default_key)

    def add_key(self, key, val):
        self.keys[key] = val

    def _send_message(self, body, key):
        if not self.keys:
            print(self.tag, "send msg error, not found group")
            return

        params = dict(key=self.keys.get(key))
        resp = requests.post(url=self.base_urls, params=params, json=body)
        if resp.status_code == 200:
            print(self.tag, "send msg success!")
        else:
            print(self.tag, "send msg fail!, state code : {}".format(resp.status_code))
        return resp

    def send_text_message(self, content, mentioned_list=None, mentioned_mobile_list=None, key="default_key"):
        """
        :param content:
        :param mentioned_list:
        :param mentioned_mobile_list:
        :param key:
        :return:
        """
        body = {
            "msgtype": "text",
        }
        text = {
            "content": content
        }
        if mentioned_list and isinstance(mentioned_list, list):
            text.update(mentioned_list=mentioned_list)
        if mentioned_mobile_list and isinstance(mentioned_mobile_list, list):
            text.update(mentioned_mobile_list=mentioned_mobile_list)
        body.update(text=text)
        return self._send_message(body=body, key=key)

    def send_markdown_message(self, content, key="default_key"):
        """
        :param content: markdown content
        :param key:
        :return:
        """
        body = {
            "msgtype": "markdown",
            "markdown": {
                "content": content
            }
        }
        return self._send_message(body=body, key=key)

    def send_image_message(self, image, key="default_key"):
        """
        :param image: Image
        :param key:
        :return:
        """
        hash_md5 = md5()
        hash_md5.update(image)
        hash_md5 = hash_md5.hexdigest()
        body = {
            "msgtype": "image",
            "image": {
                "base64": base64.b64encode(image),
                "md5": hash_md5
            }
        }
        return self._send_message(body=body, key=key)

    def send_news_message(self, articles, key="default_key"):
        """
        :param articles: [{ "title" : "title", "description" : "description", "url" : "URL", "picurl" : "xxx" }]
        :param key:
        :return: response
        """
        body = {
            "msgtype": "news",
            "news": {
                "articles": articles
            }
        }
        return self._send_message(body=body, key=key)


def send_text_message(key, content, mentioned_list=None, mentioned_mobile_list=None):
    robot = WeChatRobot(key)
    return robot.send_text_message(content, mentioned_list, mentioned_mobile_list)


def send_markdown_message(key, content):
    robot = WeChatRobot(key)
    return robot.send_markdown_message(content)


def send_image_message(key, image):
    robot = WeChatRobot(key)
    return robot.send_image_message(image)


def send_image_message_by_file(key, image_file):
    robot = WeChatRobot(key)
    with open(image_file, "rb") as fp:
        image = fp.read()
        return robot.send_image_message(image)


def send_news_message(key, articles):
    robot = WeChatRobot(key)
    return robot.send_news_message(articles)
