from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def get_response(usrText):
    bot = ChatBot(
        'Cheru', read_only = True , 
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
                'default_response': 'No' ,
            },
        ]
    )
    response = str(bot.get_response(usrText))
    return response  

            
