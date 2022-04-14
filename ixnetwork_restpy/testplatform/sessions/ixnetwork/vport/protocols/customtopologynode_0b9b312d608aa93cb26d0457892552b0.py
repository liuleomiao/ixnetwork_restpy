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


class CustomTopologyNode(Base):
    """NOT DEFINED
    The CustomTopologyNode class encapsulates a list of customTopologyNode resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTopologyNode.find() method.
    The list can be managed by using the CustomTopologyNode.add() and CustomTopologyNode.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "customTopologyNode"
    _SDM_ATT_MAP = {
        "BridgePriority": "bridgePriority",
        "EdgeBridge": "edgeBridge",
        "Enabled": "enabled",
        "Nickname": "nickname",
        "Priority": "priority",
        "SpSrcId": "spSrcId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(CustomTopologyNode, self).__init__(parent, list_op)

    @property
    def CustomNetworkTopologyLinks(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customnetworktopologylinks_5e1eaf53830b67b52c94f8ec618f4c02.CustomNetworkTopologyLinks): An instance of the CustomNetworkTopologyLinks class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customnetworktopologylinks_5e1eaf53830b67b52c94f8ec618f4c02 import (
            CustomNetworkTopologyLinks,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CustomNetworkTopologyLinks", None) is not None:
                return self._properties.get("CustomNetworkTopologyLinks")
        return CustomNetworkTopologyLinks(self)

    @property
    def BridgePriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["BridgePriority"])

    @BridgePriority.setter
    def BridgePriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BridgePriority"], value)

    @property
    def EdgeBridge(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["EdgeBridge"])

    @EdgeBridge.setter
    def EdgeBridge(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EdgeBridge"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def Nickname(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Nickname"])

    @Nickname.setter
    def Nickname(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Nickname"], value)

    @property
    def Priority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Priority"])

    @Priority.setter
    def Priority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Priority"], value)

    @property
    def SpSrcId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SpSrcId"])

    @SpSrcId.setter
    def SpSrcId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SpSrcId"], value)

    def update(
        self,
        BridgePriority=None,
        EdgeBridge=None,
        Enabled=None,
        Nickname=None,
        Priority=None,
        SpSrcId=None,
    ):
        # type: (int, bool, bool, int, int, int) -> CustomTopologyNode
        """Updates customTopologyNode resource on the server.

        Args
        ----
        - BridgePriority (number): NOT DEFINED
        - EdgeBridge (bool): NOT DEFINED
        - Enabled (bool): NOT DEFINED
        - Nickname (number): NOT DEFINED
        - Priority (number): NOT DEFINED
        - SpSrcId (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        BridgePriority=None,
        EdgeBridge=None,
        Enabled=None,
        Nickname=None,
        Priority=None,
        SpSrcId=None,
    ):
        # type: (int, bool, bool, int, int, int) -> CustomTopologyNode
        """Adds a new customTopologyNode resource on the server and adds it to the container.

        Args
        ----
        - BridgePriority (number): NOT DEFINED
        - EdgeBridge (bool): NOT DEFINED
        - Enabled (bool): NOT DEFINED
        - Nickname (number): NOT DEFINED
        - Priority (number): NOT DEFINED
        - SpSrcId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTopologyNode resources using find and the newly added customTopologyNode resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTopologyNode resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        BridgePriority=None,
        EdgeBridge=None,
        Enabled=None,
        Nickname=None,
        Priority=None,
        SpSrcId=None,
    ):
        # type: (int, bool, bool, int, int, int) -> CustomTopologyNode
        """Finds and retrieves customTopologyNode resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTopologyNode resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTopologyNode resources from the server.

        Args
        ----
        - BridgePriority (number): NOT DEFINED
        - EdgeBridge (bool): NOT DEFINED
        - Enabled (bool): NOT DEFINED
        - Nickname (number): NOT DEFINED
        - Priority (number): NOT DEFINED
        - SpSrcId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTopologyNode resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTopologyNode data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTopologyNode resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
