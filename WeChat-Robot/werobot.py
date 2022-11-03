import re
import werobot
from werobot.replies import TextReply, ImageReply, VoiceReply, SuccessReply
from werobot.replies import ArticlesReply, Article, SuccessReply, MusicReply


# 输入微信公众平台请求凭证
robot = werobot.WeRoBot(token='tsh980509')         # 写入服务器配置填写的 Token

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
    ENCODING_AES_KEY="XWbRw4lacZrNdR4C78YS0hVDovuzGuo5NePjxO502t3"
)

robot.run()



import werobot

robot = werobot.WeRoBot(token='tsh980509')

@robot.handler
def hello(message):
    return 'Hello World!'

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '43.143.142.250'
robot.config['PORT'] = 80
robot.run()

import werobot

robot = werobot.WeRoBot(token='tsh980509')

@robot.handler
def echo(message):
    return 'Hello World!'

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80

robot.run(server='gevent')




public function index()
{
    $timestamp = $_GET['timestamp'];
    $nonce = $_GET['nonce'];
    $token = $_GET['tianshaohan123'];
    $signature = $_GET['signature'];
    $echostr = $_GET['echostr'];

    $array = array($timestamp, $nonce, $token);
    sort($array);
    $tmpstr = shal(implode(glue:'', $array));
    if ($tmpstr == $signature && $echostr){
        echo $echostr;
    }

}

private function checkSignature()
{
    $signature = $_GET["signature"];
    $timestamp = $_GET["timestamp"];
    $nonce = $_GET["nonce"];

    $token = TOKEN;
    $tmpArr = array($token, $timestamp, $nonce);
    sort($tmpArr, SORT_STRING);
    $tmpStr = implode( $tmpArr );
    $tmpStr = sha1( $tmpStr );

    if( $tmpStr == $signature ){
        return true;
    }else{
        return false;
    }
}
PHP示例代码下载：下载

第三步
