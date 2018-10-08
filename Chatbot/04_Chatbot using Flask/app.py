from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import wolframalpha
import wikipedia

app = Flask(__name__)

app_id = "8H7VT7-H784VVUQYL"
client = wolframalpha.Client(app_id)

english_bot = ChatBot(
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

#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    try : 
        userInput = request.args.get('msg')
        if len(userInput) == 0 :
            return('How can I help You?')
        else:    
            response = str(english_bot.get_response(userInput))
            if  response == 'No' : 
                try:
                    # Call Wolfarmalpha
                    res = client.query(userInput)
                    response = next(res.results).text
                    #  print('Bot(Wo) :', response)
                except:
                    try:
                        # Call Wikipedia
                        response = wikipedia.summary(userInput.lower(),sentences=2)
                        #    print('Bot(Wiki) :', response)
                    except:
                        response = "I don't Know"

            return (response)  

    except(KeyboardInterrupt, EOFError, SystemExit):
            return('Sorry')

if __name__ == "__main__":
    app.run()
