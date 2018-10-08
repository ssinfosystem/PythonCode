import wolframalpha
import wikipedia
from botchatter import get_response

app_id = "8H7VT7-H784VVUQYL"
client = wolframalpha.Client(app_id)

while True: 
    try : 
        request = input('You : ')
        if request.lower().strip()!= 'bye':
            response = str(get_response(request))
            if  response == 'No' : 
                try:
                    # Call Wolfarmalpha
                    res = client.query(request)
                    response = next(res.results).text
                    print('Bot(Wo) :', response)
                except:
                    try:
                        # Call Wikipedia
                        response = wikipedia.summary(request,sentences=2)
                        print('Bot(Wiki) :', response)
                    except:
                        print("I don't Know")
            else :    
                print('Bot :',response) 
                
        if request.strip().lower() == 'bye':
            print('Bot :', 'Bye , see you next time') 
            break
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
            

