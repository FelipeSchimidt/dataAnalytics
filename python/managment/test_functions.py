from functions import Managment_functions
import unittest

file_test = '"TOA5","CHUI 1","CR1000","54696","CR1000.Std.27.04","CPU:Estacv03_CHUI 1.CR1","35897","Table1"'


class TestFunctions(unittest.TestCase):

    def test_type_files(self):
        self.assertTrue(Managment_functions.read_files(
            self, 'C://Developer//ataAnalytics//dados//arquivo_teste_02.wnd') == 'str')
