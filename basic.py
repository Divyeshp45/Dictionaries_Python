from pydoc import visiblename


first_dictionary={
 "dog":"barks","cat":"meww"}
#retrive itemfrom dictionary
print(first_dictionary["cat"])

#add item in dictionary

first_dictionary["duck"]="quacks"

'''
#Wiping an dictionary
first_dictionary={}  '''
 

#Change value in Dictionary
first_dictionary["dog"]="barks loudly"

#LOOPING THROUGH A DICTIONARY
for key in first_dictionary:
    print(key+':')
    print(first_dictionary[key])


#Nested dictionaries
travel_log={"India":{"States_visited":["ratnagiri","goa","bengaluru","Pune"],"States_not_visited":["Chennai","Gujarat","Telangana","kashmir"]},
            "America":["newyork","Washington DC","Chicago"]}   

print(travel_log["India"] )         

#Nested Dictionaries in list
travel_log=[ {"Country":"India",
            "States_visited":["ratnagiri","goa","bengaluru","Pune"],
            "States_not_visited":["Chennai","Gujarat","Telangana","kashmir"]},
            {"country":"America","Visits":["newyork","Washington DC","Chicago"]}]
print(travel_log[0])            