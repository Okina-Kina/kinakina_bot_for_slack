# rtm.connect has deprecated to call
# # coding: utf-8

# import requests
# import glob
# import os
# import re
# import random

# from slackbot.bot import respond_to     # @botname: で反応するデコーダ
# from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
# from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

# # @respond_to('string')     bot宛のメッセージ
# #                           stringは正規表現が可能 「r'string'」

# # @listen_to('string')      チャンネル内のbot宛以外の投稿
# #                           @botname: では反応しないことに注意
# #                           他の人へのメンションでは反応する
# #                           正規表現可能

# # @default_reply()          DEFAULT_REPLY と同じ働き
# #                           正規表現を指定すると、他のデコーダにヒットせず、
# #                           正規表現にマッチするときに反応
# #                           ・・・なのだが、正規表現を指定するとエラーになる？

# # message.reply('string')   @発言者名: string でメッセージを送信
# # message.send('string')    string を送信
# # message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
# #                               文字列中に':'はいらない

# #　テスト
# @respond_to('てすてす')
# def mention_func(message):
#     message.reply('てすてすおじさん')  # メンション

# #　ディレクトリ内のテキストの一覧を表示
# @respond_to('テキストファイル見せて')
# @listen_to('テキストファイル見せて')
# def text_list_reply(message):
#     message.reply('はいよっとな')
#     # デバッグ
#     # print([os.path.basename(p) for p in glob.glob("./resources/texts/*.txt")if os.path.isfile(p)])
#     # 指定ディレクトリ内のテキストのみを検索する
#     message.reply('{}'.format([os.path.basename(p) for p in glob.glob("./resources/texts/*")if os.path.isfile(p)]))

# #　テキストの呼び出し
# @respond_to('(.*)テキストちょうだい')
# def text_back_for_app(message, name):

#     fileName = [os.path.basename(p) for p in glob.glob("./resources/texts/*.txt")if os.path.isfile(p)]
#     needFile = name + ".txt"
        
#     TOKEN = os.environ.get("BOT_API_TOKEN")
#     #message.reply('{}'.format(fileName))

#     for i in range(len(fileName)):

#         if fileName[i] == needFile:
#             message.reply('はいよー')
#             #message.reply('{}'.format(fileName[i]))
#             files = {'file': open("./resources/texts/" + needFile, 'rb')}

#             param = {
#             'token':TOKEN,
#             'filename': needFile,
#             'initial_comment': needFile + "はこちら～",
#             'title': needFile
#             }
#             requests.post(url="https://slack.com/api/files.upload",params = param, files=files)
#             break
 
#         elif (i == len(fileName) - 1) and (fileName[i] != name + ".txt"):
#             message.reply('ないよー')

# @listen_to('(.*)テキストちょうだい')
# def text_back_for_channel(message, name):

#     fileName = [os.path.basename(p) for p in glob.glob("./resources/texts/*.txt")if os.path.isfile(p)]
#     needFile = name + ".txt"

#     TOKEN = os.environ["BOT_API_TOKEN"]
#     #message.reply('{}'.format(fileName))

#     for i in range(len(fileName)):

#         if fileName[i] == needFile:
#             message.reply('はいよー')
#             #message.reply('{}'.format(fileName[i]))
            
#             files = {'file': open("./resources/texts/" + needFile, 'rb')}

#             param = {
#             'token':TOKEN,
#             'filename': needFile,
#             'initial_comment': needFile + "はこちら～",
#             'title': needFile
#             }
#             requests.post(url="https://slack.com/api/files.upload",params = param, files=files)
#             break
 
#         elif (i == len(fileName) - 1) and (fileName[i] != name + ".txt"):
#             message.reply('ないよー')

# @listen_to('(.*)テキスト作って')
# def create_text_for_channel(message,name):
#     message.reply('つくりまー')
#     createText = name + ".txt"
#     file = open('./resources/texts/' + createText,'w')
#     file.close()

# #　テキストの読み上げ
# @listen_to('(.*)テキスト読み上げて')
# def read_text_for_channel(message,name):
 
#     fileName = [os.path.basename(p) for p in glob.glob("./resources/texts/*.txt")if os.path.isfile(p)]
#     needFile = name + ".txt"

#     for i in range(len(fileName)):

#         if fileName[i] == needFile:
#             message.reply('はいよー\n')
#             #message.reply('{}'.format(fileName[i]))
#             with open('./resources/texts/' + needFile) as readText:
#                 readStr = readText.read()
#             message.send(readStr)
#             message.reply('おわりー')
#             break
 
#         elif (i == len(fileName) - 1) and (fileName[i] != name + ".txt"):
#             message.reply('ないよー')
