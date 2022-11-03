from imap_tools import MailBox, AND, MailBoxTls, MailBoxUnencrypted

# 输入邮件地址, 口令和POP3服务器地址:
# email = '1185725270@qq.com'
# password = 'ubaadytmiokrjfdd'
# imap_server = 'imap.qq.com'

email = 'shaohan.tian@hotmail.com'
password = 'tsh980509'
imap_server = 'outlook.office365.com'

## 使用163邮箱需要修改imap-tools模块

# Get date, subject and body len of all emails from INBOX folder
with MailBox(imap_server).login(email, password) as mailbox:
    for msg in mailbox.fetch():
        print(f'''************
msg.uid      -> {msg.uid}
msg.date     -> {msg.date}
msg.flags    -> {msg.flags}
msg.date_str -> {msg.date_str}
msg.subject  -> {msg.subject},
msg.from_    -> {msg.from_}
msg.to       -> {msg.to}
msg.text     -> {msg.text},
msg.html     -> {msg.html},
msg.size     -> {msg.size}
len(msg.text or msg.html) -> {len(msg.text or msg.html)}
************
''')
