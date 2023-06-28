import joblib
import gradio as gr
import pandas as pd
# Load the saved model from file using joblib
loaded_model = joblib.load('model/ensemble_model.joblib')






day_of_week_options = {'Monday': 0, 'Tuesday': 1, 'Wednesday':2, 'Thursday':3,'Friday':4,'Saturday':5, 'Sunday':6}
inputs = [gr.inputs.Dropdown(choices=list(day_of_week_options.keys()), label="Day_of_Week")]

age_band_options = {'Under 18' :0, '18-30':1, '31-50':2,'Over 51': 3, 'Unknown':4}
inputs.append(gr.inputs.Dropdown(choices=list(age_band_options.keys()), label="Age_Band_of Driver"))



Sex_of_driver_dict = {'Male': 0, 'Female': 1, 'Unknown':2}
inputs.append(gr.inputs.Dropdown(choices=list(Sex_of_driver_dict.keys()), label='Sex_of_driver'))

Ed_label = {'Illiterate':0, 'Writing & reading':1,'Junior high school':2,'Elementary school':3,'High school':4,'Above high school':5,'Unknown':6}
inputs.append(gr.inputs.Dropdown(choices=list(Ed_label.keys()), label='Educational_level'))

vechicle_driver_relation = {'Other': 0, 'Employee': 1, 'Owner':2}
inputs.append(gr.inputs.Dropdown(choices=list(vechicle_driver_relation.keys()), label='Vehicle_driver_relation'))

Driving_experience = {'No Licence':0, 'Below 1yr':1,'1-2yr':2,'2-5yr':2,'5-10yr':4,'Above 10yr':5,'unknown':6}
inputs.append(gr.inputs.Dropdown(choices=list(Driving_experience.keys()), label = 'Driving_experience'))

Type_of_vehicle = {'Ridden horse' : 0, 'Bicycle':1, 'Motorcycle':2,'Taxi':3,'Automobile':4,'Pick Up':5,'Public':6,'Lorry':7,'Other':8}
inputs.append(gr.inputs.Dropdown(choices =list(Type_of_vehicle.keys()), label='Type_of_vehicle'))

Owner_of_vehicle = {'Owner': 0, 'Governmental': 1, 'Organization':2,'Other':3}
inputs.append(gr.inputs.Dropdown(choices=list(Owner_of_vehicle.keys()), label = 'Owner_of_vehicle'))

Service_year_of_vehicle = {'Below 1yr':0,'1-2yr':1,'2-5yrs':2,'5-10yrs':3,'Above 10yr':4,'Unknown':5}
inputs.append(gr.inputs.Dropdown(choices=list(Service_year_of_vehicle.keys()), label = 'Service_year_of_vehicle'))

inputs.append(gr.inputs.Slider(minimum=0, maximum=10, step=1, label="Defect_of_vehicle"))

Area_accident_occured = {'Market Areas':0,'Rural village areas' : 1, 'Hospital Areas': 2,
        'Outside Rural Areas': 3, 'Recreational Areas': 4,
        'School areas': 5, 'Industrail Areas': 6,
        'Church Areas': 7, 'Residential areas': 8,
        'Office areas': 9, 'Other': 10}
inputs.append(gr.inputs.Dropdown(choices=list(Area_accident_occured.keys()), label = 'Area_accident_occured'))

Lanes_or_Medians = {'Solid line Two Way': 0, 'One way': 1, 'Double carriageway (median)' : 2,'Undivided Two way':3,'Divided Two way':4,'Other':5}
inputs.append(gr.inputs.Dropdown(choices=list(Lanes_or_Medians.keys()), label = 'Lanes_or_Medians'))

Road_allignment ={'upward(mountain terrain,Steep grade)': 0,
        'Tangent(Rolling terrian)' : 1,
        'Sharp reverse curve': 2,
        'Escarpments': 3,
        'Gentle horizontal curve': 4,
        'Tangent(mountain terrain)': 5,
         'downward(mountain terrain,Steep grade)':6,
         'Tangent(Flat terrain, mild grade)':7,
         'Tangent(Flat terrian)':8}
