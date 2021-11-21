import streamlit as st
import requests, json

st.sidebar.header("Endpoints")
endpoint_choices = ['All Tickets', 'Solved Tickets', 'Open Tickets', 'Pending Tickets']
endpoint = st.sidebar.selectbox("Choose an Endpoint", endpoint_choices)

st.title(f"Zendesk Code Challenge - {endpoint}")

#set request params
url = 'https://zendeskcodingchallenge2053.zendesk.com/api/v2/tickets.json'
user = 'camst149@mail.rmu.edu'
pwd = 'Cman3742!'

# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()

# Example 1: Print the name of the first group in the list
#print( 'All Tickets = ', data['tickets'][0]['subject'] )
if endpoint == 'All Tickets':
    # print all tickets in the list
    ticket_list = data['tickets']
    for group in ticket_list:
        st.subheader(group['subject'])
        st.write(group['description'])
        st.write(group['requester_id'])

if endpoint == 'Open Tickets':
    # print open tickets in the list
    ticket_list = data['tickets']
    for group in ticket_list:
        if group['status'] == "open": 
            st.subheader(group['subject'])
            st.write(group['description'])
            st.write(group['requester_id'])

if endpoint == 'Solved Tickets':
    # print open tickets in the list
    ticket_list = data['tickets']
    for group in ticket_list:
        if group['status'] == "solved": 
            st.subheader(group['subject'])
            st.write(group['description'])
            st.write(group['requester_id'])
             
if endpoint == 'Pending Tickets':
    # print open tickets in the list
    ticket_list = data['tickets']
    for group in ticket_list:
        if group['status'] == "pending": 
            st.subheader(group['subject'])
            st.write(group['description'])
            st.write(group['requester_id'])

