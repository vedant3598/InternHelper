# importing IndeedClient library from Indeed's API
import indeed import IndeedClient
import socket

# Initiating an IndeedClient object
client = IndeedClient(publisher = )

# Client IP address to get IP address of user (required for 'userip' of parameter request to Indeed API)
client_hostname = socket.gethostname()
client_ip_address = socket.gethostbyname(client_hostname)

# 
def position_location(location: str, position: str):
    parameters = {
        'q': "{position}",
        'l': "{location}",
        'fromage': "12",
        'limit': "25",
        'filter': "1",
        'userip': "{client_ip_address}",
        'useragent': ""
    }

    search_response = client.search(**parameters)

def position(position: str):
    parameters = {
        'q': "{position}",
        'fromage': "12",
        'limit': "25",
        'filter': "1",
        'userip': "{client_ip_address}",
        'useragent': ""
    }

    search_response = client.search(**parameters)

