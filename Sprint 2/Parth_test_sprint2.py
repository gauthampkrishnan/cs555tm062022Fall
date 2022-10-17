import unittest
# from dateutil.parser import *
import datetime
from datetime import date
from datetime import datetime
import gedcom_parser
# from gedcom_parser import us02, us07, us01
from Parth_Userstories_validation import us02, us03, us07, us01
from gedcom_parser import p_table, f_table



details = gedcom_parser.gedcom_table("gedcom_test.ged")


print("Individual")
print(p_table)
print("Families")
print(f_table)

class TestGedcomFile(unittest.TestCase):

    def test_us07(self):
        details = gedcom_parser.gedcom_table("gedcom_test.ged")
        self.assertTrue(us07(details))

    def test_us01(self):
        details = gedcom_parser.gedcom_table("gedcom_test.ged")
        self.assertTrue(us01(details))

    def test_us02(self):
        details = gedcom_parser.gedcom_table("gedcom_test.ged")
        self.assertTrue(us02(details))

    def test_us03(self):
        details = gedcom_parser.gedcom_table("gedcom_test.ged")
        self.assertTrue(us03(details))




if __name__ == '__main__':
    unittest.main()
