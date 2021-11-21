import streamlit as st
import requests, json
import SessionState
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
        st.write(group['created_at'])
        st.write(group['requester_id'])
    N = 25
    session_state = SessionState.get(page_number = 0)
    last_page = len(group['subject']) // N

# Add a next button and a previous button
    prev, _ ,next = st.columns([1, 10, 1])
    if next.button("Next"):
        if session_state.page_number + 1 > last_page:
            session_state.page_number = 0
        else:
            session_state.page_number += 1
    if prev.button("Previous"):
        if session_state.page_number - 1 < 0:
            session_state.page_number = last_page
        else:
            session_state.page_number -= 1
    

if endpoint == 'Open Tickets':
    # Number of entries per screen
    N = 25
    session_state = SessionState.get(page_number = 0)
    last_page = len(data) // N

    # Add a next button and a previous button
    prev, _ ,next = st.columns([1, 10, 1])
    if next.button("Next"):
        if session_state.page_number + 1 > last_page:
            session_state.page_number = 0
        else:
            session_state.page_number += 1
    if prev.button("Previous"):
        if session_state.page_number - 1 < 0:
            session_state.page_number = last_page
        else:
            session_state.page_number -= 1
    # print open tickets in the list
    ticket_list = data['tickets']
    for group in ticket_list:
        if group['status'] == "open": 
            st.subheader(group['subject'])
            st.write(group['description'])
            st.write(group['created_at'])
            st.write(group['requester_id'])

if endpoint == 'Solved Tickets':
    # Number of entries per screen
    N = 25
    session_state = SessionState.get(page_number = 0)
    last_page = len(data) // N

    # Add a next button and a previous button
    prev, _ ,next = st.columns([1, 10, 1])
    if next.button("Next"):
        if session_state.page_number + 1 > last_page:
            session_state.page_number = 0
        else:
            session_state.page_number += 1
    if prev.button("Previous"):
        if session_state.page_number - 1 < 0:
            session_state.page_number = last_page
        else:
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
    # Number of entries per screen
    N = 25
    session_state = SessionState.get(page_number = 0)
    last_page = len(data) // N

    # Add a next button and a previous button
    prev, _ ,next = st.columns([1, 10, 1])
    if next.button("Next"):
        if session_state.page_number + 1 > last_page:
            session_state.page_number = 0
        else:
            session_state.page_number += 1
    if prev.button("Previous"):
        if session_state.page_number - 1 < 0:
            session_state.page_number = last_page
        else:
            session_state.page_number -= 1
    # print open tickets in the list
    ticket_list = data['tickets']
    for group in ticket_list:
        if group['status'] == "pending": 
            st.subheader(group['subject'])
            st.write(group['description'])
            st.write(group['created_at'])
            st.write(group['requester_id'])

