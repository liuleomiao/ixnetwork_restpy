# Copyright 1997 - 2018 by IXIA Keysight
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


class DceOutsideLinks(Base):
	"""The DceOutsideLinks class encapsulates a user managed dceOutsideLinks node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the DceOutsideLinks property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'dceOutsideLinks'

	def __init__(self, parent):
		super(DceOutsideLinks, self).__init__(parent)

	@property
	def ConnectionCol(self):
		"""Used with the Connection Row value to specify the particular network range router that is the endpoint of the Outside Link.

		Returns:
			number
		"""
		return self._get_attribute('connectionCol')
	@ConnectionCol.setter
	def ConnectionCol(self, value):
		self._set_attribute('connectionCol', value)

	@property
	def ConnectionRow(self):
		"""Used with the Connection Col value to specify the particular network range router that is the endpoint of the Outside Link.

		Returns:
			number
		"""
		return self._get_attribute('connectionRow')
	@ConnectionRow.setter
	def ConnectionRow(self, value):
		self._set_attribute('connectionRow', value)

	@property
	def LinkedRid(self):
		"""The Router ID of the emulated DCE ISIS router at the far end of the Outside Link.

		Returns:
			str
		"""
		return self._get_attribute('linkedRid')
	@LinkedRid.setter
	def LinkedRid(self, value):
		self._set_attribute('linkedRid', value)

	def update(self, ConnectionCol=None, ConnectionRow=None, LinkedRid=None):
		"""Updates a child instance of dceOutsideLinks on the server.

		Args:
			ConnectionCol (number): Used with the Connection Row value to specify the particular network range router that is the endpoint of the Outside Link.
			ConnectionRow (number): Used with the Connection Col value to specify the particular network range router that is the endpoint of the Outside Link.
			LinkedRid (str): The Router ID of the emulated DCE ISIS router at the far end of the Outside Link.

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._update(locals())

	def add(self, ConnectionCol=None, ConnectionRow=None, LinkedRid=None):
		"""Adds a new dceOutsideLinks node on the server and retrieves it in this instance.

		Args:
			ConnectionCol (number): Used with the Connection Row value to specify the particular network range router that is the endpoint of the Outside Link.
			ConnectionRow (number): Used with the Connection Col value to specify the particular network range router that is the endpoint of the Outside Link.
			LinkedRid (str): The Router ID of the emulated DCE ISIS router at the far end of the Outside Link.

		Returns:
			self: This instance with all currently retrieved dceOutsideLinks data using find and the newly added dceOutsideLinks data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the dceOutsideLinks data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, ConnectionCol=None, ConnectionRow=None, LinkedRid=None):
		"""Finds and retrieves dceOutsideLinks data from the server.

		All named parameters support regex and can be used to selectively retrieve dceOutsideLinks data from the server.
		By default the find method takes no parameters and will retrieve all dceOutsideLinks data from the server.

		Args:
			ConnectionCol (number): Used with the Connection Row value to specify the particular network range router that is the endpoint of the Outside Link.
			ConnectionRow (number): Used with the Connection Col value to specify the particular network range router that is the endpoint of the Outside Link.
			LinkedRid (str): The Router ID of the emulated DCE ISIS router at the far end of the Outside Link.

		Returns:
			self: This instance with matching dceOutsideLinks data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of dceOutsideLinks data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the dceOutsideLinks data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)