from functions import *

data = [
    ["Outputs", ["Outlook", "Temperature", "Humidity", "Wind", "Mood", "Time of Day", "Activity Level", "Precipitation", "Location", "Day Type"]],
    ['No', ['Sunny', 'Hot', 'High', 'Weak', "Happy", "Morning", "High", "None", "Outdoor", "Weekday"]],
    ['No', ['Sunny', 'Hot', 'High', 'Strong', "Neutral", "Afternoon", "Medium", "None", "Outdoor", "Weekday"]],
    ['Yes', ['Overcast', 'Hot', 'High', 'Weak', "Grumpy", "Morning", "Low", "None", "Indoor", "Weekend"]],
    ['Yes', ['Rain', 'Mild', 'High', 'Weak', "Happy", "Evening", "Medium", "Heavy", "Shelter", "Weekday"]],
    ['Yes', ['Rain', 'Cool', 'Normal', 'Weak', "Neutral", "Morning", "High", "Light", "Outdoor", "Weekend"]],
    ['No', ['Rain', 'Cool', 'Normal', 'Strong', "Grumpy", "Afternoon", "Low", "Heavy", "Indoor", "Weekday"]],
    ['Yes', ['Overcast', 'Cool', 'Normal', 'Strong', "Happy", "Evening", "Medium", "None", "Shelter", "Weekend"]],
    ['No', ['Sunny', 'Mild', 'High', 'Weak', "Neutral", "Morning", "Medium", "None", "Outdoor", "Weekday"]],
    ['Yes', ['Sunny', 'Cool', 'Normal', 'Weak', "Happy", "Afternoon", "High", "None", "Outdoor", "Weekend"]],
    ['Yes', ['Rain', 'Mild', 'Normal', 'Weak', "Neutral", "Morning", "Low", "Light", "Shelter", "Weekday"]],
    ['Yes', ['Sunny', 'Mild', 'Normal', 'Strong', "Grumpy", "Evening", "Medium", "None", "Indoor", "Weekend"]],
    ['Yes', ['Overcast', 'Mild', 'High', 'Strong', "Happy", "Morning", "High", "None", "Outdoor", "Weekday"]],
    ['Yes', ['Overcast', 'Hot', 'Normal', 'Weak', "Neutral", "Afternoon", "Medium", "None", "Indoor", "Weekend"]],
    ['No', ['Rain', 'Mild', 'High', 'Strong', "Happy", "Evening", "Low", "Heavy", "Shelter", "Weekday"]],
    ['No', ['Sunny', 'Hot', 'High', 'Weak', "Grumpy", "Morning", "Medium", "None", "Outdoor", "Weekday"]],
    ['Yes', ['Overcast', 'Mild', 'Normal', 'Weak', "Neutral", "Evening", "High", "None", "Outdoor", "Weekend"]],
    ['No', ['Rain', 'Hot', 'High', 'Strong', "Happy", "Afternoon", "Medium", "Heavy", "Indoor", "Weekday"]],
    ['Yes', ['Rain', 'Cool', 'Normal', 'Weak', "Neutral", "Morning", "Low", "Light", "Shelter", "Weekend"]],
    ['Yes', ['Sunny', 'Cool', 'High', 'Weak', "Happy", "Evening", "High", "None", "Outdoor", "Weekend"]],
    ['No', ['Sunny', 'Hot', 'Normal', 'Strong', "Grumpy", "Morning", "Medium", "None", "Indoor", "Weekday"]],
    ['Yes', ['Overcast', 'Cool', 'High', 'Weak', "Neutral", "Afternoon", "Low", "None", "Shelter", "Weekend"]],
    ['Yes', ['Rain', 'Mild', 'High', 'Weak', "Happy", "Evening", "Medium", "Light", "Outdoor", "Weekday"]],
    ['No', ['Rain', 'Hot', 'High', 'Strong', "Grumpy", "Afternoon", "Low", "Heavy", "Indoor", "Weekend"]],
    ['Yes', ['Overcast', 'Hot', 'Normal', 'Weak', "Happy", "Morning", "High", "None", "Shelter", "Weekday"]],
    ['No', ['Sunny', 'Mild', 'High', 'Strong', "Neutral", "Evening", "Medium", "None", "Outdoor", "Weekend"]],
    ['Yes', ['Rain', 'Cool', 'High', 'Weak', "Neutral", "Morning", "Low", "Light", "Shelter", "Weekday"]],
    ['Yes', ['Overcast', 'Cool', 'Normal', 'Weak', "Happy", "Afternoon", "High", "None", "Indoor", "Weekend"]],
    ['No', ['Sunny', 'Hot', 'High', 'Strong', "Grumpy", "Morning", "Medium", "None", "Outdoor", "Weekday"]],
    ['Yes', ['Rain', 'Mild', 'Normal', 'Weak', "Neutral", "Evening", "Medium", "Light", "Outdoor", "Weekend"]],
    ['Yes', ['Sunny', 'Cool', 'Normal', 'Weak', "Happy", "Morning", "High", "None", "Shelter", "Weekday"]],
    ['No', ['Rain', 'Cool', 'High', 'Strong', "Grumpy", "Afternoon", "Low", "Heavy", "Indoor", "Weekend"]],
    ['Yes', ['Overcast', 'Mild', 'Normal', 'Strong', "Happy", "Evening", "Medium", "None", "Outdoor", "Weekday"]],
]


