from functions import *
data=[["Outputs",["Outlook","Tempreture","Humidity","Wind","Hornyness"]],
    ['No', ['Sunny', 'Hot', 'High', 'Weak',"Yes"]],
    ['No', ['Sunny', 'Hot', 'High', 'Strong',"Mild"]],
    ['Yes', ['Overcast', 'Hot', 'High', 'Weak',"No"]],
    ['Yes', ['Rain', 'Mild', 'High', 'Weak',"Mild"]],
    ['Yes', ['Rain', 'Cool', 'Normal', 'Weak','Yes']],
    ['No', ['Rain', 'Cool', 'Normal', 'Strong',"Yes"]],
    ['Yes', ['Overcast', 'Cool', 'Normal', 'Strong',"Mild"]],
    ['No', ['Sunny', 'Mild', 'High', 'Weak',"No"]],
    ['Yes', ['Sunny', 'Cool', 'Normal', 'Weak',"No"]],
    ['Yes', ['Rain', 'Mild', 'Normal', 'Weak',"No"]],
    ['Yes', ['Sunny', 'Mild', 'Normal', 'Strong',"No"]],
    ['Yes', ['Overcast', 'Mild', 'High', 'Strong',"No"]],
    ['Yes', ['Overcast', 'Hot', 'Normal', 'Weak',"Mild"]],
    ['No', ['Rain', 'Mild', 'High', 'Strong',"Yes"]]
]

newdata=changeTable(data,0,'Sunny')
for i in newdata:
    print(i)
    
print(findNODE(newdata))