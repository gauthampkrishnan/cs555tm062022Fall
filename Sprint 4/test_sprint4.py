from tkinter.font import families
import unittest
# from dateutil.parser import *
import datetime
from datetime import date
from datetime import datetime
import gedcom_parser
# from gedcom_parser import us02, us07, us01
from Userstories_validation import us02, us03, us07, us01, us05, us06,us10,us08,us14,us15,us16,us30,us31,us32
# from gedcom_parser import p_table, f_table



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
        self.assertTrue(us02(individuals,families))

    def test_us03(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us03(individuals,families))

    def test_us05(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us05(individuals,families))

    def test_us06(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us06(individuals,families))
        
    def test_us10(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us10(individuals,families))
    
    def test_us08(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertFalse(us08(individuals,families))
    
    def test_us14(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us14(individuals,families))

        
    def test_us15(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us15(individuals,families))
    
    def test_us16(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us16(individuals,families))

    def test_us30(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us30(individuals))
    
    def test_us31(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us31(individuals,families))

    def test_us32(self):
        individuals = gedcom_parser.individual_parser("gedcom_test.ged")
        families = gedcom_parser.family_parser("gedcom_test.ged")
        self.assertTrue(us32(families))



if __name__ == '__main__':
    unittest.main()
