#! /usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide configure file management service in i18n environment.

Authors: zhuhongquan
Date:    2019/9/6
"""
import click


@click.command()
@click.option('--count', default=1, help='Number of greeting.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def main(count, name):
    for x in range(count):
        click.echo('Hello %s !' % name)


if __name__ == '__main__':
    main()
