from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Cheru',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./db.sqlite3' ,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.70,
            'default_response': 'I am sorry, but I do not understand.' ,
        },
        'chatterbot.logic.TimeLogicAdapter'
    ]
)
while True:
    try:
        request = input('You : ')
        if request.strip()!= 'Bye':
            response = str(bot.get_response(request))
            print('Bot :',response)    
        if request.strip() == 'Bye':
            print('Bot :', 'Bye , see you next time') 
            break
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
