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


class SwitchHostRangeLearnedInfo(Base):
    """NOT DEFINED
    The SwitchHostRangeLearnedInfo class encapsulates a list of switchHostRangeLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchHostRangeLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "switchHostRangeLearnedInfo"
    _SDM_ATT_MAP = {
        "DestinationHostIpv4Address": "destinationHostIpv4Address",
        "DestinationHostMac": "destinationHostMac",
        "PacketType": "packetType",
        "Path": "path",
        "SourceHostIpv4Address": "sourceHostIpv4Address",
        "SourceHostMac": "sourceHostMac",
        "Status": "status",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(SwitchHostRangeLearnedInfo, self).__init__(parent, list_op)

    @property
    def SwitchHostRangeHopsLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostrangehopslearnedinfo_644eba5a33f6c4a8b40b153ae361c253.SwitchHostRangeHopsLearnedInfo): An instance of the SwitchHostRangeHopsLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostrangehopslearnedinfo_644eba5a33f6c4a8b40b153ae361c253 import (
            SwitchHostRangeHopsLearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SwitchHostRangeHopsLearnedInfo", None) is not None:
                return self._properties.get("SwitchHostRangeHopsLearnedInfo")
        return SwitchHostRangeHopsLearnedInfo(self)

    @property
    def DestinationHostIpv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestinationHostIpv4Address"])

    @property
    def DestinationHostMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["DestinationHostMac"])

    @property
    def PacketType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["PacketType"])

    @property
    def Path(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Path"])

    @property
    def SourceHostIpv4Address(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceHostIpv4Address"])

    @property
    def SourceHostMac(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SourceHostMac"])

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Status"])

    def add(self):
        """Adds a new switchHostRangeLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved switchHostRangeLearnedInfo resources using find and the newly added switchHostRangeLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        DestinationHostIpv4Address=None,
        DestinationHostMac=None,
        PacketType=None,
        Path=None,
        SourceHostIpv4Address=None,
        SourceHostMac=None,
        Status=None,
    ):
        # type: (str, str, str, str, str, str, str) -> SwitchHostRangeLearnedInfo
        """Finds and retrieves switchHostRangeLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchHostRangeLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchHostRangeLearnedInfo resources from the server.

        Args
        ----
        - DestinationHostIpv4Address (str): NOT DEFINED
        - DestinationHostMac (str): NOT DEFINED
        - PacketType (str): NOT DEFINED
        - Path (str): NOT DEFINED
        - SourceHostIpv4Address (str): NOT DEFINED
        - SourceHostMac (str): NOT DEFINED
        - Status (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching switchHostRangeLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchHostRangeLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchHostRangeLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
