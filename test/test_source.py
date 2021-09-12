import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    '''
     Test class to test the behaviour of the class Source
    '''

    def setUp(self):
        '''
         Set up method that will run the first before every test
        '''

        self.new_source('bbc','BBC'T,'DESCRIPTION','URL')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))