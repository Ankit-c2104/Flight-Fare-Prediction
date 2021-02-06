#import numpy as np
import pickle
#import pandas as pd
import streamlit as st
from datetime import datetime, time
from flask import Flask
import pickle


app = Flask(__name__)
# Done using Streamlit
pickle_file = open("flight_fareprediction_xgb.pkl","rb")
classifier = pickle.load(pickle_file)

def welcome():
    return "Welcome All"

def flight_fare(source, destination, stops, Journey_day, Journey_month,
                                     Dept_hour, Dept_min, airlines, Arrival_day, Arrival_month,
                                     Arrival_hour, Arrival_min, Dur_hr, Dur_min):

    #Source -'Chennai', 'Delhi', 'Kolkata', 'Mumbai'
    #Banglore = 0 (not in column)
    if (source == 'Chennai') :
        s_Chennai = 1
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0

    elif (source == 'Delhi'):
        s_Chennai = 0
        s_Delhi = 1
        s_Kolkata = 0
        s_Mumbai = 0

    elif (source == 'Kolkata'):
        s_Chennai = 0
        s_Delhi = 0
        s_Kolkata = 1
        s_Mumbai = 0

    elif (source == 'Mumbai'):
        s_Chennai = 0
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 1

    else:
        s_Chennai = 0
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0

    #Destination - 'Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New_Delhi'
    #Banglore = 0 (not in column)

    if (destination == 'Cochin'):
        d_Cochin = 1
        d_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
        d_New_Delhi = 0

    elif (destination == 'Delhi'):
        d_Cochin = 0
        d_Delhi = 1
        d_Hyderabad = 0
        d_Kolkata = 0
        d_New_Delhi = 0

    elif (destination == 'Hyderabad'):
        d_Cochin = 0
        d_Delhi = 0
        d_Hyderabad = 1
        d_Kolkata = 0
        d_New_Delhi = 0

    elif (destination == 'Kolkata'):
        d_Cochin = 0
        d_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 1
        d_New_Delhi = 0

    elif (destination == 'New_Delhi'):
        d_Cochin = 0
        d_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
        d_New_Delhi = 1

    else:
        d_Cochin = 0
        d_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0
        d_New_Delhi = 0

    #Airlines - 'IndiGo', 'Jet Airways', 'Multiple carriers', 'SpiceJet', 'Trujet', 'Vistara'
    #Air India = 0(Not in column)
    if (airlines == 'IndiGo'):
        a_IndiGo = 1
        a_Jet_Airways = 0
        a_Multiple_carriers = 0
        a_SpiceJet = 0
        a_Trujet = 0
        a_Vistara = 0

    elif (airlines == 'Jet Airways'):
        a_IndiGo = 0
        a_Jet_Airways = 1
        a_Multiple_carriers = 0
        a_SpiceJet = 0
        a_Trujet = 0
        a_Vistara = 0

    elif (airlines == 'Multiple carriers'):
        a_IndiGo = 0
        a_Jet_Airways = 0
        a_Multiple_carriers = 1
        a_SpiceJet = 0
        a_Trujet = 0
        a_Vistara = 0

    elif (airlines == 'SpiceJet'):
        a_IndiGo = 0
        a_Jet_Airways = 0
        a_Multiple_carriers = 0
        a_SpiceJet = 1
        a_Trujet = 0
        a_Vistara = 0

    elif (airlines == 'Trujet'):
        a_IndiGo = 0
        a_Jet_Airways = 0
        a_Multiple_carriers = 0
        a_SpiceJet = 0
        a_Trujet = 1
        a_Vistara = 0

    elif (airlines == 'Vistara'):
        a_IndiGo = 0
        a_Jet_Airways = 0
        a_Multiple_carriers = 0
        a_SpiceJet = 0
        a_Trujet = 0
        a_Vistara = 1

    else:
        a_IndiGo = 0
        a_Jet_Airways = 0
        a_Multiple_carriers = 0
        a_SpiceJet = 0
        a_Trujet = 0
        a_Vistara = 0

    #Stops - 'Non Stop', '1 Stop', '2 Stop', '3 Stop', '4 Stop'
    # before label_encoding - 'non-stop', '2 stops', '1 stop', '3 stops', '4 stops'
    # after label_encoding - 4, 1, 0, 2, 3
    if (stops == 'Non Stop') :
        stop_val = 4
    elif (stops == '1 Stop'):
        stop_val = 0
    elif (stops == '2 Stop'):
        stop_val = 1
    elif (stops == '3 Stop'):
        stop_val = 2
    else:
        stop_val = 3

    prediction = classifier.predict([[
        stop_val,
        Journey_day,
        Journey_month,
        Dept_hour,
        Dept_min,
        Arrival_hour,
        Arrival_min,
        Dur_hr,
        Dur_min,
        a_IndiGo,
        a_Jet_Airways,
        a_Multiple_carriers,
        a_SpiceJet,
        a_Trujet,
        a_Vistara,
        s_Chennai,
        s_Delhi,
        s_Kolkata,
        s_Mumbai,
        d_Cochin,
        d_Delhi,
        d_Hyderabad,
        d_Kolkata,
        d_New_Delhi
    ]])
    output = round(prediction[0], 2)
    print(output)
    return output

