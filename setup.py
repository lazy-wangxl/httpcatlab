#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='httpcatlab',
    version='0.6',
    packages=find_packages(),
    install_requires=[
        # 任何依赖项都在这里列出
        'httpcat-sdk'
    ],
    author='lazy-wangxl',
    author_email='xawangxiaolong@126.com',
    description='httpcatlab',
    license='MIT',
    keywords='httpcatlab',
    url='https://github.com/lazy-wangxl/httpcatlab',
    download_url='https://github.com/lazy-wangxl/httpcatlab',
    project_url='https://github.com/lazy-wangxl/httpcatlab',
    repository={
        "type": "git",
        "url": "https://github.com/lazy-wangxl/httpcatlab"
    }
)