import os
import unittest
from aiopg.connection import get_psycopg2_module

__author__ = 'nick'


class AioPgTestCase(unittest.TestCase):
    def setUp(self):
        self.psycopg2_module_name = os.environ.get('PSYCOPG2_MODULE_NAME',
                                                   'psycopg2')
        print(self.psycopg2_module_name)
        self.psycopg2_module = get_psycopg2_module(self.psycopg2_module_name)