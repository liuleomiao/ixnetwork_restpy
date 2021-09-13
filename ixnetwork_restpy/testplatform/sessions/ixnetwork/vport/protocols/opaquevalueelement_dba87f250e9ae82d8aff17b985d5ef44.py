# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
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
from typing import List, Any, Union


class OpaqueValueElement(Base):
    """Configures the value for the opaque element.
    The OpaqueValueElement class encapsulates a list of opaqueValueElement resources that are managed by the user.
    A list of resources can be retrieved from the server using the OpaqueValueElement.find() method.
    The list can be managed by using the OpaqueValueElement.add() and OpaqueValueElement.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'opaqueValueElement'
    _SDM_ATT_MAP = {
        'Increment': 'increment',
        'Length': 'length',
        'Type': 'type',
        'Value': 'value',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(OpaqueValueElement, self).__init__(parent, list_op)

    @property
    def Increment(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the incremented value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Increment'])
    @Increment.setter
    def Increment(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Increment'], value)

    @property
    def Length(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the length.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Length'])
    @Length.setter
    def Length(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Length'], value)

    @property
    def Type(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It signifies the type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    @property
    def Value(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    def update(self, Increment=None, Length=None, Type=None, Value=None):
        # type: (str, int, int, str) -> OpaqueValueElement
        """Updates opaqueValueElement resource on the server.

        Args
        ----
        - Increment (str): It signifies the incremented value.
        - Length (number): It signifies the length.
        - Type (number): It signifies the type.
        - Value (str): It signifies the value.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Increment=None, Length=None, Type=None, Value=None):
        # type: (str, int, int, str) -> OpaqueValueElement
        """Adds a new opaqueValueElement resource on the server and adds it to the container.

        Args
        ----
        - Increment (str): It signifies the incremented value.
        - Length (number): It signifies the length.
        - Type (number): It signifies the type.
        - Value (str): It signifies the value.

        Returns
        -------
        - self: This instance with all currently retrieved opaqueValueElement resources using find and the newly added opaqueValueElement resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained opaqueValueElement resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Increment=None, Length=None, Type=None, Value=None):
        # type: (str, int, int, str) -> OpaqueValueElement
        """Finds and retrieves opaqueValueElement resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve opaqueValueElement resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all opaqueValueElement resources from the server.

        Args
        ----
        - Increment (str): It signifies the incremented value.
        - Length (number): It signifies the length.
        - Type (number): It signifies the type.
        - Value (str): It signifies the value.

        Returns
        -------
        - self: This instance with matching opaqueValueElement resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of opaqueValueElement data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the opaqueValueElement resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)