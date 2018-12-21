# MIT License
# 
# Copyright (c) 2018 Stichting SingularityNET
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Python Native Reputation Service API Integration Testing

import unittest

from test_reputation import TestReputationServiceBase

#TODO @nejc replace this!
from aigents_reputation_cli import *

# TODO @nejc - have this separate test_reputation_service_api.py file for this 
# Python Native Reputation Service implmentation 
class TestAigentsPythonReputationService(TestReputationServiceBase,unittest.TestCase):

	def setUp(self):
		#TODO @nejc replace this!
		self.rs = AigentsCLIReputationService('../../bin','./','test',False)

if __name__ == '__main__':
    unittest.main()