'''
Created on Jan 12, 2013

@author: dirk dierickx
'''
import re


class Parser(object):
    '''
    Parser to remove all kinds of wiki markup tags from an object
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def __parse(self, text=''):
        '''
        Parse any string to remove all wiki markup tags
        '''
        self.text = text
        self.text = re.sub('[\s\w]+\|', '', self.text)
        self.text = re.sub('[\[\]]', '', self.text)
        return self.text

    def parse_string(self, string=''):
        '''
        Parse a string object to de-wikified text
        '''
        return self.__parse(string)

    def parse_byte(self, byte=None):
        '''
        Parse a byte object to de-wikified text
        '''
        pass

    def parse_file(self, file=None):
        '''
        Parse the content of a file to de-wikified text
        '''
        pass
