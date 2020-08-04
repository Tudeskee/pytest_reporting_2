from pytest import mark

@mark.fixtest
class fixtureTests():

	def test_method1(self, numbers):
		x = 15
		assert numbers[0] == x


	def test_method2(self, numbers):
		y = 20
		assert numbers[1] == y


	def test_method3(self, numbers):
		z = 25
		assert numbers[2] == z