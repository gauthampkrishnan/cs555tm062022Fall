import unittest
import gedcom_parser
# from dateutil.parser import *
import datetime
from datetime import date
from datetime import datetime



details = gedcom_parser.gedcom_table("gedcom_test.ged")


# print("Individual")
# print(p_table)
# print("Families")
# print(f_table)

class TestGedcomFile(unittest.TestCase):

    def test_us07(self):
        for individual_person in details[0]:
            birthdate = individual_person.birth.split()
            date_of_birth = date(
                                int(birthdate[2]),
                                datetime.strptime(birthdate[1], '%b').month,
                                int(birthdate[0]))
            isalive = individual_person.alive
            if(isalive == 'True'):
                checkBirthDate = date.today().year - date_of_birth.year
                # self.assertLess(checkBirthDate, 150, "ERROR: INDIVIDUAL: US07: More than 150 years old - Birth date {}".format(birthdate))
                if(checkBirthDate > 150):
                    print("ERROR: INDIVIDUAL: US07: More than 150 years old - Birth date {}".format(birthdate))
                    return            
            else:
                deathdate = individual_person.death.split()
                date_of_death = date(
                                int(deathdate[2]),
                                datetime.strptime(deathdate[1], '%b').month,
                                int(birthdate[0]))
                checkDeathDate = date_of_death.year - date_of_birth.year
                # self.assertLess(checkDeathDate, 150, "ERROR: INDIVIDUAL: US07: More than 150 years old at Death - Birth {} : Death {}".format(birthdate,deathdate))
                if checkDeathDate > 150:
                    print("ERROR: INDIVIDUAL: US07: More than 150 years old at Death - Birth {} : Death {}".format(birthdate,deathdate))
                    return            
        print('Test 7 passed succesfully')


    def test_date_before_current(self):
        for individual_person in details[0]:
                
                birthdate = individual_person.birth.split(" ")
                date_of_birth = date(
                                int(birthdate[2]),
                                datetime.strptime(birthdate[1], '%b').month,
                                int(birthdate[0]))
                

                if individual_person.death != "N/A":
                    deathdate = individual_person.death.split()
                    date_of_death = date(
                                int(deathdate[2]),
                                datetime.strptime(deathdate[1], '%b').month,
                                int(birthdate[0]))
                    

        for family in details[1]:
            for individual in details[0]:
                if(individual.id == family.husband or individual.id == family.wife):
                    if family.married != "N/A":
                        marrieddate = family.married.split(" ")
                        date_of_marriage = date(
                                int(marrieddate[2]),
                                datetime.strptime(marrieddate[1], '%b').month,
                                int(marrieddate[0]))
                        
                    if family.divorced != "N/A":
                        divorceddate = family.divorced.split(" ")
                        date_of_divorce = date(
                                int(divorceddate[2]),
                                datetime.strptime(divorceddate[1], '%b').month,
                                int(divorceddate[0]))
                        


if __name__ == '__main__':
    unittest.main()