inputs.append(gr.inputs.Dropdown(choices=list(Road_allignment.keys()), label = 'Road_allignment'))


Types_of_Junction = {'X Shape':0, 'T Shape':1, 'O Shape': 2,'Crossing':3, 'No junction': 4, 'Y Shape': 5, 'Unknown':6, 'Other':6}
inputs.append(gr.inputs.Dropdown(choices=list(Types_of_Junction.keys()), label = 'Types_of_Junction'))

Road_surface_type = {'Asphalt roads with some distress':0, 'Gravel roads': 1, 'Earth roads': 2, 'Asphalt roads': 3, 'Unknown': 4, 'Other':4}
inputs.append(gr.inputs.Dropdown(choices=list(Road_surface_type.keys()), label = 'Road_surface_type'))

Road_surface_conditions =  {'Flood over 3cm. deep': 0, 'Snow':1,'Wet or damp':2, 'Dry':3}
inputs.append(gr.inputs.Dropdown(choices=list(Road_surface_conditions.keys()), label = 'Road_surface_conditions'))

Light_conditions = {'Darkness - lights unlit': 0, 'Darkness - no lighting':1,'Darkness - lights lit':2, 'Daylight':3}
inputs.append(gr.inputs.Dropdown(choices=list(Light_conditions.keys()), label = 'Light_conditions'))

Weather_conditions = {'Fog or mist':0,'Raining and Windy' : 1, 'Snow': 2,
        'Windy': 3, 'Cloudy': 4,
        'Raining': 5, 'Normal': 6,
        'Other': 7, 'Unknown': 7}
inputs.append(gr.inputs.Dropdown(choices=list(Weather_conditions.keys()), label = 'Weather_conditions'))


Type_of_collision = {'With Train':0,'Fall from vehicles' : 1, 'Collision with roadside-parked vehicles': 2,
        'Collision with animals': 3, 'Rollover': 4,
        'Collision with pedestrians': 5, 'Collision with roadside objects': 6,
        'Vehicle with vehicle collision': 7, 'Other': 8,
        'Unknown': 8}
inputs.append(gr.inputs.Dropdown(choices=list(Type_of_collision .keys()), label = 'Type_of_collision '))

inputs.append(gr.inputs.Slider(minimum=0, maximum=10, step=1, label="Number_of_vehicles_involved"))
inputs.append(gr.inputs.Slider(minimum=0, maximum=10, step=1, label="Number_of_casualties"))


Vehicle_movement =  {'Parked':0,'Waiting to go' : 1, 'U-Turn': 2,
        'Stopping': 3, 'Overtaking': 4,
        'Entering a junction': 5, 'Getting off': 6,
        'Turnover': 7, 'Reversing': 8,
        'Moving Backward': 9, 'Going straight': 10, 'Other':11,
        'Unknown' : 11}
inputs.append(gr.inputs.Dropdown(choices=list(Vehicle_movement .keys()), label = 'Vehicle_movement'))

Casuality_class = {'Passenger': 0, 'Pedestrian':1,'Driver or rider': 2,'Unknown':3}
inputs.append(gr.inputs.Dropdown(choices=list(Casuality_class .keys()), label = 'Casuality_class'))

Sex_of_casuality =  {'Male': 0, 'Female': 1, 'Unknown':2}
inputs.append(gr.inputs.Dropdown(choices=list(Sex_of_casuality.keys()), label = 'Sex_of_casuality'))



Age_band_of_casuality =  {'Under 18' :0, '18-30':1, '31-50':2,'Over 51': 3, 'Unknown':4}
inputs.append(gr.inputs.Dropdown(choices=list(Age_band_of_casuality.keys()), label = 'Age_band_of_casuality'))


