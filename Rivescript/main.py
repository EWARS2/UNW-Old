from rivescript import RiveScript

bot = RiveScript()
bot.load_directory("./")  # Load RiveScript files from the current directory
bot.sort_replies()  # Sort the replies for better performance

while True:
    message = input("You: ")
    reply = bot.reply("localuser", message)
    print("Bot:", reply)
