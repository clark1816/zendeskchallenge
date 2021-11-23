# zendeskchallenge
coded zendesk challenge using python and the streamlit library to publish the webapp.

to run this program you must run 2 commands in your console or just click the link to take you to the web app.

//to run on local host//
1. type - pip3 install -r requirements.txt
2. type - streamlit run getdata.py

//to run on web browser// 
visit https://share.streamlit.io/clark1816/zendeskchallenge/main/getdata.py

what I learned from this challenge. I got a better understanding of making requests to an API in python and also learned how to use
the streamlit library better. 

Challenges I faced - At first I was having trouble getting connected to the zendesk api and getting my requests to come through. 
Once I figured it out it was smooth sailing. Till I got to the part when it came time to add the next and previous option. As you will see my program lacks those functions
this is because I was not able to figure out how to get it work with a json file. I got it to work with a large pandas data frame which was nicely organized in csv. I found online resources that showed different way but I would neeed help from someone to figure out how to add the next option in streamlit with a json file. The next and previous option work sometimes you have to press it twise but other than that all requirements work well. 

//small issue
the next and previous buttons are a bit unresponsive so u have to click them twice to get them to work. They will only take u to a next page on the all tickets option.
