#12/14/2012
#The purpose of this file is to serve as a building block for executive email
#Uses micro web framework Flask to send the http requests and receive post requests from mailgun.
#
#
import sys, os, requests, json

path = os.path.dirname(os.path.abspath(__file__))
print(path)
if not path in sys.path:
    print(path)
    sys.path.append(path)
from flask import Flask
from flask import request
import keys
print('Flask Imported')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'THis is your Home page'
    print('Printing Message to COnsone')
    if request.method == 'POST':
        sender    = request.values.get('sender')
        recipient = request.values.get('recipient')
        subject   = request.values.get('subject', '')
        body_plain = request.args.get('body-plain', '')
        #body_without_quotes = request.args.get('stripped-text', '')
    return 'Hello World!'

def send_simple_message():
    return requests.post(
        keys.mailgun_login,

        auth=("api", keys.mailgun_API_key),
        data={"from": "Executive Email <me@samples.mailgun.org>",
              "to": "kisna72@gmail.com",
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


@app.route('/receiveemail', methods=['POST'])
def receive_email():
    '''This is a route method that receives email as post request from Say mailgun.
    Implementation: This function receives the post request with the 
    following information:
        sender email : kregmi@uno.com
        to email : asme@mydomain.com
    Do a database lookup for sender email. If sender email is registered email sender,
    strip asme from asme@mydomain.com.  

    #Future functionality: If the subject says RE: and a send email subject,
    remove that email from the waitlist, and forwared the correction RE: email
    to the secratry  ( email sender )

    Delegate the rest of the work to a different function for testability.
    Also if this code is ported to Django, this makes the porting much simple.

    Args:

    Returns:
        Dict:{
        'sender':kregmi@uno.edu
        'to':asme@mydomain.com
        'subject':'Register for the Bake Sale'
        'body':'Hey Guys, This is Krishna. Please sign up for the Bake Sale'
        #Future functionality : HTML emails.
        }
        sender : 
    '''
    print('Printing Message to COnsone')
    if request.method == 'POST':
        a = 2
        sender    = request.values.get('sender')
        recipient = request.values.get('recipient')
        subject   = request.values.get('subject', '')
        body_plain = request.args.get('body-plain', '')
        #body_without_quotes = request.args.get('stripped-text', '')
    #call_executive email sendint function
    #call list email in the waiting list to 
    return 'Hello World!'
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


if __name__ == '__main__':
   app.run(host='0.0.0.0')
#message = send_simple_message()
#print messasge.text


# if __name__ == "__main__":
#     app.run()