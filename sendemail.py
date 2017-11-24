# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:40:47 2017

@author: sunjingjing
"""

#import sys,os,re ,urllib
import smtplib
import traceback
#from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from urllib.parse import urlparse

def sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password):
    """
    @subject:邮件主题
    @msg:邮件内容
    @toaddrs:收件人的邮箱地址
    @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
    @pasword:发信人的授权码
    """
    mail_msg =MIMEMultipart()
    if not isinstance(subject,str):
        subject = str(subject,'utf-8')
    mail_msg['Subject'] = subject
    mail_msg['From'] = fromaddr
    mail_msg['To'] = ";".join(toaddrs)
    mail_msg['Msg'] = msg
    try:
        s = smtplib.SMTP_SSL(smtpaddr,465)
       ## s.connect(smtpaddr) #连接smtp服务器
        s.set_debuglevel(1)
        s.login(fromaddr,password) #登陆邮箱
        s.sendmail(fromaddr,toaddrs,mail_msg.as_string()) #发送邮件
        s.quit()
        print('email has been send')
    except Exception as e:
        print('Error:unable to send email')
    print (traceback.format_exc())
        
if __name__=='__main__':
    print ('ok')
    fromaddr = '648877569@qq.com'
    smtpaddr ='smtp.qq.com'
    toaddrs = ['648877569@qq.com','sunjingjing789@163.com']
    subject = '测试邮件'
    password = 'eszamthhwfpwbeij'
    msg ='测试一下'
    sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password)
        
    
    