def onQQMessage(bot, contact, member, content):
    if content is not None:
        bot.SendTo(contact, 'Hello啊，我现在有事无法及时回复，请留言...')
        bot.Stop()