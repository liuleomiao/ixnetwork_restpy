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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class TrafficProfileProxiesS5S8Sgw(Base):
    """GTP Traffic Profile from IxNetwork
    The TrafficProfileProxiesS5S8Sgw class encapsulates a list of trafficProfileProxiesS5S8Sgw resources that are managed by the user.
    A list of resources can be retrieved from the server using the TrafficProfileProxiesS5S8Sgw.find() method.
    The list can be managed by using the TrafficProfileProxiesS5S8Sgw.add() and TrafficProfileProxiesS5S8Sgw.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'trafficProfileProxiesS5S8Sgw'
    _SDM_ATT_MAP = {
        'ActualPluginSettingsRange': 'actualPluginSettingsRange',
        'Enabled': 'enabled',
        'Name': 'name',
        'ObjectId': 'objectId',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(TrafficProfileProxiesS5S8Sgw, self).__init__(parent, list_op)

    @property
    def ActualPluginSettingsRange(self):
        # type: () -> str
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalTrafficProfileS5S8): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActualPluginSettingsRange'])
    @ActualPluginSettingsRange.setter
    def ActualPluginSettingsRange(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ActualPluginSettingsRange'], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    def update(self, ActualPluginSettingsRange=None, Enabled=None, Name=None):
        # type: (str, bool, str) -> TrafficProfileProxiesS5S8Sgw
        """Updates trafficProfileProxiesS5S8Sgw resource on the server.

        Args
        ----
        - ActualPluginSettingsRange (str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalTrafficProfileS5S8)): 
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ActualPluginSettingsRange=None, Enabled=None, Name=None):
        # type: (str, bool, str) -> TrafficProfileProxiesS5S8Sgw
        """Adds a new trafficProfileProxiesS5S8Sgw resource on the server and adds it to the container.

        Args
        ----
        - ActualPluginSettingsRange (str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalTrafficProfileS5S8)): 
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): 

        Returns
        -------
        - self: This instance with all currently retrieved trafficProfileProxiesS5S8Sgw resources using find and the newly added trafficProfileProxiesS5S8Sgw resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained trafficProfileProxiesS5S8Sgw resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ActualPluginSettingsRange=None, Enabled=None, Name=None, ObjectId=None):
        # type: (str, bool, str, str) -> TrafficProfileProxiesS5S8Sgw
        """Finds and retrieves trafficProfileProxiesS5S8Sgw resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve trafficProfileProxiesS5S8Sgw resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all trafficProfileProxiesS5S8Sgw resources from the server.

        Args
        ----
        - ActualPluginSettingsRange (str(None | /api/v1/sessions/1/ixnetwork/globals/.../globalTrafficProfileS5S8)): 
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - Name (str): 
        - ObjectId (str): Unique identifier for this object

        Returns
        -------
        - self: This instance with matching trafficProfileProxiesS5S8Sgw resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of trafficProfileProxiesS5S8Sgw data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the trafficProfileProxiesS5S8Sgw resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
