#12/14/2012
#The purpose of this file is to serve as a building block for executive email
#Uses micro web framework Flask to send the http requests and receive post requests from mailgun.
#
#
import sys, os, requests, json
from flask import request
path = os.path.dirname(os.path.abspath(__file__))
print(path)
if not path in sys.path:
	print(path)
	sys.path.append(path)
from flask import Flask
import keys
print('Flask Imported')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print('Printing Message to COnsone')
    if request.method == 'POST':
        #print 'Post request received'
        #sender = request.POST.get('sender')
        #recipient = request.POST.get('recipient')
        #data = request.data
        #dataDict = json.loads(data)
        #print dataDict
        #print request.headers
        #print request.json
        sender    = request.values.get('sender')
        recipient = request.values.get('recipient')
        subject   = request.values.get('subject', '')
        body_plain = request.args.get('body-plain', '')
        #body_without_quotes = request.args.get('stripped-text', '')
        #print 'sender:' ,sender, 'recipient:', recipient, subject
        #print body_plain
        #print body_without_quotes
        #print request.values
    return 'Hello World!'

def send_simple_message():
    return requests.post(
        keys.mailgun_login,

        auth=("api", keys.mailgun_API_key),
        data={"from": "Executive Email <me@samples.mailgun.org>",
              "to": "kisna72@gmail.com",
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})



def receive_email():
	'''This is a route method that receives email as post request from Say mailgun.
	'''
	pass

def get_executive_list(org_name):
	'''Go to database and fetch executive list for org_name
	args:
		org_name (String) : name of organization.
	returns:
		list of executives.
	'''
	#Since Database doesn't exist right now, I am just returning a 
	#generic list of email addresses.
	list_of_emails = ['kisna72@gmail.com', 'krishnaregmi@outlook.com']
	return list_of_emails

#Test get_executive_list
#print(get_executive_list('asme'))
def get_member_list(org_name):
	'''Go to database and fetch member list for org_name
	args:
		org_name (String) : name of organization.
	returns:
		list of executives.
	'''
	#Since Database doesn't exist right now, I am just returning a 
	#generic list of email addresses.
	list_of_emails = ['kisna72@gmail.com', 'krishnaregmi@outlook.com']
	return list_of_emails


#if __name__ == '__main__':
#    app.run(host='0.0.0.0')
#message = send_simple_message()
#print messasge.text


# if __name__ == "__main__":
#     app.run()