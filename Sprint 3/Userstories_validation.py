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
            # checkBirthDate = date.today() - date_of_birth
            if(individual_person.age > 150):
                print("ERROR: INDIVIDUAL: US07: More than 150 years old - Birth date {}".format(birthdate))
                return  False          
        else:
            deathdate = individual_person.deathday.split("/")
            date_of_death = date(
                            int(deathdate[0]),
                            int(deathdate[1]),
                            int(birthdate[2]))
            # checkDeathDate = date_of_death.year - date_of_birth.year
            if individual_person.age > 150:
                print("ERROR: INDIVIDUAL: US07: More than 150 years old at Death - Birth {} : Death {}".format(birthdate,deathdate))
                return False           
    print('Test 7 passed succesfully')
    return True


def us01(individuals,families):
    for individual_person in individuals:
            # self.assertNotEqual(person.birthday, None, "Error: Birthday cannot be None")
            birthdate = individual_person.birthday.split("/")
            date_of_birth = date(
                            int(birthdate[0]),
                            int(birthdate[1]),
                            int(birthdate[2]))
            if(date.today() < date_of_birth):
                print('Birthday cannot be before today')
                return False

            #self.assertLess(birthday, today, "Error: Birthday cannot be before today")

            if individual_person.deathday != "NA":
                deathdate = individual_person.deathday.split("/")
                date_of_death = date(
                            int(deathdate[0]),
                            int(deathdate[1]),
                            int(birthdate[2]))
                if(date.today() < date_of_death):
                    print('Error: deathday cannot be before today')
                    return False
                # self.assertLess(deathDay, today, "Error: deathday cannot be before today")

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
                    # self.assertLess(marriedDay, today, "Error: Married day cannot be before today")
                if family.divorced != "NA":
                    divorceddate = family.divorced.split("/")
                    date_of_divorce = date(
                            int(divorceddate[0]),
                            int(divorceddate[1]),
                            int(divorceddate[2]))
                    if(date.today() < date_of_divorce):
                        print('Error: Divorced day cannot be before today')
                        return False
                    # self.assertLess(divorcedDay, today, "Error: Divorced day cannot be before today")
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
                    print('Birth should occur before marriage of an individual')
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
month_dict = {"JAN": 1,
            "FEB": 2,
            "MAR": 3,
            "APR": 4,
            "MAY": 5,
            "JUN": 6,
            "JUL": 7,
            "AUG": 8,
            "SEP": 9,
            "OCT": 10,
            "NOV": 11,
            "DEC": 12}
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
                                    temp_birth = indiv.birth.split(" ")
                                    indiv_birth = datetime.datetime(int(temp_birth[2]), month_dict[temp_birth[1]], int(temp_birth[0]))
                                    temp_child = i.birth.split(" ")
                                    child_birth = datetime.datetime(int(temp_child[2]), month_dict[temp_child[1]], int(temp_child[0]))
                                    check_birth = abs( (indiv_birth - child_birth).days ) < 2
                                    if check_birth:
                                        count+=1
                                        if count>5:
                                            print("No more than five siblings should be born at the same time")
                                            return
        print('Test 14 passed succesfully')
#Gautham Prem Krishnan
def us15(individuals,families):
        table_value_one = families
        table_value_zero = individuals
        for family in table_value_one:
            for indiv in table_value_zero:
                if indiv.id in family.childrenId:
                    if len(family.childrenId) >= 15:
                        print("There should be fewer than 15 siblings in a family")
                        return
        print('Test 15 passed succesfully')