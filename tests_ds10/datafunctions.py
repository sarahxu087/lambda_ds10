import string
import numpy as np


def increment(x):
     """A function that calculate the increment"""
    return(x + 1)
    
def strip_punctuation(text):
    """A function strip the punctutaion"""
    exclude = string.punctuation
    return ''.join(s for s in text if s not in exclude)
