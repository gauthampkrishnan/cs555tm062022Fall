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
 #User story 21 - Husband in family should be male and wife in family should be female
    def test_us_21(self):
        for family in table[1]:
            for indiv in table[0]:
                if(family.husband == indiv.id):
                    if(indiv.gender != 'M'):
                        print('Husband in family should be male')
                if(family.wife == indiv.id):
                    if(indiv.gender != 'F'):
                        print('Wife in family should be female')
        print("Test 21 passed successfully")


    #User story 23 - No more than one individual with the same name and birth date should appear in a GEDCOM file
    def test_us_23(self):
        unique = []
        for indiv in table[0]:
            if [indiv.name, indiv.birth] not in unique:
                unique.append([indiv.name, indiv.birth])
            else:
                print("No more than one individual with the same name and birth date should appear in a GEDCOM file")
                return
        print('Test 23 passed successfully')


if __name__ == '__main__':
    unittest.main()