inputs.append(gr.inputs.Slider(minimum=0, maximum=3, step=1, label="Casuality_severity"))

Work_of_casuality = {'Unemployed':0, 'Student':1, 'Employee': 2,'Self-employed':3, 'Driver': 4, 'Unknown': 5, 'Other':5}
inputs.append(gr.inputs.Dropdown(choices=list(Work_of_casuality.keys()), label = 'Work_of_casuality'))

Fitness_of_casuality = {'Blind' : 0, 'Deaf': 1, 'Normal' : 2, 'Other':3}
inputs.append(gr.inputs.Dropdown(choices=list(Fitness_of_casuality.keys()), label = 'Fitness_of_casuality'))

Pedestrian_movement = {'Walking along in carriageway, facing traffic' : 0,
         'In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing) - masked by parked or statioNot a Pedestrianry vehicle':1,
         'Walking along in carriageway, back to traffic':2,
         'In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing)':3,
         'Crossing from offside - masked by  parked or statioNot a Pedestrianry vehicle':4,
         "Crossing from driver's nearside": 5,
         'Crossing from nearside - masked by parked or statioNot a Pedestrianry vehicle':6,
         "Not a Pedestrian":7,
        "Unknown or other": 8}
inputs.append(gr.inputs.Dropdown(choices=list(Pedestrian_movement.keys()), label = 'Pedestrian_movement'))

Cause_of_accident = {'Improper parking':0,'Drunk driving':1, 'Overloading':2,'Overspeed':3,'Turnover':4,
        'Overturning':5, 'Driving at high speed':6,'Getting off the vehicle improperly':7,'Driving to the left':8,
        'Driving under the influence of drugs':9, 'Overtaking':10, 'No priority to pedestrian':11,'Moving Backward':12,
        'No priority to vehicle':12,'Driving carelessly':13,
        'Changing lane to the left':14, 'Changing lane to the right':15, 'No distancing':16, 'Unknown': 17,'Other':17}

inputs.append(gr.inputs.Dropdown(choices=list(Cause_of_accident.keys()), label = 'Cause_of_accident'))


inputs.append(gr.inputs.Slider(minimum=1, maximum=24, step=1, label="Hour_of_Day"))









outputs = gr.outputs.Textbox(label="Accident Severity Level")

