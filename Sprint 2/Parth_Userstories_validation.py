import datetime
from datetime import date
# from prettytable import PrettyTable
from datetime import datetime

#Sprint 1 - Parth Patel
def us07(details):
    for individual_person in details[0]:
        birthdate = individual_person.birth.split()
        date_of_birth = date(
                            int(birthdate[2]),
                            datetime.strptime(birthdate[1], '%b').month,
                            int(birthdate[0]))
        isalive = individual_person.alive
        if(isalive == 'True'):
            checkBirthDate = date.today() - date_of_birth
            if(checkBirthDate > 150):
                print("ERROR: INDIVIDUAL: US07: More than 150 years old - Birth date {}".format(birthdate))
                return  False          
        else:
            deathdate = individual_person.death.split()
            date_of_death = date(
                            int(deathdate[2]),
                            datetime.strptime(deathdate[1], '%b').month,
                            int(birthdate[0]))
            checkDeathDate = date_of_death.year - date_of_birth.year
            if checkDeathDate > 150:
                print("ERROR: INDIVIDUAL: US07: More than 150 years old at Death - Birth {} : Death {}".format(birthdate,deathdate))
                return False           
    print('Test 7 passed succesfully')
    return True


def us01(details):
    for individual_person in details[0]:
            # self.assertNotEqual(person.birthday, None, "Error: Birthday cannot be None")
            birthdate = individual_person.birth.split(" ")
            date_of_birth = date(
                            int(birthdate[2]),
                            datetime.strptime(birthdate[1], '%b').month,
                            int(birthdate[0]))
            if(date.today() < date_of_birth):
                print('Birthday cannot be before today')
                return False

            #self.assertLess(birthday, today, "Error: Birthday cannot be before today")

            if individual_person.death != "N/A":
                deathdate = individual_person.death.split()
                date_of_death = date(
                            int(deathdate[2]),
                            datetime.strptime(deathdate[1], '%b').month,
                            int(birthdate[0]))
                if(date.today() < date_of_death):
                    print('Error: deathday cannot be before today')
                    return False
                # self.assertLess(deathDay, today, "Error: deathday cannot be before today")

    for family in details[1]:
        for individual in details[0]:
            if(individual.id == family.husband or individual.id == family.wife):
                if family.married != "N/A":
                    marrieddate = family.married.split(" ")
                    date_of_marriage = date(
                            int(marrieddate[2]),
                            datetime.strptime(marrieddate[1], '%b').month,
                            int(marrieddate[0]))
                    if(date.today() < date_of_marriage):
                        print('Error : Married day cannot be before today')
                        return False
                    # self.assertLess(marriedDay, today, "Error: Married day cannot be before today")
                if family.divorced != "N/A":
                    divorceddate = family.divorced.split(" ")
                    date_of_divorce = date(
                            int(divorceddate[2]),
                            datetime.strptime(divorceddate[1], '%b').month,
                            int(divorceddate[0]))
                    if(date.today() < date_of_divorce):
                        print('Error: Divorced day cannot be before today')
                        return False
                    # self.assertLess(divorcedDay, today, "Error: Divorced day cannot be before today")
    print('Test 1 Successfully Passed.')
    return True

#Sprint 2 - Parth Patel
def us02(details):
    for family in details[1]:
        for individual in details[0]:
            if(individual.id == family.husband or individual.id == family.wife):
                birthdate = individual.birth.split(" ")
                date_of_birth = date(
                                int(birthdate[2]),
                                datetime.strptime(birthdate[1], '%b').month,
                                int(birthdate[0]))
                marrieddate = family.married.split(" ")
                date_of_marriage = date(
                        int(marrieddate[2]),
                        datetime.strptime(marrieddate[1], '%b').month,
                        int(marrieddate[0]))
                

                if(date_of_birth > date_of_marriage):
                    print('Birth should occur before marriage of an individual')
                    return False
    print('Test 2 Successfully Passed.')                
    return True

def us03(details):
    for individual in details[0]:
        birthdate = individual.birth.split(" ")
        date_of_birth = date(
                        int(birthdate[2]),
                        datetime.strptime(birthdate[1], '%b').month,
                        int(birthdate[0]))
        
        if individual.death is not None:
            deathdate = individual.death.split()
            date_of_death = date(
                        int(deathdate[2]),
                        datetime.strptime(deathdate[1], '%b').month,
                        int(birthdate[0]))
            if date_of_birth > date_of_death:
                print('Error : Birth should be before death of an individual.')
                return False
                
    print('Test 3 passed succesfully')
    return True