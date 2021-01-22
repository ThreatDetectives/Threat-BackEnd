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

def test_edge_case():
    nlp = NLPModel()
    text = '@11111'
    actual = nlp.remove_RT_user(text)
    expected = ''
    assert actual == expected

def test_edge_case_two():
    nlp = NLPModel()
    text = 'that chick said "the" fucks goin on'
    actual = nlp.remove_punctuation(text)
    expected = 'that chick said the fucks goin on'
    assert actual == expected

def test_all_removes():
    nlp = NLPModel()
    text = '#vapesquad "#fatclouds" @mickRipsFat siiiick clouds bruv saw you at walmart /?/?/?/ :) :( >xD chuckin em'
    actual = nlp.remove_RT_user(text)
    actual = nlp.remove_punctuation(text)
    actual = nlp.tokenize(text)
    expected = ['', 'vapesquad', 'fatclouds', 'mickRipsFat', 'siiiick', 'clouds', 'bruv', 'saw', 'you', 'at', 'walmart', 'xD', 'chuckin', 'em']
    assert actual == expected


def test_expected_failure():
    nlp = NLPModel()
    text = 5
    with pytest.raises(TypeError):
        nlp.remove_RT_user(text)

def test_expected_failure_two():
    nlp = NLPModel()
    text = 5
    with pytest.raises(TypeError):
        nlp.tokenize(text)

def test_expected_failure_three():
    nlp = NLPModel()
    text = 5
    with pytest.raises(TypeError):
        nlp.remove_punctuation(text)

