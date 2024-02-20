

from subdomain import enumerate_subdomains


import pytest

class TestEnumerateSubdomains:

    
    def test_open_wordlist_file(self, capsys):
    
        domain = "example.com"
        wordlist_path = "wordlist.txt"

        
        enumerate_subdomains(domain, wordlist_path)

        
        captured = capsys.readouterr()
        assert "Starting subdomain enumeration..." in captured.out
        assert "Wordlist file not found." in captured.out

    def test_construct_url_with_capsys(self, capsys):
        
        domain = "example.com"
        wordlist_path = "wordlist.txt"

        
        enumerate_subdomains(domain, wordlist_path)

       
        captured = capsys.readouterr()
        assert "http://subdomain1.example.com" not in captured.out
        assert "http://subdomain2.example.com" not in captured.out
        assert "http://subdomain3.example.com" not in captured.out
        assert "Wordlist file not found." in captured.out

    
    def test_send_get_request(self, capsys):
        
        domain = "example.com"
        wordlist_path = "wordlist.txt"

        
        enumerate_subdomains(domain, wordlist_path)

        captured = capsys.readouterr()
        assert "Starting subdomain enumeration..." in captured.out
        assert "Wordlist file not found." in captured.out

    def test_empty_wordlist_file(self, capsys):
        
        domain = "example.com"
        wordlist_path = "empty_wordlist.txt"

    
        enumerate_subdomains(domain, wordlist_path)

      
        captured = capsys.readouterr()
        assert "Starting subdomain enumeration..." in captured.out
        assert "Found:" not in captured.out

  
    def test_whitespace_wordlist_file(self, capsys):
       
        domain = "example.com"
        wordlist_path = "whitespace_wordlist.txt"

      
        enumerate_subdomains(domain, wordlist_path)

    
        captured = capsys.readouterr()
        assert "Starting subdomain enumeration..." in captured.out
        assert "Found:" not in captured.out

    def test_long_subdomain_wordlist_file(self, capsys):
    
        domain = "example.com"
        wordlist_path = "long_subdomain_wordlist.txt"

        
        enumerate_subdomains(domain, wordlist_path)

       
        captured = capsys.readouterr()
        assert "Starting subdomain enumeration..." in captured.out
        assert "Found:" not in captured.out