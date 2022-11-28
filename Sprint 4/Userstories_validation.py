import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime
# from tkinter.font import families


#Sprint 1 - Parth Patel
def us07(individuals, families):
    for individual_person in individuals:
        birthdate = individual_person.birthday.split("/")
        date_of_birth = date(
                            int(birthdate[0]),
                            int(birthdate[1]),
                            int(birthdate[2]))
        isalive = individual_person.alive
        if(isalive == 'True'):
            if(individual_person.age > 150):
                print("ERROR: INDIVIDUAL: US07: More than 150 years old - Birth date {}".format(birthdate))
                return  False          
        elif(isalive == 'False'):
            deathdate = individual_person.deathday.split("/")
            date_of_death = date(
                            int(deathdate[0]),
                            int(deathdate[1]),
                            int(deathdate[2]))
            if individual_person.age > 150:
                print("ERROR: INDIVIDUAL: US07: More than 150 years old at Death - Birth {} : Death {}".format(birthdate,deathdate))
                return False           
    print('Test 7 passed succesfully')
    return True


def us01(individuals,families):
    for individual_person in individuals:
            birthdate = individual_person.birthday.split("/")
            date_of_birth = date(
                            int(birthdate[0]),
                            int(birthdate[1]),
                            int(birthdate[2]))
            if(date.today() < date_of_birth):
                print('Birthday cannot be before today')
                return False


            if individual_person.deathday != "NA":
                deathdate = individual_person.deathday.split("/")
                date_of_death = date(
                            int(deathdate[0]),
                            int(deathdate[1]),
                            int(birthdate[2]))
                if(date.today() < date_of_death):
                    print('Error: deathday cannot be before today')
                    return False

    for family in families:
        for individual in individuals:
            if(individual.id == family.husbandId or individual.id == family.wifeId):
                if family.married != "NA":
                    marrieddate = family.married.split("/")
                    date_of_marriage = date(
                            int(marrieddate[0]),
                            int(marrieddate[1]),
                            int(marrieddate[2]))
                    if(date.today() < date_of_marriage):
                        print('Error : Married day cannot be before today')
                        return False
                if family.divorced != "NA":
                    divorceddate = family.divorced.split("/")
                    date_of_divorce = date(
                            int(divorceddate[0]),
                            int(divorceddate[1]),
                            int(divorceddate[2]))
                    if(date.today() < date_of_divorce):
                        print('Error: Divorced day cannot be before today')
                        return False
    print('Test 1 Successfully Passed.')
    return True

#Sprint 2 - Parth Patel
def us02(individuals,families):
    for family in families:
        for individual in individuals:
            if(individual.id == family.husbandId or individual.id == family.wifeId):
                birthdate = individual.birthday.split("/")
                date_of_birth = date(
                                int(birthdate[0]),
                                int(birthdate[1]),
                                int(birthdate[2]))
                marrieddate = family.married.split("/")
                date_of_marriage = date(
                        int(marrieddate[0]),
                        int(marrieddate[1]),
                        int(marrieddate[2]))              

                if(date_of_birth > date_of_marriage):
                    print('Birth should occur before marriage of an individual {}'.format(individual.id))
                    return False
    print('Test 2 Successfully Passed.')                
    return True

def us03(individuals,families):
    for individual in individuals:
        birthdate = individual.birthday.split("/")
        date_of_birth = date(
                        int(birthdate[0]),
                        int(birthdate[1]),
                        int(birthdate[2]))
        
        if individual.alive == False:
            deathdate = individual.deathday.split("/")
            date_of_death = date(
                        int(deathdate[0]),
                        int(deathdate[1]),
                        int(deathdate[2]))
            if date_of_birth > date_of_death:
                print('Error : Birth should be before death of an individual.')
                return False
                
    print('Test 3 passed succesfully')
    return True
#Sprint 3 - Parth Patel
def us05(individuals,families):
    for i in range(len(families)):
        for j in range(len(individuals)):
            if(individuals[j].id == families[i].husbandId or individuals[j].id == families[i].wifeId):
                if(individuals[j].alive == False):
                    deathdate = individuals[j].deathday.split("/")
                    date_of_death = date(
                                int(deathdate[0]),
                                int(deathdate[1]),
                                int(deathdate[2]))
                    marrieddate = families[i].married.split("/")
                    date_of_marriage = date(
                            int(marrieddate[0]),
                            int(marrieddate[1]),
                            int(marrieddate[2]))
                    if(date_of_death < date_of_marriage):
                        print("Error: Marriage should occur before death.")
                        return False
    print("Test 5 passes successfully")                    
    return True

def us06(individuals,families):
    for i in range(len(families)):
        for j in range(len(individuals)):
            if(individuals[j].id == families[i].husbandId or individuals[j].id == families[i].wifeId):
                if(families[i].divorced != "NA"):
                    divorceddate = families[i].divorced.split("/")
                    date_of_divorce = date(
                            int(divorceddate[0]),
                            int(divorceddate[1]),
                            int(divorceddate[2]))
                    if(individuals[j].alive == False):
                        deathdate = individuals[j].deathday.split("/")
                        date_of_death = date(
                                    int(deathdate[0]),
                                    int(deathdate[1]),
                                    int(deathdate[2]))
                        if(date_of_divorce > date_of_death):
                            print("Error: Divorce should occur before the death of individuals.")
                            return False
    print("Test 6 passed successfully")
    return True
