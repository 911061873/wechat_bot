from wxpy import *
import txai

bot = Bot(cache_path=True, console_qr=False)
yzj = ensure_one(bot.search('杨子江'))
zky = ensure_one(bot.search('赵凯云'))


# bot.self.send('能收到吗？')
# bot.file_helper.send('能收到吗？')


@bot.register(chats=bot.self, msg_types=TEXT, except_self=False)
def report_msg(msg):
    return txai.chat('1', msg.text)


embed()
