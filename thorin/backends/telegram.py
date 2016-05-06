class TelegramBackend:
    def __init__(self, thorin, token):
        self.updater = Updater(token)
        print("Using API Token: " + token + "...")
        self.dispatch = self.updater.dispatcher
        print("Prepping dispatcher...")
        self.name = name.lower()
        self.dispatch.addHandler(MessageHandler([], self.msgHandler))
        self.thorin = thorin

    def start(self):
        print("I am listening for messages...")
        self.updater.start_polling()
        self.updater.idle()

    # TODO: Make this work
    def msgHandler(self, bot, incoming):
        return 

    def onMessage(self, cb):
        def unwrap(bot, incoming):

        return

    def sendMessage(chat_id, msg):
        return

def new(thorin):

