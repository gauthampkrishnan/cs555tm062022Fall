import unittest
import gedcom_parser
# from dateutil.parser import *
import datetime
from datetime import date
from gedcom_parser import p_table, f_table


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


#print(p_table)
#print(f_table)
class TestGedcomFile(unittest.TestCase):
#User story 13 - Birth dates of siblings should be more than 8 months apart or less than 2 days apart (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
    def test_us_13(self):
        for family in table[1]:
            for indiv in table[0]:
                if indiv.id in family.children:
                    if len(family.children) >= 2:
                        for child in family.children:
                            for i in table[0]:
                                if (child==i.id):
                                    temp_birth = indiv.birth.split(" ")
                                    indiv_birth = datetime.datetime(int(temp_birth[2]), month_dict[temp_birth[1]], int(temp_birth[0]))
                                    temp_child = i.birth.split(" ")
                                    child_birth = datetime.datetime(int(temp_child[2]), month_dict[temp_child[1]], int(temp_child[0]))
                                    check_birth = abs((indiv_birth.year - child_birth.year)*12 + (indiv_birth.month - child_birth.month)) > 8 or abs( (indiv_birth - child_birth).days ) < 2
                                    if not check_birth:
                                        print("Children should be born more than 8 months apart or less than 2 days apart")
        print('Test 13 passed succesfully')
    def test_us_29(self):
        for indiv in table[0]:
            if (indiv.death != "N/A"):
                death_list = f"Test 29: {indiv.name} ({indiv.id}) is deceased"
                print(death_list)
                return(death_list)
            else:
                print('Test 29 passed successfully')
                return
if __name__ == '__main__':
    unittest.main()