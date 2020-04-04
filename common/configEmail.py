
import smtplib,time
from email.mime.text import MIMEText,MIMENonMultipart
from email.mime.multipart import MIMEMultipart
from email.header import Header

t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

class sendEmail(object):
    def __init__(self,sender,pwd,smtpserver,receiver):
        self.sender = sender
        self.pwd = pwd
        self.smtpserver = smtpserver
        self.receiver = receiver
        # 实例化smtp类
        self.sed = smtplib.SMTP()
        # 连接smtp服务器
        self.sed.connect(self.smtpserver)
        # 登录邮箱
        self.sed.login(self.sender, self.pwd)
    # 发送文本内容
    def sendContent(self,subject,context):
        context = context+t
        msg = MIMEText(context,'plain','utf-8')
        msg['Subject'] = Header(subject,'utf-8')
        msg['From'] = self.sender
        msg['To'] = self.receiver
        try:
            # 设置发件人，收件人，邮件内容
            self.sed.sendmail(self.sender,self.receiver,msg.as_string())
        except Exception as msg:
            print(msg)
            print('邮件发送失败！')
        else:
            print('邮件发送成功。')
        finally:
            self.sed.quit()
    # 将邮件内容以HTML方式发送
    def sendHtmlContent(self,subject,html):
        msg = MIMEText(html,_subtype='html',_charset='utf-8')
        msg['Subject'] = Header(subject,'utf-8')
        msg['From'] = self.sender
        msg['To'] = self.receiver
        try:
            # 设置发件人，收件人，邮件内容
            self.sed.sendmail(self.sender,self.receiver,msg.as_string())
        except Exception as msg:
            print(msg)
            print('邮件发送失败！')
        else:
            print('邮件发送成功。')
        finally:
            self.sed.quit()
    # 使用附件形式发送文件
    def sendAccessory(self,subject,html):
        body = MIMEText(_text='详见附件',_subtype='plain',_charset='utf-8')
        msg = MIMEMultipart()
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = self.sender
        msg['To'] = self.receiver
        msg.attach(body)
        # 添加附件
        att = MIMEText(_text = html, _subtype='html', _charset='utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment; filename={0}.html'.format(subject)
        msg.attach(att)
        try:
            # 设置发件人，收件人，邮件内容
            self.sed.sendmail(self.sender, self.receiver, msg.as_string())
        except Exception as e:
            print(e)
            print('邮件发送失败！')
        else:
            print('邮件发送成功。')
        finally:
            self.sed.quit()

if __name__ == '__main__':
    html_file = r'..\report\result.html'
    with open(html_file,'rb') as fp:
        mail_body = fp.read()
    sender = 'qw20140729@163.com'
    passwd = 'AMPCVEKPUVAOIYVI'
    smtpserver = 'smtp.163.com'
    toemail = 'qw20140729@163.com'
    sel = sendEmail(sender,passwd,smtpserver,toemail)
    context = '测试结果。。。'
    subject = 'testresult'
    # sel.sendContent(subject,context)
    # sel.sendHtmlContent(subject,mail_body)
    sel.sendAccessory(subject,mail_body)