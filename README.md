# pw
Interesting convenient password paste tools

## 前提:
1.该脚本是在看python编程快速上手-让繁琐工作自动化的书籍上看到的一个有趣并且还算实用的脚本,分享一下<br>
2.脚本作用就是运行时候输入需要的账号昵称,运行完会自动识别昵称对应的密码到剪切板黏贴使用<br>
3.在当今拥有这么多账号密码忘记是经常的事情(虽然有强大的密码找回),这工具在这时候便能派上用场<br>

## 脚本:
import sys<br>
import pyperclip<br>
passwords={
            '数据库':'shangde***',
            '万能':'12345678',
            '鹰眼':'SunLands***'
            }

if len(sys.argv)<2:<br>
    print("请使用以下方式: 'python aa.py [账号]' --输入后将会获取密码到剪切板")<br>
    sys.exit()<br>
    
account=sys.argv[1]<br>

if account in passwords:<br>
    pyperclip.copy(passwords[account])<br>
    print('已经复制当前账号密码到剪切板')<br>
else:<br>
    print('没有保存当前账号密码信息')<br>

## 脚本配置:
可在posswords字典添加更多的账号信息,该文件保存为pw.py(名字自行更改)<br>
然后在任何path环境变量下的路径比如在桌面,建立pw名字的文本文档(名字可改),写入以下代码:<br>

```@python C:\Users\wrath\Desktop\个人项目\pw.py %*<br>
```@pause<br>
```
路径是自己保存的py文件路径,然后另存为后缀bat的可执行文件<br>
(如果路径含有中文一定编码,另存为的时候编码选择ANSI,否则会乱码)<br>
然后就可以使用了<br>

## 脚本使用:
使用时候按win+R,在运行里面写上 pw 数据库 (即:文本文档文件名 账号昵称),按enter会弹出命令行显示:<br>

已经复制当前账号密码到剪切板<br>
请按任意键继续. . .<br>

然后就可以黏贴使用了<br>
