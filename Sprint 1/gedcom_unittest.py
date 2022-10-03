import unittest
import gedcom_parser
# from dateutil.parser import *
import datetime
from datetime import date
from gedcom_parser import p_table, f_table

table = gedcom_parser.gedcom_table("gedcom_test.ged")
month_dict = {"JAN": 1,"FEB": 2,"MAR": 3,"APR": 4,"MAY": 5,"JUN": 6,"JUL": 7,"AUG": 8,"SEP": 9,"OCT": 10,"NOV": 11,"DEC": 12}

print(p_table)
print(f_table)

class TestGedcomFile(unittest.TestCase):
    #User story 9 - Child should be born before death of mother and before 9 months after death of father
    def test_us_9(self):
        for family in table[1]:
            for indiv in table[0]:
                if (family.children == indiv.id):
                    temp_child_birth = indiv.birth.split(" ")
                    for indiv in table[0]:
                        if(indiv.id == family.wife or indiv.id == family.husband):
                            if(indiv.id == family.wife):
                                temp_wife = indiv.birth.split(" ")
                                temp_alive = indiv.alive
                                if(temp_alive == 'False'):
                                    temp_death = indiv.death.split(" ")
                                    checkBirthDate = datetime.datetime(int(temp_child_birth[2]), int(month_dict[temp_child_birth[1]]), int(temp_child_birth[0])) < datetime.datetime(int(temp_death[2]), int(month_dict[temp_death[1]]), int(temp_death[0]))
                                    if(not checkBirthDate):
                                        print("Child should be born before death of mother and before 9 months after death of father")
                                        return
                                else:
                                    checkWife = datetime.datetime(int(temp_child_birth[2]), int(month_dict[temp_child_birth[1]]), int(temp_child_birth[0]))<datetime.datetime(int(temp_wife[2]), int(month_dict[temp_wife[1]]), int(temp_wife[0]))
                                    if(not checkWife):
                                        print("Child should be born before death of mother and before 9 months after death of father")
                                        return
                            else:
                                temp_husband = indiv.birth.split(" ")
                                temp_alive = indiv.alive
                                if(temp_alive == 'False'):
                                    temp_death = indiv.death.split(" ")
                                    if (month_dict[temp_death[1]] + 9 > 12):
                                        month_dict[temp_death[1]] = month_dict[temp_death[1]] + 9
                                        month_dict[temp_death[1]] = month_dict[temp_death[1]] - 12
                                        temp_death[2] = int(temp_death[2]) + 1
                                    checkBirthDate = datetime.datetime(int(temp_child_birth[2]), int(month_dict[temp_child_birth[1]]), int(temp_child_birth[0])) < datetime.datetime(int(temp_death[2]), int(month_dict[temp_death[1]]), int(temp_death[0]))
                                    if(not checkBirthDate):
                                        print("Child should be born before death of mother and before 9 months after death of father")
                                        return
                                else:
                                    checkWife = datetime.datetime(int(temp_child_birth[2]), int(month_dict[temp_child_birth[1]]), int(temp_child_birth[0]))<datetime.datetime(int(temp_husband[2]), int(month_dict[temp_husband[1]]), int(temp_husband[0]))
                                    if(not checkWife):
                                        print("Child should be born before death of mother and before 9 months after death of father")
                                        return
        print('Test 9 passed succesfully')

        
    def test_us_38(self):
        list_recent = []
        for indiv in table[0]:
            if (indiv.alive=='True'):
                temp_birth = indiv.birth.split(" ")
                indiv_birth = datetime.datetime(int(temp_birth[2]), month_dict[temp_birth[1]], int(temp_birth[0]))
                recent_birth = datetime.datetime.now()
                check_recent = (indiv_birth - recent_birth).days < 30
                if (check_recent):
                    list_recent.append(indiv.name)

        if not list_recent:
            print(f"Story US38: No living people whose birthdays occur in the next 30 days")
        else:
            for i in list_recent:
                print(i)
        print('Test 38 passed succesfully')

if __name__ == '__main__':
    unittest.main()

 
