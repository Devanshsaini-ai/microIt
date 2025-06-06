# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 21:56:12 2025

@author: Acer
"""

import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    # Start with lowercase letters
    characters = list(string.ascii_lowercase)
    
    if use_upper:
        characters.extend(string.ascii_uppercase)
    if use_digits:
        characters.extend(string.digits)
    if use_special:
        characters.extend(string.punctuation)

    # Make sure the character pool isn't empty
    if not characters:
        raise ValueError("No character types selected for password generation.")

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    password = generate_password(length=16, use_upper=True, use_digits=True, use_special=True)
    print("Generated password:", password)
