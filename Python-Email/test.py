import mailSMTP

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

agent = mailSMTP.SMTPUser(from_addr, token)

# 1.Sending plain text test
agent.send_content(content_text, to_addr,
                   msg_subject=subject, msg_from=msg_from, msg_to=msg_to, log=False)
