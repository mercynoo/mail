from flask import Flask, render_template
from flask.ext.mail import Mail,Message
import os
'''
$ set MAIL_USERNAME=<Gmail username>
$ set MAIL_PASSWORD=<Gmail password>
'''

app = Flask(__name__)
####SMTP server config
app.config['MAIL_SERVER'] = 'smtp.163.com' #电子邮件服务器的地址
app.config['MAIL_PORT'] = '25'   #邮箱服务器的端口
app.config['MAIL_USE_TLS'] = True  #启用安全传输
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  #邮件账户用户名,已定义环境变量
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  #邮件账密码,已定义环境变量


mail = Mail(app)

@app.route('/')
def index():
    msg = Message('主题',sender=os.environ.get('MAIL_USERNAME'),recipients=['zhaoxingnan@kuaiqiangche.com'])
    msg.body = '文本 body'
    msg.html = '<b>测试flask发送邮件</b>'
    mail.send(msg)

    return '<h1>邮件发送成功</h1>'


if __name__ == '__main__':
    app.run(debug=True)
