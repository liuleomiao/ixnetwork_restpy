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


class Igmp(Base):
    """This object sends and responds to IGMP messages.
    The Igmp class encapsulates a required igmp resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'igmp'
    _SDM_ATT_MAP = {
        'EnableUnicastMode': 'enableUnicastMode',
        'Enabled': 'enabled',
        'NumberOfGroups': 'numberOfGroups',
        'NumberOfQueries': 'numberOfQueries',
        'QueryTimePeriod': 'queryTimePeriod',
        'RunningState': 'runningState',
        'SendLeaveOnHostDisable': 'sendLeaveOnHostDisable',
        'SendLeaveOnStop': 'sendLeaveOnStop',
        'StatsEnabled': 'statsEnabled',
        'TimePeriod': 'timePeriod',
    }
    _SDM_ENUM_MAP = {
        'runningState': ['unknown', 'stopped', 'stopping', 'starting', 'started'],
    }

    def __init__(self, parent, list_op=False):
        super(Igmp, self).__init__(parent, list_op)

    @property
    def Host(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.host_0710de542a7934016dc82d18924d1082.Host): An instance of the Host class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.host_0710de542a7934016dc82d18924d1082 import Host
        if self._properties.get('Host', None) is not None:
            return self._properties.get('Host')
        else:
            return Host(self)

    @property
    def Querier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.querier_caaf4682cc5c2a511c8c68d13991790f.Querier): An instance of the Querier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.querier_caaf4682cc5c2a511c8c68d13991790f import Querier
        if self._properties.get('Querier', None) is not None:
            return self._properties.get('Querier')
        else:
            return Querier(self)

    @property
    def EnableUnicastMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableUnicastMode'])
    @EnableUnicastMode.setter
    def EnableUnicastMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableUnicastMode'], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables the use of this emulated EIGRP router in the emulated EIGRP network. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def NumberOfGroups(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Provides a means of throttling the amount of IGMP traffic generated by the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfGroups'])
    @NumberOfGroups.setter
    def NumberOfGroups(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumberOfGroups'], value)

    @property
    def NumberOfQueries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Provides a means of throttling the amount of IGMP queries generated by the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfQueries'])
    @NumberOfQueries.setter
    def NumberOfQueries(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumberOfQueries'], value)

    @property
    def QueryTimePeriod(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time, in milliseconds, between queries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QueryTimePeriod'])
    @QueryTimePeriod.setter
    def QueryTimePeriod(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['QueryTimePeriod'], value)

    @property
    def RunningState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of the IGMP server.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RunningState'])

    @property
    def SendLeaveOnHostDisable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Send Leave On Host Disable
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendLeaveOnHostDisable'])
    @SendLeaveOnHostDisable.setter
    def SendLeaveOnHostDisable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['SendLeaveOnHostDisable'], value)

    @property
    def SendLeaveOnStop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Send leaves on stop (v2 and v3 only).
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendLeaveOnStop'])
    @SendLeaveOnStop.setter
    def SendLeaveOnStop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['SendLeaveOnStop'], value)

    @property
    def StatsEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, this object enables the IGMP statistics.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StatsEnabled'])
    @StatsEnabled.setter
    def StatsEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['StatsEnabled'], value)

    @property
    def TimePeriod(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the length of each time period during which the specified number of IGMP groups will be advertised.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TimePeriod'])
    @TimePeriod.setter
    def TimePeriod(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['TimePeriod'], value)

    def update(self, EnableUnicastMode=None, Enabled=None, NumberOfGroups=None, NumberOfQueries=None, QueryTimePeriod=None, SendLeaveOnHostDisable=None, SendLeaveOnStop=None, StatsEnabled=None, TimePeriod=None):
        # type: (bool, bool, int, int, int, bool, bool, bool, int) -> Igmp
        """Updates igmp resource on the server.

        Args
        ----
        - EnableUnicastMode (bool): 
        - Enabled (bool): Enables or disables the use of this emulated EIGRP router in the emulated EIGRP network. (default = disabled)
        - NumberOfGroups (number): Provides a means of throttling the amount of IGMP traffic generated by the port.
        - NumberOfQueries (number): Provides a means of throttling the amount of IGMP queries generated by the port.
        - QueryTimePeriod (number): The time, in milliseconds, between queries.
        - SendLeaveOnHostDisable (bool): Send Leave On Host Disable
        - SendLeaveOnStop (bool): Send leaves on stop (v2 and v3 only).
        - StatsEnabled (bool): If true, this object enables the IGMP statistics.
        - TimePeriod (number): Specifies the length of each time period during which the specified number of IGMP groups will be advertised.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def Join(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the join operation on the server.

        NOT DEFINED

        join(Arg2=string, Arg3=number, async_operation=bool)
        ----------------------------------------------------
        - Arg2 (str): NOT DEFINED
        - Arg3 (number): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('join', payload=payload, response_object=None)

    def Leave(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the leave operation on the server.

        NOT DEFINED

        leave(Arg2=string, Arg3=number, async_operation=bool)
        -----------------------------------------------------
        - Arg2 (str): NOT DEFINED
        - Arg3 (number): NOT DEFINED
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('leave', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the EIGRP protocol on a port or group of ports simultaneously.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the IGMP protocol on a port or group of ports simultaneously.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)