class TelegramBackend:
    def __init__(token):
        self.updater = Updater(token)
        print("Using API Token: " + token + "...")
        self.dispatch = self.updater.dispatcher
        print("Prepping dispatcher...")
        self.name = name.lower()
        self.dispatch.addHandler(MessageHandler([], self.msgHandler))

    # TODO: Make this work
    def msgHandler(self, bot, incoming):
        return 

    def onMessage(self, cb):
        return

    def sendMessage(chat_id, msg):
        return

