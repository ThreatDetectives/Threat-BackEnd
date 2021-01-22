from nlp_model.model import NLPModel
import pytest

def test_remove_RT_user():
    nlp = NLPModel()
    text = '#vapesquad #fatclouds @mickRipsFat siiiick clouds bruv saw you at walmart chuckin em'
    actual = nlp.remove_RT_user(text)
    expected = 'siiiick clouds bruv saw you at walmart chuckin em'
    assert actual == expected
