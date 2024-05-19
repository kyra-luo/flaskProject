from flask import render_template
from flask_mail import Message
from app import mail
from app.blueprint import main
from flask import current_app

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    with current_app.app_context():
        current_app.logger.debug("Connecting to mail server")
    mail.send(msg)

# 修改 send_password_reset_email 函数
def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('Reset Your Password',
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token, errors={}))



# seding email function
def send_welcome_email(user):
    # 构建邮件内容
    subject = 'Welcome to Our Website'
    sender = current_app.config['ADMINS'][0]
    recipients = [user.email]
    text_body = render_template('email/welcome.txt', user=user)
    html_body = render_template('email/welcome.html', user=user)

    # 发送邮件
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    with current_app.app_context():
        mail.send(msg)
