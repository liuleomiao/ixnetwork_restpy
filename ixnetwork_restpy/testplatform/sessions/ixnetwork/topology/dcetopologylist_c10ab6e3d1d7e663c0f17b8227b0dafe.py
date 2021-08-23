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


class DceTopologyList(Base):
    """Fabric-Path Topology
    The DceTopologyList class encapsulates a required dceTopologyList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'dceTopologyList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableFTAG': 'enableFTAG',
        'InterestedVlanRangeCount': 'interestedVlanRangeCount',
        'Name': 'name',
        'NicknameCount': 'nicknameCount',
        'NoOfTreesToCompute': 'noOfTreesToCompute',
        'StartFTAGValue': 'startFTAGValue',
        'TopologyId': 'topologyId',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(DceTopologyList, self).__init__(parent, list_op)

    @property
    def InterestedVlanList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interestedvlanlist_728a61dfe3033f50a4c4b24dd65f6d27.InterestedVlanList): An instance of the InterestedVlanList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interestedvlanlist_728a61dfe3033f50a4c4b24dd65f6d27 import InterestedVlanList
        if self._properties.get('InterestedVlanList', None) is not None:
            return self._properties.get('InterestedVlanList')
        else:
            return InterestedVlanList(self)._select()

    @property
    def NicknameRecordList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nicknamerecordlist_035390df83e22e146cb32cc19244f93b.NicknameRecordList): An instance of the NicknameRecordList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nicknamerecordlist_035390df83e22e146cb32cc19244f93b import NicknameRecordList
        if self._properties.get('NicknameRecordList', None) is not None:
            return self._properties.get('NicknameRecordList')
        else:
            return NicknameRecordList(self)._select()

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EnableFTAG(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable FTAG
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFTAG']))

    @property
    def InterestedVlanRangeCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Interested VLAN Range Count(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterestedVlanRangeCount'])
    @InterestedVlanRangeCount.setter
    def InterestedVlanRangeCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['InterestedVlanRangeCount'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NicknameCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Nickname Count(multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['NicknameCount'])
    @NicknameCount.setter
    def NicknameCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NicknameCount'], value)

    @property
    def NoOfTreesToCompute(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No. of Trees to Compute
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NoOfTreesToCompute']))

    @property
    def StartFTAGValue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start FTAG Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartFTAGValue']))

    @property
    def TopologyId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Topology Id
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TopologyId']))

    def update(self, InterestedVlanRangeCount=None, Name=None, NicknameCount=None):
        # type: (int, str, int) -> DceTopologyList
        """Updates dceTopologyList resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - InterestedVlanRangeCount (number): Interested VLAN Range Count(multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NicknameCount (number): Nickname Count(multiplier)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, Active=None, EnableFTAG=None, NoOfTreesToCompute=None, StartFTAGValue=None, TopologyId=None):
        """Base class infrastructure that gets a list of dceTopologyList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - EnableFTAG (str): optional regex of enableFTAG
        - NoOfTreesToCompute (str): optional regex of noOfTreesToCompute
        - StartFTAGValue (str): optional regex of startFTAGValue
        - TopologyId (str): optional regex of topologyId

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