def predict_outcome(day_of_week, age_band, sex_of_driver, educational_level, vehicle_driver_relation,
driving_experience, type_of_vehicle, owner_of_vehicle, service_year_of_vehicle, defect_of_vehicle,
area_accident_occured, lanes_or_medians, road_allignment, types_of_junction,
road_surface_type, road_surface_conditions, light_conditions, weather_conditions,type_of_collision,number_of_vechicle_involved,
number_of_casualties,vehicle_movement,casuality_class,sex_of_casuality,age_band_of_casuality, number_of_casuality_severity,work_of_casuality,
fitness_of_casuality,pedestrian_movement,cause_of_accident, hour_of_day):
    # Convert categorical variables to numerical form
    day_of_week_num = day_of_week_options[day_of_week]
    age_band_num = age_band_options[age_band]
    sex_of_driver_num = Sex_of_driver_dict[sex_of_driver]
    educational_level_num = Ed_label[educational_level]
    vehicle_driver_relation_num = vechicle_driver_relation[vehicle_driver_relation]
    driving_experience_num = Driving_experience[driving_experience]
    type_of_vehicle_num = Type_of_vehicle[type_of_vehicle]
    owner_of_vehicle_num = Owner_of_vehicle[owner_of_vehicle]
    service_year_of_vehicle_num = Service_year_of_vehicle[service_year_of_vehicle]
    defect_of_vehicle_num = defect_of_vehicle
    area_accident_occured_num = Area_accident_occured[area_accident_occured]
    lanes_or_medians_num = Lanes_or_Medians[lanes_or_medians]
    road_allignment_num = Road_allignment[road_allignment]
    types_of_junction_num = Types_of_Junction[types_of_junction]
    road_surface_type_num = Road_surface_type[road_surface_type]
    road_surface_conditions_num = Road_surface_conditions[road_surface_conditions]
    light_conditions_num = Light_conditions[light_conditions]
    weather_conditions_num = Weather_conditions[weather_conditions]
    type_of_collision_num = Type_of_collision[type_of_collision]
    number_of_vehicle_involved_num = number_of_vechicle_involved
    number_of_casuaties_num = number_of_casualties
    vehicle_movement_num = Vehicle_movement[vehicle_movement]
    casuality_class_num = Casuality_class[casuality_class]
    sex_of_casuality_num = Sex_of_casuality[sex_of_casuality]
    age_band_of_casuality_num = Age_band_of_casuality[age_band_of_casuality]
    number_of_casuality_num = number_of_casuality_severity
    work_of_casuality_num = Work_of_casuality[work_of_casuality]
    fitness_of_casuality_num =  Fitness_of_casuality[fitness_of_casuality]
    pedestrian_movement_num = Pedestrian_movement[pedestrian_movement]
    cause_of_accident_num = Cause_of_accident[cause_of_accident]
    hour_of_day_num = hour_of_day
    
    
    
    feature_dict = {'Day_of_week': day_of_week_num,
                'Age_band_of_driver': age_band_num,
                'Sex_of_driver': sex_of_driver_num,
                'Educational_level': educational_level_num,
                'Vehicle_driver_relation': vehicle_driver_relation_num,
                'Driving_experience': driving_experience_num,
                'Type_of_vehicle': type_of_vehicle_num,
                'Owner_of_vehicle': owner_of_vehicle_num,
                'Service_year_of_vehicle': service_year_of_vehicle_num,
                'Defect_of_vehicle': defect_of_vehicle,
                'Area_accident_occured': area_accident_occured_num,
                'Lanes_or_Medians': lanes_or_medians_num,
                'Road_allignment': road_allignment_num,
                'Types_of_Junction': types_of_junction_num,
                'Road_surface_type': road_surface_type_num,
                'Road_surface_conditions': road_surface_conditions_num,
                'Light_conditions': light_conditions_num,
                'Weather_conditions': weather_conditions_num,
                'Type_of_collision': type_of_collision_num,
                'Number_of_vehicles_involved' : number_of_vehicle_involved_num,
                'Number_of_casualties' : number_of_casuaties_num,
                'Vehicle_movement' : vehicle_movement_num,
                'Casualty_class' : casuality_class_num,
                'Sex_of_casualty': sex_of_casuality_num,
                'Age_band_of_casualty': age_band_of_casuality_num ,
                'Casualty_severity': number_of_casuality_num,
                'Work_of_casuality': work_of_casuality_num,
                'Fitness_of_casuality':fitness_of_casuality_num,
                'Pedestrian_movement' : pedestrian_movement_num,
                'Cause_of_accident' : cause_of_accident_num,
                'Hour_of_Day': hour_of_day_num
                
                }
                
    

    # Convert the dictionary into a dataframe
    input_df = pd.DataFrame.from_dict([feature_dict])

    # Use the loaded model to make predictions
    severity_prediction = loaded_model.predict(input_df)

    # Return the predicted outcome (i.e. severity) as a string
    if severity_prediction == 0:
        return 'Fatal'
    elif severity_prediction == 1:
        return 'Serious'
    elif severity_prediction == 2:
        return 'Slight'
    else:
        return 'Unknown'









def predict(*inputs):
    # call your model with the input values
    #result = loaded_model.predict(inputs)
    # return the result as a string
    return str(inputs)

# Create the Gradio app with the input and output interfaces, and the prediction function
app = gr.Interface(predict_outcome,inputs,outputs,title = 'Road Accident Severity Prediction',description = "Choose the parameters for the prediction.")


# Run the app
app.launch()
