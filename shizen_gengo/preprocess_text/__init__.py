"""
this text is in shizen_gengo/preprocess_text/init.py
"""
from .nltkmodules import *
from .text_utils import remove_nl_cr, remove_digits, remove_non_char, custom_replace, remove_url, remove_email, \
                   remove_consecutive_spaces, remove_stopwords, remove_accented_chars, remove_punctuation

__all__ = ['remove_nl_cr', 'remove_digits', 'remove_non_char', 'custom_replace', 'remove_url', 'remove_email',
           'remove_consecutive_spaces', 'remove_stopwords', 'remove_accented_chars', 'remove_punctuation']