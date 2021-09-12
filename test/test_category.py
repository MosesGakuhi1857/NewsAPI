import unittest
from app.models import Category

class CategoryTest(unittest.TestCase):
    '''
    Test Class to test thr behaviour of the class Category
    '''

    def setUp(self):
        '''
        Set up method that will run the test before every test
        '''
        self.new_category = Category('the joke of day','the president of Kenya says he wants to rename kenya to Kenyatta haha!','september 12-12:33am','link','image.jpg')
    
    def test_instance(self):

        self.assertTrue(isinstance(self.new_category,Category))