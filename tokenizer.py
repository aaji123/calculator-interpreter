import re

def tokenize(expression):
    #token patterns with named groups
    token_patterns = [
        ('NUMBER', r'(\d+(\.\d*)?|\.\d+)'),
        
    ]