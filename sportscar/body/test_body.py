from pytest import mark


#The use of markers gives one the possibility to setup a self-maintaining test suite
#A suite can be built by simply marking desired testcases or calling markers


#pytest -m marker.name

@mark.body
class BodyTests:
	@mark.door
	def test_body_functions_as_expected(self):
		assert True
		
		mark.smoke
	def test_windshield(self):
		assert True

	def test_bumber(self):
		assert True
