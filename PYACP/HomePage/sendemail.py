# -*- coding: utf-8 -*-
from HomePage.models import EmailVerifyRecord
from random import Random
from PYACP import settings
from django.core.mail import send_mail


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGg1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email):
    code = random_str(16)
    record = EmailVerifyRecord.objects.create(send_email=email, code=code)
    record.save()
    email_title = "PYACP注册验证"
    email_body = "点击下面链接激活账号：http://127.0.0.1:8000/email?email={0}".format(code)
    send_mail(email_title, email_body, settings.EMAIL_FROM, [email])


def send_findpassword_email(email, username, newpassword):
    email_title = "PYACP找回密码"
    email_body = "您好，您在PYACP注册的账号：{0}，新密码为：{1}".format(username, newpassword)
    send_mail(email_title, email_body, settings.EMAIL_FROM, [email])


