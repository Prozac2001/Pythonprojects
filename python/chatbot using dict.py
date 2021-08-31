# Chatbot

bot_dict = {
    "how are you": "I'm fine :) How are you too?",
    "weather": "It's raining today :(Please try to stay indoor",
    "what name": "My name is Oke Julius, May I know your name too?",
    "which school": "FCAH&PT",
    "at home": "Nope :(I'm not at home"
    }
print("Welcome to TOBI'S ChatBot!\nPress[x] to quit")

print("Bot: Hello Friend!")

while True:
    u_input = input("You: ").lower()

    if u_input == 'x':
        break

    

#for i in bot_dict:
#    if i in u_input:
#        print('Bot: {}'.format(bot_dict))

    bot_reply = [bot_dict[i] for i in bot_dict if i in u_input]

    if len(bot_reply) >0:
        print('Bot: {}'.format(bot_reply[0]))
        continue

    print("Bot: Sorry :(I have no reply for this ")




print("Thank you for chatting with me:)")
