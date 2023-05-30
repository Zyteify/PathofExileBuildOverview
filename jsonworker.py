import json
import pandas as pd
import requests

ENDPOINT = f"https://poe.ninja/api/data/0/getbuildoverview"

PARAMS = {"overview": "sanctum", "type": "exp", "language": "en"}


def _try_get_builds():
    r = requests.get(url=ENDPOINT, params=PARAMS)
    try:
        return r.json()
    except:
        return {}
    
def save_json_to_file(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_json_from_file(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        return data

json_filename = 'data.json'
#jsondata = load_json_from_file(json_filename)

def save_section_of_data(jsondata, keys, outputlocation, IDName):
    
    # Create a new dictionary with only the desired properties
    cull_data = {prop: jsondata[prop] for prop in keys if prop in jsondata}

    #create the dataframe bases on the dictionary
    df = pd.DataFrame(cull_data)
    # Add index as a new column
    df[IDName] = df.reset_index().index

    # Save DataFrame to a CSV file
    df.to_csv(outputlocation, index=False)

def save_uniques(jsondata, outputlocation):
    Uniques= []
    for i in jsondata["uniqueItemUse"]:
        playerincrement = 0

        for j in jsondata["uniqueItemUse"][i]:
            c = []
            #unique items are stored by the incremental value so this needs to be updated every time
            playerincrement += j
            #get the id of the person using the unique
            c.append(playerincrement)
            #get the id of the unqiue
            c.append(i)
            Uniques.append(c)

    columns = ['account_ID', 'Unique_ID']
    df = pd.DataFrame(Uniques, columns=columns)

    # Save DataFrame to a CSV file
    df.to_csv(outputlocation, index=False)

def save_unique_names(jsondata, outputlocation):
    Uniques= []
    for index, unique in enumerate(jsondata["uniqueItems"]):

        c = []
        c.append(index)
        c.append(unique["name"])
        c.append(unique["type"])
        

        Uniques.append(c)

    columns = ['Unique_ID', 'UniqueName', 'uniqueType']
    df = pd.DataFrame(Uniques, columns=columns)

    # Save DataFrame to a CSV file
    df.to_csv(outputlocation, index=False)

def save_activeskill_names(jsondata, outputlocation):
    activeskills = []
    for index, activeskill in enumerate(jsondata["activeSkills"]):

        c = []
        c.append(index)
        c.append(activeskill["name"])
        c.append(activeskill["icon"])
        c.append(activeskill["dpsName"])
        

        activeskills.append(c)

    columns = ['activeSkill_ID', 'activeSkillName', 'icon', 'activeSkillDPSName']
    df = pd.DataFrame(activeskills, columns=columns)

    # Save DataFrame to a CSV file
    df.to_csv(outputlocation, index=False)

def save_activeSkills(jsondata, outputlocation):
    ActiveSkills = []
    for i in jsondata["activeSkillUse"]:
        playerincrement = 0

        for j in jsondata["activeSkillUse"][i]:
            c = []
            #unique items are stored by the incremental value so this needs to be updated every time
            playerincrement += j
            #get the id of the person using the unique
            c.append(playerincrement)
            #get the id of the unqiue
            c.append(i)
            ActiveSkills.append(c)

    columns = ['account_ID', 'activeSkills_ID']
    df = pd.DataFrame(ActiveSkills, columns=columns)

    # Save DataFrame to a CSV file
    df.to_csv(outputlocation, index=False)

def save_allskill_names(jsondata, outputlocation):
    allskills = []
    for index, value in enumerate(jsondata["allSkills"]):

        c = []
        c.append(index)
        c.append(value["name"])
        
        #some skills have no icon for some reason
        if 'icon' in value:
            c.append(value["icon"])
        #else:
            #print(value["name"])

        allskills.append(c)

    columns = ['allSkill_ID', 'allSkillName', 'icon']
    df = pd.DataFrame(allskills, columns=columns)

    # Save DataFrame to a CSV file
    df.to_csv(outputlocation, index=False)

def save_allSkills(jsondata, outputlocation):
    Allskills = []
    for i in jsondata["allSkillUse"]:
        playerincrement = 0

        for j in jsondata["allSkillUse"][i]:
            c = []
            #unique items are stored by the incremental value so this needs to be updated every time
            playerincrement += j
            #get the id of the person using the unique
            c.append(playerincrement)
            #get the id of the unqiue
            c.append(i)
            #add the unique with the person using it
            #testing increment
            #c.append(str(j))
            Allskills.append(c)

    columns = ['account_ID', 'allSkills_ID']
    df = pd.DataFrame(Allskills, columns=columns)

    # Save DataFrame to a CSV file
    df.to_csv(outputlocation, index=False)



#download the json from the api endpoint at poe.ninja
jsondata = _try_get_builds()
#save the json to file
save_json_to_file(jsondata, 'data.json')
#save the parts of json required into csv files

save_section_of_data(jsondata, ["accounts", "names", "levels", "classes"], 'output/account.csv', 'account_ID')

save_section_of_data(jsondata, ["classNames"], 'output/classNames.csv', 'classNames_ID')

save_uniques(jsondata, 'output/uniques.csv')

save_unique_names(jsondata, 'output/uniqueNames.csv')

#todo check why the cypher commands to create a relationship between the active skill names and accounts doesnt work
# save_activeskill_names(jsondata, 'output/activeSkillNames.csv')

#save_activeSkills(jsondata, 'output/activeSkills.csv')

save_allskill_names(jsondata, 'output/allSkillNames.csv')

save_allSkills(jsondata, 'output/allSkills.csv')
#



"""
def save_skillDetails(jsondata, outputlocation):
    skilldetails = []
    for i in jsondata["skillDetails"]:
        
        c = []
        c.append(jsondata["skillDetails"][i]["name"])
        for j in jsondata["skillDetails"][i]:
            
            #list of all support games
            for k in jsondata["skillDetails"]["supportGems"]["names"]:
                #the name of the support gem
                c.append(jsondata["skillDetails"]["supportGems"]["name"])
            
            playerincrement = 0
            #list of all usage of support games
            for k in jsondata["skillDetails"]["supportGems"]["use"]:

                c.append(k)
                c.append(jsondata["skillDetails"]["supportGems"][k])
                #usage is stored by the incremental value so this needs to be updated every time
                playerincrement += k
                #get the id of the person using the skill
                c.append(playerincrement)

        for j in jsondata["skillDetails"]["dps"]:
            
            c.append(j)
            #dps is stored in an array with [physical dps, lightning dps, cold dps, fire dps, chaos dps, dps mode]
            #dps mode is 0 for normal and 2 for damage over time
            c.append(jsondata["skillDetails"]["dps"][0])
            c.append(jsondata["skillDetails"]["dps"][1])
            c.append(jsondata["skillDetails"]["dps"][2])
            c.append(jsondata["skillDetails"]["dps"][3])
            c.append(jsondata["skillDetails"]["dps"][4])
            #dps mode
            c.append(jsondata["skillDetails"]["dps"][5])
        
        skilldetails.append(c)

    #columns = ['account_ID', 'allSkills_ID']
    df = pd.DataFrame(skilldetails)#, columns=columns)

    # Save DataFrame to a CSV file
    df.to_csv(outputlocation, index=False)

save_skillDetails(jsondata, 'output/skillDetails.csv')
"""
exit()


