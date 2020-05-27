import unittest
from functions import read_files

file_test = ["TOA5", "CHUI 1", "CR1000", "54696",
             "CR1000.Std.27.04", "CPU:Estacv03_CHUI 1.CR1", "35897", "Table1"]


class TestFunctions(unittest.TestCase):

    def test_type_files_list(self):
        self.assertFalse(type(read_files(
            'c://Developer//dataAnalytics//dados//arquivo_teste_02.wnd')) == 'list')
