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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
from typing import List, Any, Union


class PccGroup(Base):
    """Pce Group (Device) level Configuration
    The PccGroup class encapsulates a list of pccGroup resources that are managed by the user.
    A list of resources can be retrieved from the server using the PccGroup.find() method.
    The list can be managed by using the PccGroup.add() and PccGroup.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'pccGroup'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Authentication': 'authentication',
        'BurstInterval': 'burstInterval',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DeadInterval': 'deadInterval',
        'DescriptiveName': 'descriptiveName',
        'Errors': 'errors',
        'KeepaliveInterval': 'keepaliveInterval',
        'LspInstantiationCapability': 'lspInstantiationCapability',
        'LspUpdateCapability': 'lspUpdateCapability',
        'MD5Key': 'mD5Key',
        'MaxInitiatedLspPerInterval': 'maxInitiatedLspPerInterval',
        'MaxLspPerPcUpdate': 'maxLspPerPcUpdate',
        'MaxLspsPerPcInitiate': 'maxLspsPerPcInitiate',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'PcReplyLspsPerPcc': 'pcReplyLspsPerPcc',
        'PccIpv4Address': 'pccIpv4Address',
        'PceInitiatedLspsPerPcc': 'pceInitiatedLspsPerPcc',
        'PcePpagTLVType': 'pcePpagTLVType',
        'PceTEPathBindingTLVType': 'pceTEPathBindingTLVType',
        'RateControl': 'rateControl',
        'SessionStatus': 'sessionStatus',
        'SrPceCapability': 'srPceCapability',
        'Srv6PceCapability': 'srv6PceCapability',
        'StackedLayers': 'stackedLayers',
        'StateCounts': 'stateCounts',
        'StatefulPceCapability': 'statefulPceCapability',
        'Status': 'status',
    }
    _SDM_ENUM_MAP = {
        'status': ['configured', 'error', 'mixed', 'notStarted', 'started', 'starting', 'stopping'],
    }

    def __init__(self, parent, list_op=False):
        super(PccGroup, self).__init__(parent, list_op)

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import LearnedInfo
        if self._properties.get('LearnedInfo', None) is not None:
            return self._properties.get('LearnedInfo')
        else:
            return LearnedInfo(self)

    @property
    def LearnedInfoUpdate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfoupdate_b6503122c0a4a58877467964920e27b5.LearnedInfoUpdate): An instance of the LearnedInfoUpdate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfoupdate_b6503122c0a4a58877467964920e27b5 import LearnedInfoUpdate
        if self._properties.get('LearnedInfoUpdate', None) is not None:
            return self._properties.get('LearnedInfoUpdate')
        else:
            return LearnedInfoUpdate(self)

    @property
    def PcReplyLspParameters(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.pcreplylspparameters_73031069954bcd625c2f1df5c90abae7.PcReplyLspParameters): An instance of the PcReplyLspParameters class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.pcreplylspparameters_73031069954bcd625c2f1df5c90abae7 import PcReplyLspParameters
        if self._properties.get('PcReplyLspParameters', None) is not None:
            return self._properties.get('PcReplyLspParameters')
        else:
            return PcReplyLspParameters(self)._select()

    @property
    def PcRequestMatchCriteria(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.pcrequestmatchcriteria_365554ce0f609244eb458907a0c918f3.PcRequestMatchCriteria): An instance of the PcRequestMatchCriteria class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.pcrequestmatchcriteria_365554ce0f609244eb458907a0c918f3 import PcRequestMatchCriteria
        if self._properties.get('PcRequestMatchCriteria', None) is not None:
            return self._properties.get('PcRequestMatchCriteria')
        else:
            return PcRequestMatchCriteria(self)._select()

    @property
    def PceInitiateLSPParameters(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.pceinitiatelspparameters_c8b10382dd410ad40974ae280a39117b.PceInitiateLSPParameters): An instance of the PceInitiateLSPParameters class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.pceinitiatelspparameters_c8b10382dd410ad40974ae280a39117b import PceInitiateLSPParameters
        if self._properties.get('PceInitiateLSPParameters', None) is not None:
            return self._properties.get('PceInitiateLSPParameters')
        else:
            return PceInitiateLSPParameters(self)._select()

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def Authentication(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The type of cryptographic authentication to be used on this link interface
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Authentication']))

    @property
    def BurstInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interval in milisecond in which desired rate of messages needs to be maintained.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BurstInterval']))

    @property
    def ConnectedVia(self):
        # type: () -> List[str]
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

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
    def DeadInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This is the time interval, after the expiration of which, a PCEP peer declares the session down if no PCEP message has been received.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DeadInterval']))

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
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def KeepaliveInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Frequency/Time Interval of sending PCEP messages to keep the session active.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['KeepaliveInterval']))

    @property
    def LspInstantiationCapability(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If Stateful PCE Capability is enabled then this control should be activated to set the LSP Instantiation capability in the Stateful PCE Capability TLV.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LspInstantiationCapability']))

    @property
    def LspUpdateCapability(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If the Stateful PCE Capability is enabled then this control should be activated to set the update capability in the Stateful PCE Capability TLV.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LspUpdateCapability']))

    @property
    def MD5Key(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): A value to be used as the secret MD5 Key.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MD5Key']))

    @property
    def MaxInitiatedLspPerInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Maximum number of messages can be sent per interval.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxInitiatedLspPerInterval']))

    @property
    def MaxLspPerPcUpdate(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Controls the maximum number of LSPs that can be present in a PcUpdate message.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxLspPerPcUpdate']))

    @property
    def MaxLspsPerPcInitiate(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Controls the maximum number of LSPs that can be present in a PCInitiate message.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxLspsPerPcInitiate']))

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

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
    def PcReplyLspsPerPcc(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Controls the maximum number of PCE LSPs that can be send as PATH Response.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PcReplyLspsPerPcc'])
    @PcReplyLspsPerPcc.setter
    def PcReplyLspsPerPcc(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PcReplyLspsPerPcc'], value)

    @property
    def PccIpv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): IPv4 address of the PCC. This column is greyed out in case of PCEv6.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PccIpv4Address']))

    @property
    def PceInitiatedLspsPerPcc(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Controls the maximum number of PCE LSPs that can be Initiated per PCC.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PceInitiatedLspsPerPcc'])
    @PceInitiatedLspsPerPcc.setter
    def PceInitiatedLspsPerPcc(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PceInitiatedLspsPerPcc'], value)

    @property
    def PcePpagTLVType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): PPAG TLV Type specifies PCE's capability of interpreting this type of PPAG TLV
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PcePpagTLVType']))

    @property
    def PceTEPathBindingTLVType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): PCE TE-PATH-BINDING TLV Type is a TLV that carries MPLS label binding or SRv6 Binding SID. This is only configurable if the Binding SID Draft Version is set to ietf-pce-binding-label-sid. The minimum value is 0. The maximum value is 65535. The default value is 31.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PceTEPathBindingTLVType']))

    @property
    def RateControl(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The rate control is an optional feature associated with PCE initiated LSP.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RateControl']))

    @property
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def SrPceCapability(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The SR PCE Capability TLV is an optional TLV associated with the OPEN Object to exchange SR capability of PCEP speakers.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrPceCapability']))

    @property
    def Srv6PceCapability(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The SRv6 PCE Capability TLV is a sub-TLV that comes under PATH-SETUP-TYPE-CAPABILITY TLV if PST List contains SRv6 PST type. This TLV is associated with the OPEN Object to exchange SRv6 capability of PCEP speakers.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Srv6PceCapability']))

    @property
    def StackedLayers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['StackedLayers'], value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP['StateCounts'])

    @property
    def StatefulPceCapability(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If enabled, the server will work like a Stateful PCE else like a stateless PCE.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StatefulPceCapability']))

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, PcReplyLspsPerPcc=None, PceInitiatedLspsPerPcc=None, StackedLayers=None):
        # type: (List[str], int, str, int, int, List[str]) -> PccGroup
        """Updates pccGroup resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PcReplyLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be send as PATH Response.
        - PceInitiatedLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be Initiated per PCC.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, PcReplyLspsPerPcc=None, PceInitiatedLspsPerPcc=None, StackedLayers=None):
        # type: (List[str], int, str, int, int, List[str]) -> PccGroup
        """Adds a new pccGroup resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PcReplyLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be send as PATH Response.
        - PceInitiatedLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be Initiated per PCC.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved pccGroup resources using find and the newly added pccGroup resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained pccGroup resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, PcReplyLspsPerPcc=None, PceInitiatedLspsPerPcc=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves pccGroup resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pccGroup resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pccGroup resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - PcReplyLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be send as PATH Response.
        - PceInitiatedLspsPerPcc (number): Controls the maximum number of PCE LSPs that can be Initiated per PCC.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching pccGroup resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pccGroup data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pccGroup resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def ClearPceAllLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the clearPceAllLearnedInfo operation on the server.

        Clears ALL Learned LSP Information By PCC Device.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearPceAllLearnedInfo(async_operation=bool)
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearPceAllLearnedInfo(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearPceAllLearnedInfo(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearPceAllLearnedInfo(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearPceAllLearnedInfo', payload=payload, response_object=None)

    def GetPceBasicAllRsvpLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceBasicAllRsvpLspLearnedInfo operation on the server.

        Gets Basic Information about All RSVP LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceBasicAllRsvpLspLearnedInfo(async_operation=bool)
        ------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicAllRsvpLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicAllRsvpLspLearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicAllRsvpLspLearnedInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceBasicAllRsvpLspLearnedInfo', payload=payload, response_object=None)

    def GetPceBasicAllSrLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceBasicAllSrLspLearnedInfo operation on the server.

        Gets Basic Information about All SR LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceBasicAllSrLspLearnedInfo(async_operation=bool)
        ----------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicAllSrLspLearnedInfo(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicAllSrLspLearnedInfo(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicAllSrLspLearnedInfo(Arg2=list, async_operation=bool)list
        -------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceBasicAllSrLspLearnedInfo', payload=payload, response_object=None)

    def GetPceBasicAllSrv6LspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceBasicAllSrv6LspLearnedInfo operation on the server.

        Gets Basic Information about All SRv6 LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceBasicAllSrv6LspLearnedInfo(async_operation=bool)
        ------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicAllSrv6LspLearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicAllSrv6LspLearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicAllSrv6LspLearnedInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceBasicAllSrv6LspLearnedInfo', payload=payload, response_object=None)

    def GetPceBasicRsvpPccRequestedLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceBasicRsvpPccRequestedLspLearnedInfo operation on the server.

        Gets Basic Information about RSVP-TE PCC Requested LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceBasicRsvpPccRequestedLspLearnedInfo(async_operation=bool)
        ---------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicRsvpPccRequestedLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicRsvpPccRequestedLspLearnedInfo(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicRsvpPccRequestedLspLearnedInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceBasicRsvpPccRequestedLspLearnedInfo', payload=payload, response_object=None)

    def GetPceBasicRsvpPccSyncLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceBasicRsvpPccSyncLspLearnedInfo operation on the server.

        Gets Basic Information about RSVP-TE PCC Sync/Report LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceBasicRsvpPccSyncLspLearnedInfo(async_operation=bool)
        ----------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicRsvpPccSyncLspLearnedInfo(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicRsvpPccSyncLspLearnedInfo(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicRsvpPccSyncLspLearnedInfo(Arg2=list, async_operation=bool)list
        -------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceBasicRsvpPccSyncLspLearnedInfo', payload=payload, response_object=None)

    def GetPceBasicRsvpPceInitiatedLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceBasicRsvpPceInitiatedLspLearnedInfo operation on the server.

        Gets Basic Information about RSVP-TE PCE Initiated LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceBasicRsvpPceInitiatedLspLearnedInfo(async_operation=bool)
        ---------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicRsvpPceInitiatedLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicRsvpPceInitiatedLspLearnedInfo(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicRsvpPceInitiatedLspLearnedInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceBasicRsvpPceInitiatedLspLearnedInfo', payload=payload, response_object=None)

    def GetPceBasicSrPccRequestedLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceBasicSrPccRequestedLspLearnedInfo operation on the server.

        Gets Basic Information about SR-TE PCC Requested LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceBasicSrPccRequestedLspLearnedInfo(async_operation=bool)
        -------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrPccRequestedLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrPccRequestedLspLearnedInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrPccRequestedLspLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceBasicSrPccRequestedLspLearnedInfo', payload=payload, response_object=None)

    def GetPceBasicSrPccSyncLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceBasicSrPccSyncLspLearnedInfo operation on the server.

        Gets Basic Information about SR-TE PCC Sync/Report LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceBasicSrPccSyncLspLearnedInfo(async_operation=bool)
        --------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrPccSyncLspLearnedInfo(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrPccSyncLspLearnedInfo(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrPccSyncLspLearnedInfo(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceBasicSrPccSyncLspLearnedInfo', payload=payload, response_object=None)

    def GetPceBasicSrPceInitiatedLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceBasicSrPceInitiatedLspLearnedInfo operation on the server.

        Gets Basic Information about SR-TE PCE Initiated LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceBasicSrPceInitiatedLspLearnedInfo(async_operation=bool)
        -------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrPceInitiatedLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrPceInitiatedLspLearnedInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrPceInitiatedLspLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceBasicSrPceInitiatedLspLearnedInfo', payload=payload, response_object=None)

    def GetPceBasicSrv6PccRequestedLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceBasicSrv6PccRequestedLspLearnedInfo operation on the server.

        Gets Basic Information about SRv6 PCC Requested LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceBasicSrv6PccRequestedLspLearnedInfo(async_operation=bool)
        ---------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrv6PccRequestedLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrv6PccRequestedLspLearnedInfo(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrv6PccRequestedLspLearnedInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceBasicSrv6PccRequestedLspLearnedInfo', payload=payload, response_object=None)

    def GetPceBasicSrv6PccSyncLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceBasicSrv6PccSyncLspLearnedInfo operation on the server.

        Gets Basic Information about SRv6 PCC Sync/Report LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceBasicSrv6PccSyncLspLearnedInfo(async_operation=bool)
        ----------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrv6PccSyncLspLearnedInfo(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrv6PccSyncLspLearnedInfo(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrv6PccSyncLspLearnedInfo(Arg2=list, async_operation=bool)list
        -------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceBasicSrv6PccSyncLspLearnedInfo', payload=payload, response_object=None)

    def GetPceBasicSrv6PceInitiatedLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceBasicSrv6PceInitiatedLspLearnedInfo operation on the server.

        Gets Basic Information about SRv6 PCE Initiated LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceBasicSrv6PceInitiatedLspLearnedInfo(async_operation=bool)
        ---------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrv6PceInitiatedLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrv6PceInitiatedLspLearnedInfo(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceBasicSrv6PceInitiatedLspLearnedInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceBasicSrv6PceInitiatedLspLearnedInfo', payload=payload, response_object=None)

    def GetPceDetailedAllRsvpLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceDetailedAllRsvpLspLearnedInfo operation on the server.

        Gets Detailed Information about All RSVP LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceDetailedAllRsvpLspLearnedInfo(async_operation=bool)
        ---------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedAllRsvpLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedAllRsvpLspLearnedInfo(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedAllRsvpLspLearnedInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceDetailedAllRsvpLspLearnedInfo', payload=payload, response_object=None)

    def GetPceDetailedAllSrLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceDetailedAllSrLspLearnedInfo operation on the server.

        Gets Detailed Information about All SR LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceDetailedAllSrLspLearnedInfo(async_operation=bool)
        -------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedAllSrLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedAllSrLspLearnedInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedAllSrLspLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceDetailedAllSrLspLearnedInfo', payload=payload, response_object=None)

    def GetPceDetailedAllSrv6LspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceDetailedAllSrv6LspLearnedInfo operation on the server.

        Gets Detailed Information about All SRv6 LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceDetailedAllSrv6LspLearnedInfo(async_operation=bool)
        ---------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedAllSrv6LspLearnedInfo(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedAllSrv6LspLearnedInfo(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedAllSrv6LspLearnedInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceDetailedAllSrv6LspLearnedInfo', payload=payload, response_object=None)

    def GetPceDetailedRsvpPccRequestedLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceDetailedRsvpPccRequestedLspLearnedInfo operation on the server.

        Gets Detailed Information about RSVP-TE PCC Requested LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceDetailedRsvpPccRequestedLspLearnedInfo(async_operation=bool)
        ------------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedRsvpPccRequestedLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedRsvpPccRequestedLspLearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedRsvpPccRequestedLspLearnedInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceDetailedRsvpPccRequestedLspLearnedInfo', payload=payload, response_object=None)

    def GetPceDetailedRsvpPccSyncLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceDetailedRsvpPccSyncLspLearnedInfo operation on the server.

        Gets Detailed Information about RSVP-TE PCC Sync/Report LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceDetailedRsvpPccSyncLspLearnedInfo(async_operation=bool)
        -------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedRsvpPccSyncLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedRsvpPccSyncLspLearnedInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedRsvpPccSyncLspLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceDetailedRsvpPccSyncLspLearnedInfo', payload=payload, response_object=None)

    def GetPceDetailedRsvpPceInitiatedLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceDetailedRsvpPceInitiatedLspLearnedInfo operation on the server.

        Gets Detailed Information about RSVP-TE PCE Initiated LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceDetailedRsvpPceInitiatedLspLearnedInfo(async_operation=bool)
        ------------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedRsvpPceInitiatedLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedRsvpPceInitiatedLspLearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedRsvpPceInitiatedLspLearnedInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceDetailedRsvpPceInitiatedLspLearnedInfo', payload=payload, response_object=None)

    def GetPceDetailedSrPccRequestedLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceDetailedSrPccRequestedLspLearnedInfo operation on the server.

        Gets Detailed Information about SR-TE PCC Requested LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceDetailedSrPccRequestedLspLearnedInfo(async_operation=bool)
        ----------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrPccRequestedLspLearnedInfo(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrPccRequestedLspLearnedInfo(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrPccRequestedLspLearnedInfo(Arg2=list, async_operation=bool)list
        -------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceDetailedSrPccRequestedLspLearnedInfo', payload=payload, response_object=None)

    def GetPceDetailedSrPccSyncLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceDetailedSrPccSyncLspLearnedInfo operation on the server.

        Gets Detailed Information about SR-TE PCC Sync/Report LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceDetailedSrPccSyncLspLearnedInfo(async_operation=bool)
        -----------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrPccSyncLspLearnedInfo(SessionIndices=list, async_operation=bool)
        --------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrPccSyncLspLearnedInfo(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrPccSyncLspLearnedInfo(Arg2=list, async_operation=bool)list
        --------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceDetailedSrPccSyncLspLearnedInfo', payload=payload, response_object=None)

    def GetPceDetailedSrPceInitiatedLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceDetailedSrPceInitiatedLspLearnedInfo operation on the server.

        Gets Detailed Information about SR-TE PCE Initiated LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceDetailedSrPceInitiatedLspLearnedInfo(async_operation=bool)
        ----------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrPceInitiatedLspLearnedInfo(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrPceInitiatedLspLearnedInfo(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrPceInitiatedLspLearnedInfo(Arg2=list, async_operation=bool)list
        -------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceDetailedSrPceInitiatedLspLearnedInfo', payload=payload, response_object=None)

    def GetPceDetailedSrv6PccRequestedLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceDetailedSrv6PccRequestedLspLearnedInfo operation on the server.

        Gets Detailed Information about SRv6 PCC Requested LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceDetailedSrv6PccRequestedLspLearnedInfo(async_operation=bool)
        ------------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrv6PccRequestedLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrv6PccRequestedLspLearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrv6PccRequestedLspLearnedInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceDetailedSrv6PccRequestedLspLearnedInfo', payload=payload, response_object=None)

    def GetPceDetailedSrv6PccSyncLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceDetailedSrv6PccSyncLspLearnedInfo operation on the server.

        Gets Detailed Information about SRv6 PCC Sync/Report LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceDetailedSrv6PccSyncLspLearnedInfo(async_operation=bool)
        -------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrv6PccSyncLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrv6PccSyncLspLearnedInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrv6PccSyncLspLearnedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceDetailedSrv6PccSyncLspLearnedInfo', payload=payload, response_object=None)

    def GetPceDetailedSrv6PceInitiatedLspLearnedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPceDetailedSrv6PceInitiatedLspLearnedInfo operation on the server.

        Gets Detailed Information about SRv6 PCE Initiated LSPs learnt by this PCE.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPceDetailedSrv6PceInitiatedLspLearnedInfo(async_operation=bool)
        ------------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrv6PceInitiatedLspLearnedInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrv6PceInitiatedLspLearnedInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPceDetailedSrv6PceInitiatedLspLearnedInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getPceDetailedSrv6PceInitiatedLspLearnedInfo', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=list, async_operation=bool)
        -----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=string, async_operation=bool)
        -------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None, Authentication=None, BurstInterval=None, DeadInterval=None, KeepaliveInterval=None, LspInstantiationCapability=None, LspUpdateCapability=None, MD5Key=None, MaxInitiatedLspPerInterval=None, MaxLspPerPcUpdate=None, MaxLspsPerPcInitiate=None, PccIpv4Address=None, PcePpagTLVType=None, PceTEPathBindingTLVType=None, RateControl=None, SrPceCapability=None, Srv6PceCapability=None, StatefulPceCapability=None):
        """Base class infrastructure that gets a list of pccGroup device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - Authentication (str): optional regex of authentication
        - BurstInterval (str): optional regex of burstInterval
        - DeadInterval (str): optional regex of deadInterval
        - KeepaliveInterval (str): optional regex of keepaliveInterval
        - LspInstantiationCapability (str): optional regex of lspInstantiationCapability
        - LspUpdateCapability (str): optional regex of lspUpdateCapability
        - MD5Key (str): optional regex of mD5Key
        - MaxInitiatedLspPerInterval (str): optional regex of maxInitiatedLspPerInterval
        - MaxLspPerPcUpdate (str): optional regex of maxLspPerPcUpdate
        - MaxLspsPerPcInitiate (str): optional regex of maxLspsPerPcInitiate
        - PccIpv4Address (str): optional regex of pccIpv4Address
        - PcePpagTLVType (str): optional regex of pcePpagTLVType
        - PceTEPathBindingTLVType (str): optional regex of pceTEPathBindingTLVType
        - RateControl (str): optional regex of rateControl
        - SrPceCapability (str): optional regex of srPceCapability
        - Srv6PceCapability (str): optional regex of srv6PceCapability
        - StatefulPceCapability (str): optional regex of statefulPceCapability

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
