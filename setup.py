# coding=utf-8
from setuptools import setup, find_packages

setup(
    name="QYWeChatRobot",
    version='1.1',
    description='企业微信机器人封装',
    author='qxsugar',
    py_modules=['QYWeChatRobot'],
    author_email='qxsugar@gmail.com',
    install_requires=[
        "requests>=2.18.4"
    ],
    packages=find_packages(),
)
