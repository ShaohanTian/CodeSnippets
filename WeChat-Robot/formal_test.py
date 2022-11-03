import werobot
import base64
from werobot.replies import TextReply, ImageReply, VoiceReply, SuccessReply
from werobot.replies import ArticlesReply, Article, SuccessReply, MusicReply

# 输入微信公众平台请求凭证
robot = werobot.WeRoBot(token='tsh980509')         # 写入服务器配置填写的 Token

def cal(str):
    try:
        result = str(eval(str))

    except:
        result = 'Please try again！'
    return result

def string(ss):
    if ss[0:7] == 'encode ':
        result = base64.b64encode(ss[7:].encode())
        result = str(result, encoding = "utf-8")
    elif ss[0:7] == 'decode ':
        result = str.encode(ss[7:])
        result = base64.b64decode(result).decode()
    else:
        result = '请在需要编码的文字前添加encode ，需要解码的文字前添加decode '
    return result


# @robot.text 修饰的 Handler 只处理文本消息
@robot.text
def reply_text(message):
    print(message.content)



    # if len(re.findall(r'music|孤勇者|陈奕迅', message.content)) > 0:

    #     reply = MusicReply(message=message,
    #         title='孤勇者',
    #         description='陈奕迅新作',
    #         url="https://shaohan-yun.oss-cn-beijing.aliyuncs.com/my_blog/陈奕迅 - 孤勇者.mp3")
    # else:

    #     reply = TextReply(message=message, content=message.content)
    return string(message.content)
    # return reply

robot.config.update(
    SERVER="auto",
    HOST="0.0.0.0",
    PORT="80",
    SESSION_STORAGE=None,
    APP_ID="wxa975f27840138056",
    APP_SECRET="b692e1a76e43316fd768724939345999",
    ENCODING_AES_KEY="XWbRw4lacZrNdR4C78YS0hVDovuzGuo5NePjxO502t3"
)

robot.run()



# print(string('encode 同事'))
# print(string('decode 5ZCM5LqL'))
# print(string('fjsljflsdf'))


# print(string(b'ZW5jb2RlIOWQjOS6iw=='))


