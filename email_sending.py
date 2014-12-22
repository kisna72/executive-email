#12/14/2012
#The purpose of this file is to serve as a building block for executive email
#Uses micro web framework Flask to send the http requests and receive post requests from mailgun.
#
#
import sys, os, requests, json, re

path = os.path.dirname(os.path.abspath(__file__))
print(path)
if not path in sys.path:
    print(path)
    sys.path.append(path)
from flask import Flask
from flask import request
import helper_functions as hf
import keys
#import keys
print('Flask Imported')
app = Flask(__name__)

#Flow
# 1. Receive an Email.
# 2. Check for sent to :
#     It can either be a organization or a person.
# 3. If it is organization, that means the user wants to send the email to that organization.
# 4. Make Sure that this user has the authority to send email to that org.
# 5. Next, Make a databse entry for this email. Mark requested.
# 6. Send Emails to executives. If successfull, Mark Sent, and add Email_Users_TIme as 30 mins ahead of time.
# 7. Keep checking for database for Email_Users_TIme. If the time is older than the said time, send Users Emails.
# 8. If you receive a reply from a user, check if he is a executive.
# 9. IF EXECUTIVE, then find the email sent, using the data from the email, then mark it cancelled.
# 10. Email the original sender that his email has been cancelled.


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
    #Must return json_data
    #In thei future, receive a Post Request, Check if it is Post. Then convert it into JSON Format, 
    #Next return the JSON Format. Must use for key, value in request.values.iteritems()
    json_file = '/Users/krishnaregmi/Documents/OneDrive/12-projects-2015/executive-email/email_2.json'
    with open(json_file, 'r') as f:
        raw_data = f.read()
    json_data = json.loads(raw_data)
    return json_data
#Test receive_email.
#t = receive_email()
#print t['Date']

def send_single_email(email_address, json_data):
    '''Takes in the json_data and a email_address and then sends the email through mailgun
        The Idea is to forward the email to the email_address.
    '''
    print 'Sending Single Email'
    json_data['To'] = email_address
    print json_data
    return requests.post(
        keys.mailgun_login,

        auth=("api", keys.mailgun_API_key),
        data={"from": json_data['From'],
              "to": email_address,
              "subject": json_data['Subject'],
              "text": json_data['body-plain'],
              "html":json_data['body-html']}
              )
    
#Test get_org_name
t = receive_email()
p = hf.get_org_name(t)
email_lst = hf.get_executive_list(p)
msg = send_single_email(email_lst[0], t)
print email_lst
print msg


sys.exit()
if __name__ == '__main__':
   app.run(host='0.0.0.0')