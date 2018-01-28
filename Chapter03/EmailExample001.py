#! /usr/bin/python
# -*- coding: utf-8 -*-

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image  import MIMEImage
import email
from smtplib import SMTP

# 定义发送多部分的邮件信息
def make_mpa_msg():
    e = MIMEMultipart("alternative");
    text = MIMEText("Hello World")
    e.attach(text)
    html = MIMEText("""
    <H1>Hello World</H1>
    """)
    e.attach(html)
    return e

def make_img_msg(fn):
    try:
        with open(fn, "r") as f:
            e = MIMEImage(f.read(), f.name)
            e.add_header("Content-Dispositioin", "attachment;filename=%s" % f.name)
            return e
    except:
        return None

def send_email(from_addr, to_addr, content_msg):
    smtp = SMTP("smtp.python.is.cool")
    smtp.sendmail(from_addr, to_addr, content_msg)
    smtp.close()


def processmsg(entire_msg):
    body = ""
    msg = email.message_from_string(entire_msg)
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload()
                break
            else:
                body = part.get_payload(decode=True)
    else:
        body = msg.get_payload(decode=True)
    return body

if __name__ == "__main__":
    e = make_mpa_msg()
    e["From"] = "test@qq.com"
    e["To"] = "test@qq.com"
    e["Subject"] = "Test Email"
    send_email(e["From"], e["To"], e.as_string())

    e = make_img_msg("coach-head.jpg")
    e["From"] = "test@qq.com"
    e["To"] = "test@qq.com"
    e["Subject"] = "Test Email"
    send_email(e["From"], e["To"], e.as_string())
