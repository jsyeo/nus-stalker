from __future__ import print_function, unicode_literals
from ldap3 import connection, server
from ldap3 import AUTH_SIMPLE, STRATEGY_SYNC, STRATEGY_ASYNC_THREADED, SEARCH_SCOPE_WHOLE_SUBTREE
import getpass
import json
import sys
import re
import argparse

basedn = 'ou=Students,dc=stu,dc=nus,dc=edu,dc=sg'

def read_config():

    with open("config.json", "r") as f:
        data = f.read()
    config = json.loads(data)
    username = config.get('username', "")
    password = config.get('password', "")
    if username == "nusstu\\" or password == "":
        print("Please enter your NUSNET credentials in the config.json file")
        sys.exit(1)
    return (username, password)

def get_module_code(grp):
    m = re.search('CN=MODULE(.*?),OU=Modules,OU=Student,DC=stu,DC=nus,DC=edu,DC=sg', grp)
    if m:
        return m.group(1)
    else:
        return ""

def get_group_type(grp):
    m = re.search('OU=(.*?),OU=Student,DC=stu,DC=nus,DC=edu,DC=sg', grp)
    if m:
        return m.group(1)
    else:
        return ""

def response_to_persons(response):
    """
    Converts ldap search response to person dict
    """
    results = []
    for r in response:
        person = {}
        modules = []
        person['name'] = r['attributes']['displayName']
        person['id'] = r['attributes']['name']
        person['modules'] = []
        person['course'] = []
        person['career'] = []
        person['groups'] = []
        groups = r['attributes']['memberOf']
        for group in groups:
            group_type = get_group_type(group)
            if group_type == "Modules":
                person['modules'].append(get_module_code(group))
            elif group_type == "Courses":
                person['course'].append(group)
            elif group_type == "Careers":
                person['career'].append(group)
            else:
                person['groups'].append(group)
        results.append(person)
    return results

def person_search(c, query):
    """
    Searches for a person based on the person's name.
    c = LDAP connection object
    query = search string
    """
    filter_by = '(displayName=*{0}*)'.format(query)
    found = c.search(basedn, filter_by, SEARCH_SCOPE_WHOLE_SUBTREE,
                      attributes = ['displayName', 'memberOf', 'name'])
    if found:
        return response_to_persons(c.response)
    else:
        return []

def get_roster(c, module_code):
    filter_by = "(memberOf=CN=MODULE{0},OU=Modules,OU=Student,DC=stu,DC=nus,DC=edu,DC=sg)".format(query.upper())
    found = c.search(basedn, filter_by, SEARCH_SCOPE_WHOLE_SUBTREE,
                      attributes = ['displayName', 'memberOf', 'name'])
    if found:
        return response_to_persons(c.response)
    else:
        return []


def connect_nus():
    user, pw = read_config()
    servername = "ldapstu.nus.edu.sg"
    # define a basic authentication server
    s = server.Server(servername, port = 389)
    # define a client strategy (synchronous, not threaded)
    c = connection.Connection(s, clientStrategy = STRATEGY_SYNC,
                              user=user, password=pw, authentication=AUTH_SIMPLE)
    c.open()  # open connection
    if c.bind():
        print("Sucessfully connected to nus directory.")
        print("Master {0}, let the stalking begin.".format(getpass.getuser()))
    else:
        print("Something bad happened, do you have a working internet connection?")
        print("Did you enter your credentials into config.json correctly?")
        sys.exit(1)
    return c

def main():
    c = connect_nus()
    return

if __name__ == "__main__":
    main()
