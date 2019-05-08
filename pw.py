# -*- coding: utf-8 -*-

import sys
import pyperclip
passwords={
            '数据库':'shangde2018',
            '万能':'12345678',
            '鹰眼':'SunLands7109'
            }

if len(sys.argv)<2:
    print("请使用以下方式: 'python aa.py [账号]' --输入后将会获取密码到剪切板")
    sys.exit()

account=sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('已经复制当前账号密码到剪切板')
else:
    print('没有保存当前账号密码信息')
