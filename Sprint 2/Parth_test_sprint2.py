from tkinter.font import families
import unittest
# from dateutil.parser import *
import datetime
from datetime import date
from datetime import datetime
import gedcom_parser
# from gedcom_parser import us02, us07, us01
from Parth_Userstories_validation import us02, us03, us07, us01




individuals = gedcom_parser.individual_parser("gedcom_test.ged")
families = gedcom_parser.family_parser("gedcom_test.ged")


class TestGedcomFile(unittest.TestCase):

    def test_us07(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us07(individuals,families))

    def test_us01(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us01(individuals,families))

    def test_us02(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertFalse(us02(individuals,families))

    def test_us03(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertFalse(us03(individuals,families))


if __name__ == '__main__':
    unittest.main()
