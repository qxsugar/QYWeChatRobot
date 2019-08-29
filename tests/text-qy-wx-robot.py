import unittest
from QYWeChatRobot import *


class RobotTest(unittest.TestCase):
    key = "xxxx"

    def test_send_text_message(self):
        resp = send_text_message(key=self.key, content="ping")
        self.assertEqual(resp.json().get('errcode'), 0)

    def test_send_images_message(self):
        resp = send_image_message_by_file(key=self.key, image_file="tests/1.jpg")
        self.assertEqual(resp.json().get('errcode'), 0)

    def test_send_markdown_message(self):
        resp = send_markdown_message(key=self.key, content="### title \n > ls ")
        self.assertEqual(resp.json().get('errcode'), 0)

    def test_send_news_message(self):
        data = [
            {
                "title": "title",
                "description": "description",
                "url": "http://www.google.com",
                "picurl": "https://p.ssl.qhimg.com/dmfd/400_300_/t0120b2f23b554b8402.jpg"
            },
            {
                "title": "title2",
                "description": "description2",
                "url": "http://www.google.com",
                "picurl": "https://p.ssl.qhimg.com/dmfd/400_300_/t0120b2f23b554b8402.jpg"
            }
        ]
        resp = send_news_message(key=self.key, articles=data)
        self.assertEqual(resp.json().get('errcode'), 0)


if __name__ == '__main__':
    unittest.main()
