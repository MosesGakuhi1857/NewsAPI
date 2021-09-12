import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
     Test class to test the behaviour of the article class
    '''

    def setUp(self):
        '''
         set up method that will run before every test
        '''

        self.new_article = Article('the joke of day','the president of Kenya says he wants to rename kenya to Kenyatta haha!','september 12-12:33am','link','image.jpg')

    def test_instance(self):
        
        self.assertTrue(isinstance(self.new_article,Article))