#Sprint-4 Parth Patel
def us10(individuals,families):   
    for family in families:
        if(family.married != "NA"):
            marrieddate = family.married.split("/")
            date_of_marriage = date(
                    int(marrieddate[0]),
                    int(marrieddate[1]),
                    int(marrieddate[2]))
        for individual in individuals:            
            birthdate = individual.birthday.split("/")
            date_of_birth = date(
                            int(birthdate[0]),
                            int(birthdate[1]),
                            int(birthdate[2]))
            if (family.married != "NA" and individual.id == family.husbandId and date_of_marriage.year - date_of_birth.year < 14):
                print("Husband Birthdate is less than 14 years of Marriage Date")
                return False
            if (family.married != "NA" and individual.id == family.wifeId and date_of_marriage.year - date_of_birth.year < 14):
                print("Wife Birthdate is less than 14 years of Marriage Date.")
                return False
    print("Test 10 passed successfully")
    return True

def us08(individuals, families):
    for individual in individuals:
        birthdate = individual.birthday.split("/")
        date_of_birth = date(
                        int(birthdate[0]),
                        int(birthdate[1]),
                        int(birthdate[2]))
        for family in families:
            if individual.id in family.childrenId:
                marrieddate = family.married.split("/")
                date_of_marriage = date(
                        int(marrieddate[0]),
                        int(marrieddate[1]),
                        int(marrieddate[2]))
                if(date_of_birth > date_of_marriage):
                    print("Children birthday should be after marriage of parents.")
                    return False
    print("Test 8 passed successfully")
    return True

#Gautham Prem Krishnan
def us14(individuals,families):
        for family in families:
            for indiv in individuals:
                count = 0
                if indiv.id in family.childrenId:
                    if len(family.childrenId) <= 5:
                        break
                    else:
                        for child in family.childrenId:
                            for i in individuals:
                                if (child==i.id):
                                    temp_birth = indiv.birth.split("/")
                                    indiv_birth=date(
                                    int(temp_birth[0]),
                                    int(temp_birth[1]),
                                    int(temp_birth[2]))
                                    temp_child = i.birth.split("/")
                                    child_birth=date(
                                    int(temp_child[0]),
                                    int(temp_child[1]),
                                    int(temp_child[2]))
                                    check_birth = abs( (indiv_birth - child_birth).days ) < 2
                                    if check_birth:
                                        count+=1
                                        if count>5:
                                            print("No more than five siblings should be born at the same time")
                                            return False                                            
        print('Test 14 passed succesfully')
        return True

#Gautham Prem Krishnan
def us15(individuals,families):
        table_value_one = families
        table_value_zero = individuals
        for family in table_value_one:
            for indiv in table_value_zero:
                if indiv.id in family.childrenId:
                    if (len(family.childrenId)<15):
                        print('Test 15 passed succesfully')
                        return True
                    elif (len(family.childrenId) >= 15):
                        print("There should be fewer than 15 siblings in a family")
                        return False
        
        print('Test 15 passed succesfully')
        return True

#Gautham Prem Krishnan
def us16(individuals,families):
        for family in families:
            flag = False
            for indiv in individuals:
                if(family.husbandId == indiv.id):
                    temp_family_name = indiv.name.split("/")
                    last_name = temp_family_name[1]
                    flag = True
                if (indiv.gender == "M" and indiv.name.split("/")[1] != last_name and flag == True):
                    print('All male members of a family should have the same last name')
                    return    
        print('Test 16 passed successfully')
        return True

#Gautham Prem Krishnan   
def us30(individuals):
        for indiv in individuals:
            if (indiv.deathday == "N/A" and indiv.spouse != "N/A"):
                married_list = f"Test case US30: {indiv.name} ({indiv.id}) is alive and married"
                return(married_list)
            else:

                print('Test 30 had no living married people')
                print('Test 30 passed successfully')
                return True
        print('Test 30 passed successfully')
        return True

def us31(individuals,families):
        for family in families:
            for indiv in individuals:
                if (family.husbandName == "N/A" and family.wife.age > 30 and family.wife.alive):
                    print("into loop")
                    info = f"Story US31: {indiv.name} ({indiv.id}) is over 30 years old at {indiv.age} and not married"
                    print(info)
                    return info
                else:
                    print('Test 31 passed successfully')
                    return True

    # #User story 32 - List all multiple births in a GEDCOM file
def us32(families):
        for family in families:
            leng_value = len(family.childrenId)
            if (leng_value > 1):
                info = f"Story US32: Family {family.id} has multiple births ({leng_value}) on line "
                print(info)
                return info
            else:
                print('Test 32 passed successfully')
                return True
