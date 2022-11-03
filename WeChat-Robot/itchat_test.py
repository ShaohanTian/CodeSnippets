
import re
import werobot
from werobot.replies import TextReply, ImageReply, VoiceReply, SuccessReply
from werobot.replies import ArticlesReply, Article, SuccessReply, MusicReply


# 输入微信公众平台请求凭证
robot = werobot.WeRoBot(token='tsh980509')         # 写入服务器配置填写的 Token


@robot.image
def img(message):
    print('*'*10)
    reply = ImageReply(message=message, media_id='GRYfT6zPTkXQMwy9FYdIw8RbJrsQHRaH8jAdDNV2_IfQhfuo_xU2iGViUnPF4ZCR')
    return reply

# @robot.text 修饰的 Handler 只处理文本消息
@robot.text
def reply_text(message):
    print(message.content)

    if len(re.findall(r'music|孤勇者|陈奕迅', message.content)) > 0:

        reply = MusicReply(message=message,
            title='孤勇者',
            description='陈奕迅新作',
            url="https://shaohan-yun.oss-cn-beijing.aliyuncs.com/my_blog/陈奕迅 - 孤勇者.mp3")
    else:

        reply = TextReply(message=message, content=message.content)
        # return cal(message.content)
    return reply


@robot.voice
def reply_voice(message):

    print('*'*10)
    reply = TextReply(message=message, content=message.recognition)
    # print(message.media_id)
    # print(message.format)
    return reply


@robot.video
def reply_video(message):
    reply = ArticlesReply(message=message)
    article = Article(
        title="WeRoBot",
        description="WeRoBot是一个微信机器人框架",
        img="https://mmbiz.qpic.cn/mmbiz_jpg/UiaMPvgzg0NHAI2Jga36WpL6pIccUEUwb1XQPcunKWmDPMC8HezqvGFsk6KvwUhLj0dRlntQiaYyibrL6baUXia9jA/0?wx_fmt=jpeg",
        url="https://github.com/whtsky/WeRoBot"
    )
    reply.add_article(article)
    # print('*'*10)
    # print(message.media_id)
    # print(message.thumb_media_id)
    return reply

# @robot.filter(re.compile("music"), "歌", "乐")
# def music(message):
#     return [
#         "title",
#         "description",
#         "music_url",
#         "hq_music_url"
#         ]

# @robot.filter(re.compile("music"), "歌", "乐")
# def music2(message):
#     return [
#         "孤勇者",
#         "陈奕迅新作",
#         "https://shaohan-yun.oss-cn-beijing.aliyuncs.com/my_blog/陈奕迅 - 孤勇者.mp3",
#         ]


@robot.unknown
def reply_unknown(message):
    return SuccessReply(message=message)



robot.config.update(
    SERVER="auto",
    HOST="43.143.142.250",
    PORT="80",
    SESSION_STORAGE=None,
    APP_ID="wxa975f27840138056",
    APP_SECRET="b692e1a76e43316fd768724939345999",
    ENCODING_AES_KEY="2n6d6SHDPAuaBEHCQqROAWSd0zZwoxioADxeFL3cahm"
)

robot.run()
