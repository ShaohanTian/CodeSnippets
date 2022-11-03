import re
import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.utils import parseaddr, formataddr


def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def convert_path(path):
    seps = r'\/'
    sep_other = seps.replace(os.sep, '')
    return path.replace(sep_other, os.sep) if sep_other in path else path


class SMTPUser():

    """Sending mail with SMTP service"""
    global SMTP_PORT, SMTP_SERVER

    SMTP_SERVER = {'163': 'smtp.163.com',
                   'qq': 'smtp.qq.com',
                   'foxmail': 'smtp.qq.com',
                   'gmail': 'smtp.163.com',
                   'hotmail': 'smtp.office365.com'}
    SMTP_PORT = {'163': 25, 'qq': 587, 'gmail': 465,
                 'hotmail': 587, 'foxmail': 587}

    def __init__(self, from_addr, token):
        self.from_addr = from_addr
        self.token = token

    def _connect(self, from_type, log):
        # print(SMTP_SERVER[from_type], SMTP_PORT[from_type])
        server = smtplib.SMTP(SMTP_SERVER[from_type], SMTP_PORT[from_type])
        if log:
            server.set_debuglevel(1)
        server.login(self.from_addr, self.token)
        self.server = server
        print("********** SMTP connected **********")

    def _disconnect(self):
        self.server.quit()
        print("********** Message sent, SMTP disconnected! **********")

    def add_frominfo(self, msg_subject='', msg_from='', msg_to=''):
        self.msg['From'] = format_addr(
            msg_from + ' ' + '<%s>' % self.from_addr)
        self.msg['To'] = format_addr(msg_to + ' ' + '<%s>' % self.to_addr[0])
        self.msg['Subject'] = Header(msg_subject, 'utf-8').encode()

    def send_content(self, content, to_addr, type='plain', msg_subject='', msg_from='', msg_to='', log=False):
        self.to_addr = to_addr
        from_server_type = re.findall(r'@(.*)\.com', self.from_addr)
        self._connect(from_server_type[0], log)
        self.msg = MIMEText(content, type, 'utf-8')
        self.add_frominfo(msg_subject, msg_from, msg_to)
        print("********** Sending ...... **********")
        self.server.sendmail(self.from_addr, to_addr, self.msg.as_string())
        self._disconnect()

    def send_multi(self, content, attach, to_addr, type='plain', msg_subject='', msg_from='', msg_to='', log=False):
        self.to_addr = to_addr
        from_server_type = re.findall(r'@(.*)\.com', self.from_addr)
        self._connect(from_server_type[0], log)

        print("********** Sending ...... **********")
        self.msg = MIMEMultipart()
        self.add_frominfo(msg_subject, msg_from, msg_to)
        # add text
        self.msg.attach(MIMEText(content, type, 'utf-8'))
        # add attachment
        for idx, path in enumerate(attach):
            path = convert_path(path)
            with open(path, 'rb') as f:
                att = MIMEText(f.read(), 'base64', 'utf-8')
                att["Content-Type"] = 'application/octet-stream'
                att["Content-Disposition"] = 'attachment; filename=' + \
                    os.path.split(path)[1]
                att['Content-ID'] = '<' + str(idx) + '>'
                att["X-Attachment-Id"] = str(idx)
                self.msg.attach(att)

        self.server.sendmail(self.from_addr, to_addr, self.msg.as_string())
        self._disconnect()


if __name__ == '__main__':

    from_addr = 'shaohan.tian@foxmail.com'
    to_addr = ['shaohan.tian@hotmail.com', 'tianshaohan@yeah.net']
    token = 'ubaadytmiokrjfdd'
    subject = 'SMTPUser test'
    msg_from = 'Shaohan Tian'
    msg_to = 'You'
    content_text = """No Man is an Island"""
    content_html = '<html><body><h1>Hello</h1>' + \
        '<p>send by <a href="http://www.python.org">Python</a>...</p>' + '</body></html>'
    content_html_cid = '<html><body><h1>Hello</h1>' + \
        '<p><img src="cid:0"></p>' + '</body></html>'
    attach = [r"D:\360yun\360yun\code\code_myself\code_mail\python_logo.png",
              r"D:\360yun\360yun\code\code_myself\code_mail\mail_text.txt"]

    agent = SMTPUser(from_addr, token)

    # # 1.Sending plain text test
    # agent.send_content(content_text, to_addr,
    #                    msg_subject=subject, msg_from=msg_from, msg_to=msg_to, log=True)

    # # 2.Sending html test
    # agent.send_content(content_html, to_addr, type='html',
    #                    msg_subject=subject, msg_from=msg_from, msg_to=msg_to)

    # # 3.Sending text with attachments test
    # agent.send_multi(content_text, attach, to_addr, type='plain',
    #                  msg_subject=subject, msg_from=msg_from, msg_to=msg_to)

    # 4.Sending html and using attachments cid
    agent.send_multi(content_html_cid, attach, to_addr, type='html',
                     msg_subject=subject, msg_from=msg_from, msg_to=msg_to)

