# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ValueList(Base):
	"""This object specifies the value list properties.
	The ValueList class encapsulates a list of valueList resources that is managed by the system.
	A list of resources can be retrieved from the server using the ValueList.find() method.
	"""

	__slots__ = ()
	_SDM_NAME = 'valueList'

	def __init__(self, parent):
		super(ValueList, self).__init__(parent)

	@property
	def AvailableWidths(self):
		"""Species all the possible widths available for a UDF in particular Type.

		Returns:
			list(str)
		"""
		return self._get_attribute('availableWidths')

	@property
	def StartValueList(self):
		"""Specifies the starting value for a particular UDF.

		Returns:
			list(number)
		"""
		return self._get_attribute('startValueList')
	@StartValueList.setter
	def StartValueList(self, value):
		self._set_attribute('startValueList', value)

	@property
	def Width(self):
		"""Specifies the width of the UDF.

		Returns:
			str(16|24|32|8)
		"""
		return self._get_attribute('width')
	@Width.setter
	def Width(self, value):
		self._set_attribute('width', value)

	def update(self, StartValueList=None, Width=None):
		"""Updates a child instance of valueList on the server.

		Args:
			StartValueList (list(number)): Specifies the starting value for a particular UDF.
			Width (str(16|24|32|8)): Specifies the width of the UDF.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def find(self, AvailableWidths=None, StartValueList=None, Width=None):
		"""Finds and retrieves valueList data from the server.

		All named parameters support regex and can be used to selectively retrieve valueList data from the server.
		By default the find method takes no parameters and will retrieve all valueList data from the server.

		Args:
			AvailableWidths (list(str)): Species all the possible widths available for a UDF in particular Type.
			StartValueList (list(number)): Specifies the starting value for a particular UDF.
			Width (str(16|24|32|8)): Specifies the width of the UDF.

		Returns:
			self: This instance with matching valueList data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of valueList data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the valueList data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
