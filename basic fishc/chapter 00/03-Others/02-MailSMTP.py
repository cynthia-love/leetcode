# -*- coding: utf-8 -*-

# Author: Cynthia

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from sys import exit


def main():
    def mail(mail_name, mail_password):

        host, user, password = "smtp.126.com", mail_name + "@126.com", mail_password
        sender, receivers = user, [user, "xxx@126.com"]

        message = MIMEMultipart()
        # 注意收件人是多个的时候, To得用","给拼起来
        message['From'], message['To'] = sender, ",".join(receivers)
        message['Subject'] = "这里是标题"

        # *************************************************************************
        # 普通文本正文
        p1 = MIMEText("这里是普通正文", "plain", "utf-8")
        message.attach(p1)

        # *************************************************************************
        # html正文和图片正文，注意， 图片正文依赖于html正文
        html = """
            <p>这里是html部分,并演示图片</p>
            <p><img src="data:image/jpg;base64,{0}"
            """
        try:
            with open("data/data.jpg", "rb") as file:
                img_mime = MIMEText(file.read(), "base64", "utf-8")
        except:
            img_mime = None
            print("未找到图片!")
            exit(1)

        p2 = MIMEText(html.format(img_mime.get_payload()), "html", "utf-8")
        # 注意正文部分只能有一个, 如果没有显示地声明后面这个是附件,会把之前attach的顶成附件
        message.attach(p2)

        # *************************************************************************
        # 图片附件
        p3 = img_mime
        p3['Content-Type'] = "application/octet-stream"
        p3['Content-Disposition'] = "attachment;filename=view.jpg"
        message.attach(p3)

        # *************************************************************************
        # 其他格式附件一样的上传方法, 也是要先以base64/utf-8读取
        try:
            with open("00-CrawlerElearning.py", "rb") as file:
                p4 = MIMEText(file.read(), "base64", "utf-8")
        except:
            p4 = None
            print("未找到文件!")
            exit(1)

        p4['Content-Type'] = "application/octet-stream"
        p4['Content-Disposition'] = "attachment;filename=test.py"
        message.attach(p4)

        try:
            smtp = SMTP(host, 25)
            smtp.login(user, password)
            smtp.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功！")
        except:
            print("邮件发送失败！")
            exit(1)

    mail("XXXXXX", "XXXXXX")


if __name__ == '__main__':
    main()
