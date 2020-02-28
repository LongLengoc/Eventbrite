import requests
import json
import os
from configparser import ConfigParser
from eventbrite import Eventbrite

class ex2():
    def __init__(self):
        config = ConfigParser()
        config.read(os.getcwd() + "/config_eventbrite.txt")
        self.privateToken = config.get("Eventbrite", "Private_token")

    def create_event(self):
        #get user id
        eventbrite = Eventbrite(self.privateToken)
        user = eventbrite.get_user()
        user_id = user['id']

        #header
        header = {
            'Authorization' : 'Bearer ' + self.privateToken,
            'Accept' : 'application/json',
            'Content-Type' : 'application/json'
        }

        #event data
        data = {
            "event" : {
                "name" : {
                    "html" : "Tiki bam la co 1 "
                },
                "start" : {
                    "timezone" : "Asia/Ho_Chi_Minh",
                    "utc" : "2019-11-25T10:00:00Z"
                },
                "end" : {
                    "timezone" : "Asia/Ho_Chi_Minh",
                    "utc" : "2019-11-25T11:00:00Z"
                },
                "currency" : "USD",
                "capacity" : 200,
            }
        }

        #create event
        link = 'https://www.eventbriteapi.com/v3/organizations/' + user_id + '/events/'
        cre_evt = requests.post(link, data=json.dumps(data), headers = header)
        print("Create Event : " + str(cre_evt.status_code))
        
        #get event id
        dict1 = json.loads(cre_evt.text)
        event_id = dict1['id']

        #create ticket class
        data1 = {
            "ticket_class" : {
                "name" : "VIP1",
                "quantity_total" : 150,
                "free" : True
            }
        }
        link1 = 'https://www.eventbriteapi.com/v3/events/' + event_id + '/ticket_classes/'
        cre_ticket = requests.post(link1, data= json.dumps(data1), headers = header)
        print("Create Ticket : " + str(cre_ticket.status_code))

        #public event
        link2 = 'https://www.eventbriteapi.com/v3/events/'+ event_id + '/publish/'
        evt_public = requests.post(link2, headers=header)
        print("Public Event : " + str(evt_public.status_code))

def main():
    event = ex2()
    event.create_event()

if __name__ == '__main__':
    main()