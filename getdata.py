import streamlit as st
import requests, json
import SessionState
import config
st.sidebar.header("Endpoints")
endpoint_choices = ['All Tickets', 'Solved Tickets', 'Open Tickets', 'Pending Tickets']
endpoint = st.sidebar.selectbox("Choose an Endpoint", endpoint_choices)

st.title(f"Zendesk Code Challenge - {endpoint}")

#set request params
url = config.zendeskurl
user = config.user
pwd = config.pwd

# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))
#define session state
session_state = SessionState.get(page_number = 1)
prev, _ ,next = st.columns([1, 25, 1])

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
    N = 25
    ticket_list = data['tickets']

    last_page = len(ticket_list) // N
    if (last_page * N) < len(ticket_list):
        last_page += 1

    start = (session_state.page_number-1)*N
    end = min(start+N, len(ticket_list))
    ticket_list = ticket_list[start:end]

    if next.button('Next'):
        if session_state.page_number < last_page:
            session_state.page_number += 1

    if prev.button('Previous'):
        if session_state.page_number > 1:
            session_state.page_number -= 1

    for group in ticket_list:
        st.subheader(group['subject'])
        st.write(group['description'])
        st.write(group['created_at'])
        st.write(group['requester_id'])
       

if endpoint == 'Open Tickets':
    # print open tickets in the list
    ticket_list = data['tickets']
    # print all tickets in the list
    N = 25
    ticket_list = data['tickets']

    last_page = len(ticket_list) // N
    if (last_page * N) < len(ticket_list):
        last_page += 1

    start = (session_state.page_number-1)*N
    end = min(start+N, len(ticket_list))
    ticket_list = ticket_list[start:end]

    if next.button('Next'):
        if session_state.page_number < last_page:
            session_state.page_number += 1

    if prev.button('Previous'):
        if session_state.page_number > 1:
            session_state.page_number -= 1

    for group in ticket_list:
        if group['status'] == "open": 
            st.subheader(group['subject'])
            st.write(group['description'])
            st.write(group['created_at'])
            st.write(group['requester_id'])
    prev, _ ,next = st.columns([1, 10, 1])
        # A variable to keep track of which product we are currently displaying
    session_state = SessionState.get(page_number = 0)
    N =25
       
if endpoint == 'Solved Tickets':
    # print all tickets in the list
    N = 25
    ticket_list = data['tickets']

    last_page = len(ticket_list) // N
    if (last_page * N) < len(ticket_list):
        last_page += 1

    start = (session_state.page_number-1)*N
    end = min(start+N, len(ticket_list))
    ticket_list = ticket_list[start:end]

    if next.button('Next'):
        if session_state.page_number < last_page:
            session_state.page_number += 1

    if prev.button('Previous'):
        if session_state.page_number > 1:
            session_state.page_number -= 1

    # print open tickets in the list
    ticket_list = data['tickets']
    for group in ticket_list:
        if group['status'] == "solved": 
            st.subheader(group['subject'])
            st.write(group['description'])
            st.write(group['created_at'])
            st.write(group['requester_id'])
             
if endpoint == 'Pending Tickets':
    # print all tickets in the list
    N = 25
    ticket_list = data['tickets']

    last_page = len(ticket_list) // N
    if (last_page * N) < len(ticket_list):
        last_page += 1

    start = (session_state.page_number-1)*N
    end = min(start+N, len(ticket_list))
    ticket_list = ticket_list[start:end]

    if next.button('Next'):
        if session_state.page_number < last_page:
            session_state.page_number += 1

    if prev.button('Previous'):
        if session_state.page_number > 1:
            session_state.page_number -= 1

    # print open tickets in the list
    ticket_list = data['tickets']
    for group in ticket_list:
        if group['status'] == "pending": 
            st.subheader(group['subject'])
            st.write(group['description'])
            st.write(group['created_at'])
            st.write(group['requester_id'])

