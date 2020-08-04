from pytest import mark


#pytest -m "not entertainment"
@mark.entertainment
def test_entertainment_system():
	assert True
