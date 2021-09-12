import unittest
from app.models import Headlines

class HeadlinesTest(unittest.TestCase):
    '''
     Test Class to test thr behaviour of the class Headlines
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_headlines = Headlines('the joke of day','the president of Kenya says he wants to rename kenya to Kenyatta haha!','september 12-12:33am','link','image.jpg')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_headlines,Headlines))