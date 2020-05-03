import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test case to test the behavior of the Sources class
    '''
    def setUp(self):
        '''
        Setup function that will run before every test
        '''
        self.new_source = Source('mynews','My News','We have the latest updates','https://google.com','general','ke')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_to_check_instance_variables(self):
        '''
        Test function to check instance variables
        '''
        self.assertEquals(self.new_source.id,'mynews')
        self.assertEquals(self.new_source.name,'My News')
        self.assertEquals(self.new_source.description,'We have the latest updates')
        self.assertEquals(self.new_source.url,'https://google.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'ke')

if __name__ == '__main__':
    manager.run()