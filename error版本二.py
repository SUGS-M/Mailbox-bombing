
from smtplib import SMTP_SSL
from email.mime.text import MIMEText#该模块是python自带；注意文件名不能是email
from email.header import Header

#第三方服务（qq）
mail_host = 'smtp.163.com'
mail_user = '18599141728@163.com' #账号
mail_pws = 'ju187369' #授权码

#登录
smtp = SMTP_SSL(mail_host,465)  #实例化
smtp.ehlo(mail_host)
smtp.login(mail_user,mail_pws)#登录

#我和对方的邮件地址
my_mail = '18599141728@163.com' #自己打的邮箱地址
her_mail = '2953126974@qq.com' #对方的邮箱地址

#写入的内容
cont = '你好我是HV，我来自外星球！'
#标题
title = '来着地球的HV'

#内容格式化
for i in range(10): #向目标发送10个邮箱
    msg = MIMEText(cont,'plain','UTF-8') #plain为txt格式，如果直接写txt的话，会被检测为垃圾邮箱
    msg['Subject'] = Header(title,'UTF-8')
    msg['From'] = my_mail #这里有填写您的邮箱地址格式，对方才会知道发件人是谁，要不然对方默认为（无发件人）
    msg['To'] = '我的好友' #这个要注意！这里只能填字符串，如果填其他的数据类型就会报错！
    smtp.sendmail(my_mail,her_mail,msg.as_string())
    # smtp.quit()

smtp.quit() #关闭SMTP，邮箱信息传输

'''
地址：https://blog.csdn.net/weixin_33721427/article/details/92368887?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~aggregatepage~first_rank_ecpm_v1~rank_v31_ecpm-1-92368887.pc_agg_new_rank&utm_term=MIMEText+python+%E5%AE%89%E8%A3%85&spm=1000.2123.3001.4430
'''


'''
问题一：email模块  python自带的；但是文件名不能是email
问题二:can't open file '<unprintable file name>': [Errno 2] No such file or directory
地址：https://blog.csdn.net/LaoYuanPython/article/details/103788827
'''