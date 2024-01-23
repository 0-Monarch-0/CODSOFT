import time

# simple restraunt recommendation system using small database for basic idea 

# we are going to use content-based filtering :
def restraunt_suggest(cuisine,rating,area):
    list = []
    list1 = []
    list2 = []
    list3 =[]
    
    data={
    'Tirami su': {'cuisine': 'italian', 'area': 'downtown', 'price': '$$', 'occupancy': 'High', 'rating': '3.0'},
    'TinyTalian': {'cuisine': 'italian', 'area': 'suburb', 'price': '$$', 'occupancy': 'Medium', 'rating': '4.0'},
    'Anthony and Cleopatras': {'cuisine': 'italian', 'area': 'uptown', 'price': '$$$', 'occupancy': 'less', 'rating': '5.0'},

    'Tortillaistic': {'cuisine': 'mexican', 'area': 'downtown', 'price': '$', 'occupancy': 'High', 'rating': '4.0'},
    'Burrito bliss': {'cuisine': 'mexican', 'area': 'suburb', 'price': '$$', 'occupancy': 'Medium', 'rating': '3.0'},
    'Casa de Queso': {'cuisine': 'mexican', 'area': 'uptown', 'price': '$$', 'occupancy': 'less', 'rating': '5.0'},
    
    'Bento House': {'cuisine': 'japanese', 'area': 'downtown', 'price': '$$', 'occupancy': 'Low', 'rating': '4.0'},
    'Kitsune Grills': {'cuisine': 'japanese', 'area': 'suburb', 'price': '$$', 'occupancy': 'Medium', 'rating': '3.0'},
    'Sushi Motto': {'cuisine': 'japanese', 'area': 'uptown', 'price': '$$$', 'occupancy': 'high', 'rating': '5.0'},

    'Café Cognac': {'cuisine': 'french', 'area': 'downtown', 'price': '$$', 'occupancy': 'High', 'rating': '3.0'},
    'Parisian Parfait': {'cuisine': 'french', 'area': 'suburb', 'price': '$$', 'occupancy': 'Medium', 'rating': '4.0'},
    'LOpus au Château': {'cuisine': 'french', 'area': 'uptown', 'price': '$$$', 'occupancy': 'less', 'rating': '5.0'},

    'Paradise': {'cuisine': 'indian', 'area': 'downtown', 'price': '$$', 'occupancy': 'High', 'rating': '3.0'},
    'Tandoori Time': {'cuisine': 'indian', 'area': 'suburb', 'price': '$$', 'occupancy': 'Medium', 'rating': '4.0'},
    'House of Dosa': {'cuisine': 'indian', 'area': 'uptown', 'price': '$$$', 'occupancy': 'less', 'rating': '5.0'},

    'Thai BBQ': {'cuisine': 'thai', 'area': 'downtown', 'price': '$$', 'occupancy': 'High', 'rating': '3.0'},
    'Phuket Cafe': {'cuisine': 'thai', 'area': 'suburb', 'price': '$$', 'occupancy': 'Medium', 'rating': '4.0'},
    'Ving Khong': {'cuisine': 'thai', 'area': 'uptown', 'price': '$$$', 'occupancy': 'less', 'rating': '5.0'},

    'Aegyo Korea': {'cuisine': 'korean', 'area': 'downtown', 'price': '$$', 'occupancy': 'High', 'rating': '3.0'},
    'Seoul Food': {'cuisine': 'korean', 'area': 'suburb', 'price': '$$', 'occupancy': 'Medium', 'rating': '4.0'},
    'Korean Stew House': {'cuisine': 'korean', 'area': 'uptown', 'price': '$$$', 'occupancy': 'less', 'rating': '5.0'},
    }
    if(cuisine != 'null' and rating == 'null' and area =="null"):
        for names,details in data.items():
            for category,values in details.items():
                if(values == cuisine):
                    list.append(names)
    elif(cuisine =='null' and rating != 'null' and area == 'null'):
        for names,details in data.items():
            for category,values in details.items():
                if(values == rating):
                    list.append(names)
    elif(cuisine =='null' and rating == 'null' and area != 'null'):
        for names,details in data.items():
            for category,values in details.items():
                if(values == area):
                    list.append(names)
    else:
        for names,details in data.items():
            for category,values in details.items():
                if(values == cuisine):
                    list1.append(names)
                if(values == rating):
                    list2.append(names)
                if(values == area):
                    list3.append(names)
        for namez in list1:
            for name in list2:
                for nam in list3:
                    if (namez == name == nam):
                        list.append(namez)
    if (list == []):
        print('no record found')
    for names,values in data.items():
        for i in list:
            if(i == names):
                print('restraunt name:'+names)
                for name,value in values.items():
                    print(name,":",value)
                print(" ")              
    #we can also add large data sets but i am restricting my database to this extent....

    #iterating through the dictonary 
    
print("......................welcome to Restraunt Recommendation System........................")
time.sleep(1)
print('choose one option to consider: \n1.cuisine \n2.rating \n3.area \n4.all')
option = int(input("enter the num: "))
if(option == 1 or option == 4):
    user_cuisine = input("what type of cuisine you are looking for?\n") 
    time.sleep(1)
    if(option == 1):
        restraunt_suggest(user_cuisine.lower(),'null','null')
if(option == 2 or option == 4):
    user_rating = input("what type of a restraunt are you looking for?(like rating 3.0,4.0,5.0 etc)\n if you dont have an idea just type null\n")
    time.sleep(1)
    if(option == 2):
        restraunt_suggest('null',user_rating,'null')
if(option == 3 or option == 4):
    user_area = input("which place are we talking about? \n (uptown,downtown,suburb) \n if you don't have any idea just type null\n")
    if(option == 3):
        restraunt_suggest('null','null',user_area.lower())

if(option == 4):
    restraunt_suggest(user_cuisine.lower(),user_rating,user_area.lower())