def main():
    #st.title("Flight Fare Prediction")
    html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Flight Fare Prediction ML App </h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    #Select source
    st.write('Select Source of Journey : ')
    source = st.selectbox('',('Chennai', 'Delhi', 'Kolkata', 'Mumbai', 'Banglore'))
    #st.write('You selected:', source)

    #Select Destination
    st.write('Select Journey Destination : ')
    destination = st.selectbox('',
                               ('Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New_Delhi', 'Banglore'))
    #st.write('You selected:', destination)

    # Select Stopages
    st.write('Select How many stops you want in your Journey : ')
    stops = st.selectbox('',
                         ('Non Stop', '1 Stop', '2 Stop', '3 Stop', '4 Stop'))
    #st.write('You selected:', stops)

    #Journey Day
    st.write('Select Journey Day : ')
    Journey_day = st.slider('', 1, 31, 1)
    #st.write("Selected Day of Journey", Journey_day)

    #Journey Month
    st.write('Select Journey Month : ')
    Journey_month = st.slider('', 1, 12, 1)
    #st.write("Selected Month of Journey", Journey_month)

    # Departure Hour
    st.write('Select Departure Hour : ')
    Dept_hour = st.slider('', 1, 24, 1)
    #st.write("Selected Departure Hour", Dept_hour)

    # Departure Min
    st.write('Select Departure Minutes : ')
    Dept_min = st.slider("", 0, 60, 1)
    #st.write("Selected Departure Minute", Dept_min)

    # Airlines
    st.write('Select Airlines : ')
    airlines = st.selectbox('',
                            ('Air India' ,'IndiGo', 'Jet Airways', 'Multiple carriers', 'SpiceJet',
                             'Trujet', 'Vistara'))
    #st.write("Selected Airline", airlines)

    # Arrival Day
    st.write('Select Arrival Day : ')
    Arrival_day = st.slider('', 1, 31, 1, key="arrd")
    #st.write("Selected Arrival Day", Arrival_day)

    # Arrival Month
    st.write('Select Arrival Month : ')
    Arrival_month = st.slider('', 1, 12, 1, key="arrhm")
    #st.write("Selected Arrival Month", Arrival_month)

    #Arrival Hour
    st.write('Select Arrival Hour : ')
    Arrival_hour = st.slider("",1,24,1, key="arrhr")
    #st.write("Selected Arrival Hour", Arrival_hour)

    # Arrival Min
    st.write('Select Arrival Minute : ')
    Arrival_min = st.slider("", 0, 60, 1, key="arrmin")
    #st.write("Selected Arrival Minute", Arrival_min)

    #Duration Hour
    Dur_hr = abs(Arrival_hour - Dept_hour)
    #st.write("Duration Hour", Dur_hr)

    #Duration Minute
    Dur_min = abs(Arrival_min - Dept_min)
    #st.write("Duration Minute", Dur_min)

    fare_price = ''
    if st.button('Predict'):
            fare_price = flight_fare(source, destination, stops, Journey_day, Journey_month,
                                     Dept_hour, Dept_min, airlines, Arrival_day, Arrival_month,
                                     Arrival_hour, Arrival_min, Dur_hr, Dur_min)

            st.success('The Predicted Flight Fare is {}'.format(fare_price))

    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()

#to execute - streamlit run app.py

