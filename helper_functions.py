import os, sys, json, re

def get_name_from_email(email):
    return re.split('@', email)[0]
#print get_name_from_email('kisna72@gmail.com')

def get_org_name(json_data):
    '''Gets the json_data, finds to_email, and returns the to name'''
    sent_to_email = json_data['To']
    org = re.split('@', sent_to_email)

    return org[0]
def check_if_org(org_name):
    #make a database connection  and check if the org_name exists
    return True


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
