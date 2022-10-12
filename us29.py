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


print(p_table)
print(f_table)
def test_us_29(self):
        for indiv in table[0]:
            if (indiv.death != "N/A"):
                death_list = f"Test 29: {indiv.name} ({indiv.id}) is deceased"
                print(death_list)
                return(death_list)
            else:
                print('Test 29 passed successfully')
                return
