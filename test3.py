
from test2 import enumerate_directories


import pytest

class TestEnumerateDirectories:


    def test_valid_url_and_wordlist(self):
    
        url = "https://www.google.com"
        wordlist_path = "wordlist dirb.txt"
        stop_enumeration = False
    
        
        enumerate_directories(url, wordlist_path, stop_enumeration)
        

    
    def test_directory_not_found(self):
    
        url = "https://www.google.com"
        wordlist_path = "wordlist dirb.txt"
        stop_enumeration = False
    
        
        enumerate_directories(url, wordlist_path, stop_enumeration)
    
    