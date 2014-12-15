#12/14/2012
#The purpose of this file is to serve as a building block for executive email
#Uses micro web framework Flask to send the http requests and receive post requests from mailgun.
#
#
import sys, os, requests, json
from flask import request
path = os.path.dirname(os.path.abspath(__file__))
if not path in sys.path:
    sys.path.append(path)
from flask import Flask
print 'Flask Imported'
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print 'Printing Message to COnsone'
    if request.method == 'POST':
        print 'Post request received'
        #sender = request.POST.get('sender')
        #recipient = request.POST.get('recipient')
        #data = request.data
        #dataDict = json.loads(data)
        #print dataDict
        print request.headers
        #print request.json
        sender    = request.values.get('sender')
        recipient = request.values.get('recipient')
        subject   = request.values.get('subject', '')
        body_plain = request.args.get('body-plain', '')
        #body_without_quotes = request.args.get('stripped-text', '')
        print 'sender:' ,sender, 'recipient:', recipient, subject
        #print body_plain
        #print body_without_quotes
        #print request.values
    return 'Hello World!'





def send_simple_message():
    return requests.post(
        #"https://api.mailgun.net/v2/sandboxfc48ae5340e746ad99c9ab6079f3643d.mailgun.org",
        "https://api.mailgun.net/v2/livingcitynola.com/messages",
        auth=("api", "DumDaDumDumDumDumDum"),
        data={"from": "Executive Email <me@samples.mailgun.org>",
              "to": "kisna72@gmail.com",
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})



if __name__ == '__main__':
    app.run(host='0.0.0.0')
#message = send_simple_message()
#print messasge.text

##Flow:
# Receive Email. If the 

# if __name__ == "__main__":
#     app.run()