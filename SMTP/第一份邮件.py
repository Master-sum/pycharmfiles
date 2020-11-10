"""
作者   ：bjx
创建时间   ：2020/11/10  4:50 下午 
文件名称   ：第一份邮件.PY
开发工具   ：PyCharm
"""
#第一份邮件
import smtplib
from email.mime.text import MIMEText
msg = MIMEText('这是我的第一份邮件')
msg['Subject'] = 'An Email Alert'
msg['']