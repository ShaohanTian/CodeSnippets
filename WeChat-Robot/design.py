from werobot import WeRoBot
robot = WeRoBot()
robot.config["APP_ID"] = "wxa975f27840138056"
robot.config["APP_SECRET"] = "2e62e6dd384e8387639415f0bb797f43"
# robot.config['HOST'] = '127.0.0.1'



# robot.config['HOST'] = '127.0.0.1'
# robot.config['PORT'] = '9050'

client = robot.client
print(client.grant_token())
print(client.get_media_list(media_type='image', offset=0, count=10))
# robot.config["TOKEN"] = client.grant_token()["access_token"]

# client.create_menu({
#     "button":[{
#          "type": "click",
#          "name": "今日歌曲",
#          "key": "music"
#     }]
# })


# robot.config['HOST'] = '127.0.0.1'
# robot.config['PORT'] = '9050'
# robot.run()
