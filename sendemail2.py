# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:26:55 2017

@author: sunjingjing
"""
    
import smtplib
import traceback
from email.header import Header
from email.mime.text import MIMEText
   # from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr,formataddr

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

user ='648877569@qq.com'
password='eszamthhwfpwbeij'
to_addr =['648877569@qq.com','sunjingjing789@163.com']
smtp_server ='smtp.qq.com'
content ='测试一下'

msg =MIMEText(content,'plain','utf-8')
msg['From'] = _format_addr('Frank的监控txy <%s>'% user)
msg['To'] = ";".join(to_addr)
msg['Subject'] = Header('kdjfkdjfkd','utf-8')

smtpObj = smtplib.SMTP(smtp_server,port=465)
smtpObj.login(user,password)
smtpObj.sendmail(user,to_addr,msg.as_string())
smtpObj.quit();
print('mail has been sent.')
