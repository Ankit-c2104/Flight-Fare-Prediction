from flask import Flask, request, render_template
#from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app1 = Flask(__name__)
classifier = pickle.load(open("flight_fareprediction_xgb.pkl", "rb"))

@app1.route("/", methods = ['GET'])
#@cross_origin()
def home():
    return render_template("home.html")

@app1.route("/predict", methods = ['POST'])
#@cross_origin()
def predict():
    if request.method == "POST":
        # Journey Day and Journey Month
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
        #print("Journey Day :",Journey_day, Journey_month)

        # Departure Hour and Minute
        Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)
        #print("Departure Time : ", Dep_hour, Dep_min)

        #Arrival Hour and Minute
        date_arr = request.form['Arrival_Time']
        Arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)
        #print("Arrival Time : ", Arrival_hour, Arrival_min)

        #Duration Hour adn Duration Minute
        dur_hr = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        #print("Duration : ", dur_hr, dur_min)

        #Number of Stops
        # Stops - 'Non Stop', '1 Stop', '2 Stop', '3 Stop', '4 Stop'
        # before label_encoding - 'non-stop', '2 stops', '1 stop', '3 stops', '4 stops'
        # after label_encoding - 4, 1, 0, 2, 3

        Total_stops = int(request.form['stops'])  #changes made in home.html according to label enconding
        #print("Total Stops : ", Total_stops)

        # Airlines - 'IndiGo', 'Jet Airways', 'Multiple carriers', 'SpiceJet', 'Trujet', 'Vistara'
        # Air India = 0(Not in column)

        airlines = request.form['airline']
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

        #print("Airlines : ",
            #       a_IndiGo,
            #      a_Jet_Airways,
            #      a_Multiple_carriers,
            #   a_SpiceJet,
            # a_Trujet,
        # a_Vistara)

        # Source -'Chennai', 'Delhi', 'Kolkata', 'Mumbai'
        # Banglore = 0 (not in column)
        source = request.form['Source']
        if (source == 'Chennai'):
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

        #print('Source : ',
            #     s_Chennai,
            #s_Delhi,
            #s_Kolkata,
            #s_Mumbai )

        # Destination - 'Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New_Delhi'
        # Banglore = 0 (not in column)

        destination = request.form['Destination']
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

        elif (destination == 'New Delhi'):
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

         #print('Destination : ',
            #d_Cochin,
            #d_Delhi,
            #d_Hyderabad,
            #d_Kolkata,
            #d_New_Delhi)

        prediction = classifier.predict([[
        Total_stops,
        Journey_day,
        Journey_month,
        Dep_hour,
        Dep_min,
        Arrival_hour,
        Arrival_min,
        dur_hr,
        dur_min,
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
        d_New_Delhi]])

        output = round(prediction[0],2)

        return render_template('home.html', prediction_text = "Predicted Flight Fare is Rs. {}".format(output))

    return render_template('home.html')

if __name__ == "__main__":
    app1.run(debug=True)