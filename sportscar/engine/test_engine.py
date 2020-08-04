from pytest import mark


#pytest -m "body and engine"
#pytest -m "body or engine"
@mark.smoke
@mark.engine
def test_engine_as_expected():
	assert True
