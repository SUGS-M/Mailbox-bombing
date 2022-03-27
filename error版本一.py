# smtp =>simple mail transfer protocol  简单邮件传输协议
import smtplib
import email  # 文件名不可以和引入的库同名
from email.mime.image import MIMEImage  # 图片类型邮件
from email.mime.text import MIMEText  # MIME 多用于邮件扩充协议
from email.mime.multipart import MIMEMultipart  # 创建附件类型

HOST = 'smtp.qq.com'  # 调用的邮箱借借口
SUBJECT = '今天是2018年八月10日，是谁18岁生日'  # 设置邮件标题
FROM = '1468630684@qq.com'  # 发件人的邮箱需先设置开启smtp协议
TO = 'hsiangshuai@163.com,1468630684@qq.com'  # 设置收件人的邮箱（可以一次发给多个人）
message = MIMEMultipart('related')  # 邮件信息，内容为空  #相当于信封##related表示使用内嵌资源的形式，将邮件发送给对方
# 发送邮件主体到对方邮箱，
# 参数  1.内容必须是字符串
# 2.内容形式，文本类型默认为plain
# 3.内容编码使用utf-8
# message_html=MIMEText('shuai123 消灭不开行','plain','utf-8')
# 将邮件内容，装入邮件信息中
message_html = MIMEText('<h1 style="color:red；font-size:100px">好好学习，天天向上</h1><img src="cid:small">', 'html', 'utf-8')
message.attach(message_html)
'''
# ===========发送图片-=============
image_data = open('1.gif', 'rb')
message_image = MIMEImage(image_data.read())
# 关闭刚才打开的文件
image_data.close()
# (222)
message_image.add_header('Content-ID', 'small')
# 添加图片文件到邮件信息中去
message.attach(message_image)
# (333)
message_image = MIMEText(open('1.gif', 'rb').read(), 'base64', 'utf-8')
message_image['Content-disposition'] = 'attachment;filename="happy.gif"'
message.attach(message_image)
# ===========将xlsx文件作为内容发送到对方的邮箱读取excel，rb形式读取，
# ==对于MIMEText()来说默认的编码形式是base64 对于二进制文件来说没有设置base64，会出现乱码==========
message_xlsx = MIMEText(open('table.xlsx', 'rb').read(), 'base64', 'utf-8')
# 设置文件在附件当中的名字
message_xlsx['Content-Disposition'] = 'attachment;filename="test1111.xlsx"'
message.attach(message_xlsx)
'''
# 设置邮件发件人
message['From'] = FROM
# 设置邮件收件人
message['TO'] = TO
# 设置邮件标题
message['Subject'] = SUBJECT
# 获取江建有奖传输协议证书
email_client = smtplib.SMTP_SSL()
email_client.connect(HOST, '465')
# 设置发送域名，端口465
result = email_client.login(FROM, 'rehotdvftldxgfdf')  # qq
# result=email_client.login(FROM,'xs147258')#网易163


print('登录结果', result)

email_client.sendmail(from_addr=FROM, to_addrs=TO.split(','), msg=message.as_string())
# 关闭邮件发送客户端
email_client.close()