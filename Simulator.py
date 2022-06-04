# for picking countries
from itertools import count
import random
import math
import mysql.connector

# Define Continents
Continents = ['Europe','Asia','South America','Africa','Ocenia','North America']


# Define Seeds
Seeds = {
    1 : [
        {'Belgium':[1]}
        ,{'France':[1]}
        ,{'England':[1]}
        ,{'Espain':[1]}
        ,{'Portugal':[1]}
        ,{'Brazil':[3]}
        ,{'Argentina':[3]}
        ,{'Qatar':[2]}
    ]
    ,2 : [
        {'Denmaek':[1]}
        ,{'Netherlands':[1]}
        ,{'Germany':[1]}
        ,{'Mexico':[6]}
        ,{'USA':[6]}
        ,{'Switzerland':[1]}
        ,{'Crotia':[1]}
        ,{'Uruguay':[3]}
    ]
    ,3 : [
        {'Senegal':[4]}
        ,{'Iran':[2]}
        ,{'Japan':[2]}
        ,{'Morocco':[4]}
        ,{'Serbia':[1]}
        ,{'Poland':[1]}
        ,{'South Korea':[2]}
        ,{'Tunisia':[4]}
    ]
    ,4 : [
        {'Arabia':[2]}
        ,{'Ecuador':[3]}
        ,{'Ghana':[4]}
        ,{'Canada':[6]}
        ,{'Cameroon':[4]}
        ,{'Asia or North America Unkown':[2,6]}
        ,{'Europe Unkwon':[1]}
        ,{'Ocenia or South America Unkown':[5,3]}
    ]

}

# For set Qatar to A1 
isFirstRound = True 

# for pick random country from a seed
def pickCounry(s):

    global isFirstRound
    # check if ist is first round
    if isFirstRound and s == 1 : 
        rnd = 7
        isFirstRound = False
    else :
        # pick a random country from list
        rnd = math.floor(random.random() * len(Seeds[s]))

    # return selected Country
    return rnd

# delete a country
def PopCountry(s,c):
    Seeds[s].pop(c)

# add a country
def addCountry(g,s,c):
    country = Seeds[s][c]
    group = Groups[g]
    group[list(country.keys())[0]] = list(country.values())[0]


# check max 2 Europeans in a group and 1 from other Continents 
def checkConditions(g,s,c):
    country = Seeds[s][c]
    group = Groups[g]
    CountryValues = [x[0] for x in country.values()]
    GroupValues = [x[0] for x in group.values()]

    # max 2 Europeans
    if GroupValues.count(1) == 2 and 1 in CountryValues :
        return False
    # max 1 from other Continents 
    elif (CountryValues[0] in GroupValues) and (CountryValues[0] != 1) :
        return False
    elif len(CountryValues) > 1 : 
        if (CountryValues[1] in GroupValues) and (CountryValues[1] != 1) :
            return False
    else : 
        return True


# Define Groups
Groups = {
'A':{},
'B':{},
'C':{},
'D':{},
'E':{},
'F':{},
'G':{},
'H':{}
}


# fill all seeds in order 
for i in range(4) : 
    # fill all groups in order 
    for group in Groups : 
        country = pickCounry(i+1)

        # check conditions
        while not checkConditions(group,i+1,country) : 
            country = pickCounry(i+1)
        
        addCountry(group,i+1,country)
        PopCountry(i+1,country)

GroupsList = {}
for g in Groups : 
    GroupsList[g] = list(Groups[g].keys())

print(GroupsList)
        
# # open a connection
# cnx = mysql.connector.connect(user='root', password='',
#                                 host='127.0.0.1',
#                                 database='Worldcup')

# for group in GroupsList : 
#     for country in GroupsList[group] :
#         cursor =  cnx.cursor()  
#         query  = 'INSERT INTO `Predict` (`Country`, `Group`) VALUES (\'{0}\',\'{1}\')'.format(
#             country,
#             group
#         )
#         cursor.execute(query)
#         cnx.commit()

# #close connection
# cnx.close() 

        
# # MySQL Query 

# SELECT 
# p.Country , p.Group ,COUNT(p.Group) as Pcount 
# FROM
# predict as p 
# GROUP BY p.Country , p.Group 
# ORDER BY Pcount desc , Country 
# limit 32;