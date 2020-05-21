import unittest
import functions

file_test = ["TOA5", "CHUI 1", "CR1000", "54696",
             "CR1000.Std.27.04", "CPU:Estacv03_CHUI 1.CR1", "35897", "Table1"]


class TestFunctions(unittest.TestCase):

    def test_type_not_files(self):
        self.assertFalse(
            expr=(file_test == functions.read_files(self, 'C:\Developer\dataAnalytics\dados')))

    def test_out_read_files(self):
        self.assertIs(type(functions.read_files(
            self, 'C:\Developer\dataAnalytics\dados')), type(file_test))
