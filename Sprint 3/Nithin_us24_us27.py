import unittest
import gedcom_parser
# from dateutil.parser import parse
import datetime
from datetime import date, timedelta
from gedcom_parser import Individual, p_table, f_table, Family


table = gedcom_parser.gedcom_table("gedcom_test.ged")
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


# print(p_table)
# print(f_table)

class TestGedcomFile(unittest.TestCase):

#User story 24 - No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file
    def test_us_24(self):
        unique = []
        for family in table[1]:
            if [family.husband, family.wife, family.married] not in unique:
                unique.append([family.husband, family.wife, family.married])
            else:
                print("No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file")

    #User story 27 - List individuals with age
    def test_us_27(self):
        listOfNames = []
        for indiv in table[0]:
            temp_alive = indiv.alive
            temp_birth = indiv.birth.split(" ")
            if(temp_alive == 'False'):
                temp_death = indiv.death.split(" ")
                checkBirthDate = datetime.datetime(int(temp_death[2]), int(month_dict[temp_death[1]]), int(temp_death[0])) - datetime.datetime(int(temp_birth[2]), int(month_dict[temp_birth[1]]), int(temp_birth[0]))
                age = str(int(checkBirthDate.total_seconds()/(3600*24*365)))
                listOfNames.append(indiv.name + ", Age: " + age)
            else:
                checkBirthDate = datetime.datetime.now() - datetime.datetime(int(temp_birth[2]), int(month_dict[temp_birth[1]]), int(temp_birth[0]))
                age = str(int(checkBirthDate.total_seconds()/(3600*24*365)))
                listOfNames.append(indiv.name + ", Age: " + age)
        print(listOfNames)
        print("Test 27 passed successfully")


if __name__ == '__main__':
    unittest.main()