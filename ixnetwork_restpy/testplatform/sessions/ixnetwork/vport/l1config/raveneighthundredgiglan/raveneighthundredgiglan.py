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


class RavenEightHundredGigLan(Base):
    """
    The RavenEightHundredGigLan class encapsulates a required ravenEightHundredGigLan resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ravenEightHundredGigLan"
    _SDM_ATT_MAP = {
        "AutoInstrumentation": "autoInstrumentation",
        "AvailableSpeeds": "availableSpeeds",
        "BadBlocksNumber": "badBlocksNumber",
        "CanModifySpeed": "canModifySpeed",
        "CanSetMultipleSpeeds": "canSetMultipleSpeeds",
        "EnablePPM": "enablePPM",
        "EnabledFlowControl": "enabledFlowControl",
        "FlowControlDirectedAddress": "flowControlDirectedAddress",
        "GoodBlocksNumber": "goodBlocksNumber",
        "LaserOn": "laserOn",
        "LoopContinuously": "loopContinuously",
        "LoopCountNumber": "loopCountNumber",
        "Loopback": "loopback",
        "LoopbackMode": "loopbackMode",
        "Ppm": "ppm",
        "SelectedSpeeds": "selectedSpeeds",
        "SendSetsMode": "sendSetsMode",
        "Speed": "speed",
        "StartErrorInsertion": "startErrorInsertion",
        "TxIgnoreRxLinkFaults": "txIgnoreRxLinkFaults",
        "TypeAOrderedSets": "typeAOrderedSets",
        "TypeBOrderedSets": "typeBOrderedSets",
    }
    _SDM_ENUM_MAP = {
        "autoInstrumentation": ["endOfFrame", "floating"],
        "loopbackMode": ["none", "internalLoopback"],
        "sendSetsMode": ["alternate", "typeAOnly", "typeBOnly"],
        "speed": ["speed100g", "speed200g", "speed400g", "speed800g"],
        "typeAOrderedSets": ["localFault", "remoteFault"],
        "typeBOrderedSets": ["localFault", "remoteFault"],
    }

    def __init__(self, parent, list_op=False):
        super(RavenEightHundredGigLan, self).__init__(parent, list_op)

    @property
    def Fcoe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.raveneighthundredgiglan.fcoe.fcoe.Fcoe): An instance of the Fcoe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.raveneighthundredgiglan.fcoe.fcoe import (
            Fcoe,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Fcoe", None) is not None:
                return self._properties.get("Fcoe")
        return Fcoe(self)._select()

    @property
    def AutoInstrumentation(self):
        # type: () -> str
        """
        Returns
        -------
        - str(endOfFrame | floating): The auto instrumentation mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoInstrumentation"])

    @AutoInstrumentation.setter
    def AutoInstrumentation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoInstrumentation"], value)

    @property
    def AvailableSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed100g | speed200g | speed400g | speed800g]): Which speeds are available for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableSpeeds"])

    @property
    def BadBlocksNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["BadBlocksNumber"])

    @BadBlocksNumber.setter
    def BadBlocksNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BadBlocksNumber"], value)

    @property
    def CanModifySpeed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Returns true/false depending upon if the port can change speed for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CanModifySpeed"])

    @property
    def CanSetMultipleSpeeds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Can this port selectmultiple speeds for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CanSetMultipleSpeeds"])

    @property
    def EnablePPM(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the portsppm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePPM"])

    @EnablePPM.setter
    def EnablePPM(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePPM"], value)

    @property
    def EnabledFlowControl(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the port's MAC flow control mechanisms to listen for a directed address pause message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnabledFlowControl"])

    @EnabledFlowControl.setter
    def EnabledFlowControl(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnabledFlowControl"], value)

    @property
    def FlowControlDirectedAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The 48-bit MAC address that the port listens on for a directed pause.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowControlDirectedAddress"])

    @FlowControlDirectedAddress.setter
    def FlowControlDirectedAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowControlDirectedAddress"], value)

    @property
    def GoodBlocksNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["GoodBlocksNumber"])

    @GoodBlocksNumber.setter
    def GoodBlocksNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GoodBlocksNumber"], value)

    @property
    def LaserOn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["LaserOn"])

    @LaserOn.setter
    def LaserOn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LaserOn"], value)

    @property
    def LoopContinuously(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoopContinuously"])

    @LoopContinuously.setter
    def LoopContinuously(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoopContinuously"], value)

    @property
    def LoopCountNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoopCountNumber"])

    @LoopCountNumber.setter
    def LoopCountNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoopCountNumber"], value)

    @property
    def Loopback(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the port is set to internally loopback from transmit to receive.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Loopback"])

    @Loopback.setter
    def Loopback(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Loopback"], value)

    @property
    def LoopbackMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(none | internalLoopback):
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoopbackMode"])

    @LoopbackMode.setter
    def LoopbackMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoopbackMode"], value)

    @property
    def Ppm(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the value that needs to be adjusted for the line transmit frequency.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ppm"])

    @Ppm.setter
    def Ppm(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ppm"], value)

    @property
    def SelectedSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed100g | speed200g | speed400g | speed800g]): Which speeds are selected for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SelectedSpeeds"])

    @SelectedSpeeds.setter
    def SelectedSpeeds(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["SelectedSpeeds"], value)

    @property
    def SendSetsMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(alternate | typeAOnly | typeBOnly):
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendSetsMode"])

    @SendSetsMode.setter
    def SendSetsMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendSetsMode"], value)

    @property
    def Speed(self):
        # type: () -> str
        """
        Returns
        -------
        - str(speed100g | speed200g | speed400g | speed800g):
        """
        return self._get_attribute(self._SDM_ATT_MAP["Speed"])

    @Speed.setter
    def Speed(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Speed"], value)

    @property
    def StartErrorInsertion(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartErrorInsertion"])

    @StartErrorInsertion.setter
    def StartErrorInsertion(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartErrorInsertion"], value)

    @property
    def TxIgnoreRxLinkFaults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, will allow transmission of packets even if the receive link is down.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxIgnoreRxLinkFaults"])

    @TxIgnoreRxLinkFaults.setter
    def TxIgnoreRxLinkFaults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxIgnoreRxLinkFaults"], value)

    @property
    def TypeAOrderedSets(self):
        # type: () -> str
        """
        Returns
        -------
        - str(localFault | remoteFault):
        """
        return self._get_attribute(self._SDM_ATT_MAP["TypeAOrderedSets"])

    @TypeAOrderedSets.setter
    def TypeAOrderedSets(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TypeAOrderedSets"], value)

    @property
    def TypeBOrderedSets(self):
        # type: () -> str
        """
        Returns
        -------
        - str(localFault | remoteFault):
        """
        return self._get_attribute(self._SDM_ATT_MAP["TypeBOrderedSets"])

    @TypeBOrderedSets.setter
    def TypeBOrderedSets(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TypeBOrderedSets"], value)

    def update(
        self,
        AutoInstrumentation=None,
        BadBlocksNumber=None,
        EnablePPM=None,
        EnabledFlowControl=None,
        FlowControlDirectedAddress=None,
        GoodBlocksNumber=None,
        LaserOn=None,
        LoopContinuously=None,
        LoopCountNumber=None,
        Loopback=None,
        LoopbackMode=None,
        Ppm=None,
        SelectedSpeeds=None,
        SendSetsMode=None,
        Speed=None,
        StartErrorInsertion=None,
        TxIgnoreRxLinkFaults=None,
        TypeAOrderedSets=None,
        TypeBOrderedSets=None,
    ):
        # type: (str, int, bool, bool, str, int, bool, bool, int, bool, str, int, List[str], str, str, bool, bool, str, str) -> RavenEightHundredGigLan
        """Updates ravenEightHundredGigLan resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - BadBlocksNumber (number):
        - EnablePPM (bool): If true, enables the portsppm.
        - EnabledFlowControl (bool): If true, enables the port's MAC flow control mechanisms to listen for a directed address pause message.
        - FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
        - GoodBlocksNumber (number):
        - LaserOn (bool):
        - LoopContinuously (bool):
        - LoopCountNumber (number):
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - LoopbackMode (str(none | internalLoopback)):
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - SelectedSpeeds (list(str[speed100g | speed200g | speed400g | speed800g])): Which speeds are selected for the current media and AN settings.
        - SendSetsMode (str(alternate | typeAOnly | typeBOnly)):
        - Speed (str(speed100g | speed200g | speed400g | speed800g)):
        - StartErrorInsertion (bool):
        - TxIgnoreRxLinkFaults (bool): If enabled, will allow transmission of packets even if the receive link is down.
        - TypeAOrderedSets (str(localFault | remoteFault)):
        - TypeBOrderedSets (str(localFault | remoteFault)):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AutoInstrumentation=None,
        AvailableSpeeds=None,
        BadBlocksNumber=None,
        CanModifySpeed=None,
        CanSetMultipleSpeeds=None,
        EnablePPM=None,
        EnabledFlowControl=None,
        FlowControlDirectedAddress=None,
        GoodBlocksNumber=None,
        LaserOn=None,
        LoopContinuously=None,
        LoopCountNumber=None,
        Loopback=None,
        LoopbackMode=None,
        Ppm=None,
        SelectedSpeeds=None,
        SendSetsMode=None,
        Speed=None,
        StartErrorInsertion=None,
        TxIgnoreRxLinkFaults=None,
        TypeAOrderedSets=None,
        TypeBOrderedSets=None,
    ):
        # type: (str, List[str], int, bool, bool, bool, bool, str, int, bool, bool, int, bool, str, int, List[str], str, str, bool, bool, str, str) -> RavenEightHundredGigLan
        """Finds and retrieves ravenEightHundredGigLan resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ravenEightHundredGigLan resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ravenEightHundredGigLan resources from the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - AvailableSpeeds (list(str[speed100g | speed200g | speed400g | speed800g])): Which speeds are available for the current media and AN settings.
        - BadBlocksNumber (number):
        - CanModifySpeed (bool): Returns true/false depending upon if the port can change speed for the current media and AN settings.
        - CanSetMultipleSpeeds (bool): Can this port selectmultiple speeds for the current media and AN settings.
        - EnablePPM (bool): If true, enables the portsppm.
        - EnabledFlowControl (bool): If true, enables the port's MAC flow control mechanisms to listen for a directed address pause message.
        - FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
        - GoodBlocksNumber (number):
        - LaserOn (bool):
        - LoopContinuously (bool):
        - LoopCountNumber (number):
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - LoopbackMode (str(none | internalLoopback)):
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - SelectedSpeeds (list(str[speed100g | speed200g | speed400g | speed800g])): Which speeds are selected for the current media and AN settings.
        - SendSetsMode (str(alternate | typeAOnly | typeBOnly)):
        - Speed (str(speed100g | speed200g | speed400g | speed800g)):
        - StartErrorInsertion (bool):
        - TxIgnoreRxLinkFaults (bool): If enabled, will allow transmission of packets even if the receive link is down.
        - TypeAOrderedSets (str(localFault | remoteFault)):
        - TypeBOrderedSets (str(localFault | remoteFault)):

        Returns
        -------
        - self: This instance with matching ravenEightHundredGigLan resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ravenEightHundredGigLan data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ravenEightHundredGigLan resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
