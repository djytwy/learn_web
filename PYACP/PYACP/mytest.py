# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
# _user = "676534074@qq.com"
# _pwd  = "jykvjizcenopbcje"
# _to   = "676534074@qq.com"
#
# msg = MIMEText("Test")
# msg["Subject"] = "don't panic"
# msg["From"]    = _user
# msg["To"]      = _to
#
# try:
#     s = smtplib.SMTP_SSL("smtp.qq.com", 465)
#     s.login(_user, _pwd)
#     s.sendmail(_user, _to, msg.as_string())
#     s.quit()
#     print "Success!"
# except smtplib.SMTPException,e:
#     print "Falied,%s"%e

# a=[1,2,4,2,4,5,6,5,7,8,9,0]
# b={}
# b=b.fromkeys(a)
# c=tuple(b.keys())
# print c


# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print '%s %s():' % (text, func.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
#
# @log('execute')
# def now():
#     print '2013-12-25'
#
# if __name__ == '__main__':
#     now()

