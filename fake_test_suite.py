from nose.plugins.attrib import attr
from unittest import TestCase

class FakeTest(TestCase):

	@attr("passing")
	def passing_test(self):
		assert True;

	@attr("failing")
	def failling_test(self):
		assert False;