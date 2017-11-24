# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:03:11 2017

@author: sunjingjing
"""

#qq邮箱
from email.mime.text import MIMEText
msg = MIMEText('hello,send by Python...','plain','utf-8')

from_addr  = '648877569@qq.com'

password = 'eszamthhwfpwbeij'  #密码是启用smtp的 授权码，163的授权码是自己设置的1qaz2wsx

to_addr = ['sunjingjing789@163.com','648877569@qq.com','sun_jingjing@founder.com']

smtp_server = 'smtp.qq.com'

import smtplib
server =smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit
print('done')


"""
#163邮箱
from email.mime.text import MIMEText
msg = MIMEText('中文试试','plain','utf-8')

from_addr  = 'sunjingjing789@163.com'

password = '1qaz2wsx'  #密码是启用smtp的 授权码，163的授权码是自己设置的1qaz2wsx

to_addr = ['sunjingjing789@163.com','648877569@qq.com']

smtp_server = 'smtp.163.com'

import smtplib
server =smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit
print('done')
"""