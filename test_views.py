from simple_server.simple_server.views import NLPModel
import pytest
import pandas as pd

def test_connection():
    assert NLPModel()

def test_remove_RT_user():
    nlp = NLPModel()
    text = '#vapesquad #fatclouds @mickRipsFat siiiick clouds bruv saw you at walmart chuckin em'
    actual = nlp.remove_RT_user(text)
    expected = '   siiiick clouds bruv saw you at walmart chuckin em'
    assert actual == expected

def test_remove_punctunation():
    nlp = NLPModel()
    text = '!!!! This... is... great???'
    actual = nlp.remove_punctuation(text)
    expected = ' This is great'
    assert actual == expected

def test_tokenize():
    nlp = NLPModel()
    text = 'Tokenize this'
    actual = nlp.tokenize(text)
    expected = ['Tokenize', 'this']
    assert actual == expected

