from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCoEGPNFT(Base):
    __slots__ = ()
    _SDM_NAME = "fCoEGPNFT"
    _SDM_ATT_MAP = {
        "FcoeHeaderVersion": "fCoEGPNFT.header.fcoeHeader.version-1",
        "FcoeHeaderReserved": "fCoEGPNFT.header.fcoeHeader.reserved-2",
        "FcoeHeaderESOF": "fCoEGPNFT.header.fcoeHeader.eSOF-3",
        "DeviceDataFramesDeviceDataInfo": "fCoEGPNFT.header.fcHeader.rCTL.deviceDataFrames.deviceDataInfo-4",
        "RCTLReserved": "fCoEGPNFT.header.fcHeader.rCTL.reserved-5",
        "ExtendedLinkServicesInfo": "fCoEGPNFT.header.fcHeader.rCTL.extendedLinkServices.info-6",
        "Fc4LinkDataInfo": "fCoEGPNFT.header.fcHeader.rCTL.fc4LinkData.info-7",
        "VideoDataInfo": "fCoEGPNFT.header.fcHeader.rCTL.videoData.info-8",
        "ExtendedHeaderInfo": "fCoEGPNFT.header.fcHeader.rCTL.extendedHeader.info-9",
        "BasicLinkServicesInfo": "fCoEGPNFT.header.fcHeader.rCTL.basicLinkServices.info-10",
        "LinkControlFramesInfo": "fCoEGPNFT.header.fcHeader.rCTL.linkControlFrames.info-11",
        "ExtendedRoutingInfo": "fCoEGPNFT.header.fcHeader.rCTL.extendedRouting.info-12",
        "FcHeaderDstId": "fCoEGPNFT.header.fcHeader.dstId-13",
        "FcHeaderCsCTLPriority": "fCoEGPNFT.header.fcHeader.csCTLPriority-14",
        "FcHeaderSrcId": "fCoEGPNFT.header.fcHeader.srcId-15",
        "FcHeaderType": "fCoEGPNFT.header.fcHeader.type-16",
        "FCTLCustom": "fCoEGPNFT.header.fcHeader.fCTL.custom-17",
        "BuildFCTLExchangeContext": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.exchangeContext-18",
        "BuildFCTLSequenceContext": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.sequenceContext-19",
        "BuildFCTLFirstSequence": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.firstSequence-20",
        "BuildFCTLLastSequence": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.lastSequence-21",
        "BuildFCTLEndSequence": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.endSequence-22",
        "BuildFCTLEndConnection": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.endConnection-23",
        "BuildFCTLCsCTLPriority": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.csCTLPriority-24",
        "BuildFCTLSequenceInitiative": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.sequenceInitiative-25",
        "BuildFCTLFcXIDReassigned": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.fcXIDReassigned-26",
        "BuildFCTLFcInvalidateXID": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.fcInvalidateXID-27",
        "BuildFCTLAckForm": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.ackForm-28",
        "BuildFCTLFcDataCompression": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.fcDataCompression-29",
        "BuildFCTLFcDataEncryption": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.fcDataEncryption-30",
        "BuildFCTLRetransmittedSequence": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.retransmittedSequence-31",
        "BuildFCTLUnidirectionalTransmit": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.unidirectionalTransmit-32",
        "BuildFCTLContinueSeqCondition": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.continueSeqCondition-33",
        "BuildFCTLAbortSeqCondition": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.abortSeqCondition-34",
        "BuildFCTLRelativeOffsetPresent": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.relativeOffsetPresent-35",
        "BuildFCTLExchangeReassembly": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.exchangeReassembly-36",
        "BuildFCTLFillBytes": "fCoEGPNFT.header.fcHeader.fCTL.buildFCTL.fillBytes-37",
        "FcHeaderSeqID": "fCoEGPNFT.header.fcHeader.seqID-38",
        "FcHeaderDfCTL": "fCoEGPNFT.header.fcHeader.dfCTL-39",
        "FcHeaderSeqCNT": "fCoEGPNFT.header.fcHeader.seqCNT-40",
        "FcHeaderOxID": "fCoEGPNFT.header.fcHeader.oxID-41",
        "FcHeaderRxID": "fCoEGPNFT.header.fcHeader.rxID-42",
        "FcHeaderParameter": "fCoEGPNFT.header.fcHeader.parameter-43",
        "FcCTRevision": "fCoEGPNFT.header.fcCT.revision-44",
        "FcCTInId": "fCoEGPNFT.header.fcCT.inId-45",
        "FcCTGsType": "fCoEGPNFT.header.fcCT.gsType-46",
        "FcCTGsSubtype": "fCoEGPNFT.header.fcCT.gsSubtype-47",
        "FcCTOptions": "fCoEGPNFT.header.fcCT.options-48",
        "FcCTReserved": "fCoEGPNFT.header.fcCT.reserved-49",
        "DNSOpcode": "fCoEGPNFT.header.dNS.opcode-50",
        "DNSMaxsize": "fCoEGPNFT.header.dNS.maxsize-51",
        "DNSReserved": "fCoEGPNFT.header.dNS.reserved-52",
        "DNSFlags": "fCoEGPNFT.header.dNS.flags-53",
        "DNSDomainIdScope": "fCoEGPNFT.header.dNS.domainIdScope-54",
        "DNSAreaIdScope": "fCoEGPNFT.header.dNS.areaIdScope-55",
        "DNSFc4TypeCode": "fCoEGPNFT.header.dNS.fc4TypeCode-56",
        "FcCRCAutoCRC": "fCoEGPNFT.header.fcCRC.autoCRC-57",
        "FcCRCGenerateBadCRC": "fCoEGPNFT.header.fcCRC.generateBadCRC-58",
        "FcTrailerEEOF": "fCoEGPNFT.header.fcTrailer.eEOF-59",
        "FcTrailerReserved": "fCoEGPNFT.header.fcTrailer.reserved-60",
    }

    def __init__(self, parent, list_op=False):
        super(FCoEGPNFT, self).__init__(parent, list_op)

    @property
    def FcoeHeaderVersion(self):
        """
        Display Name: Version
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcoeHeaderVersion"])
        )

    @property
    def FcoeHeaderReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcoeHeaderReserved"])
        )

    @property
    def FcoeHeaderESOF(self):
        """
        Display Name: E-SOF
        Default Value: 54
        Value Format: decimal
        Available enum values: SOFf - Fabric, 40, SOFi4 - Initiate Class 4, 41, SOFi2 - Initiate Class 2, 45, SOFi3 - Initiate Class 3, 46, SOFn4 - Normal Class 4, 49, SOFn2 - Normal Class 2, 53, SOFn3 - Normal Class 3, 54, SOFc4 - Connect Class 4, 57, SOFn1 - Normal Class 1 or 6, 250
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcoeHeaderESOF"])
        )

    @property
    def DeviceDataFramesDeviceDataInfo(self):
        """
        Display Name: Information
        Default Value: 0
        Value Format: decimal
        Available enum values: Uncategorized Information, 0, Solicited Data, 1, Unsolicited Control, 2, Solicited Control, 3, Unsolicited Data, 4, Data Descriptor, 5, Unsolicited Command, 6, Command Status, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DeviceDataFramesDeviceDataInfo"]),
        )

    @property
    def RCTLReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RCTLReserved"]))

    @property
    def ExtendedLinkServicesInfo(self):
        """
        Display Name: Information
        Default Value: 33
        Value Format: decimal
        Available enum values: Solicited Data, 32, Request, 33, Reply, 34
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedLinkServicesInfo"])
        )

    @property
    def Fc4LinkDataInfo(self):
        """
        Display Name: Information
        Default Value: 48
        Value Format: decimal
        Available enum values: Uncategorized Information, 48, Solicited Data, 49, Unsolicited Control, 50, Solicited Control, 51, Unsolicited Data, 52, Data Descriptor, 53, Unsolicited Command, 54, Command Status, 55
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Fc4LinkDataInfo"])
        )

    @property
    def VideoDataInfo(self):
        """
        Display Name: Information
        Default Value: 68
        Value Format: decimal
        Available enum values: Unsolicited Data, 68
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VideoDataInfo"]))

    @property
    def ExtendedHeaderInfo(self):
        """
        Display Name: Information
        Default Value: 80
        Value Format: decimal
        Available enum values: Virtual Fabric Tagging Header, 80, Inter Fabric Routing Header, 81, Encapsulation Header, 82
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedHeaderInfo"])
        )

    @property
    def BasicLinkServicesInfo(self):
        """
        Display Name: Information
        Default Value: 128
        Value Format: decimal
        Available enum values: No Operation, 128, Abort Sequence, 129, Remove Connection, 130, Basic Accept, 132, Basic Reject, 133, Dedicated Connection Preempted, 134
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BasicLinkServicesInfo"])
        )

    @property
    def LinkControlFramesInfo(self):
        """
        Display Name: Information
        Default Value: 192
        Value Format: decimal
        Available enum values: Acknowledge_1, 128, Acknowledge_0, 129, Nx Port Reject, 130, Fabric Reject, 131, Nx Port Busy, 132, Fabric Busy to Data Frame, 133, Fabric Busy to Link Control Frame, 134, Link Credit Reset, 135, Notify, 136, End, 137
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["LinkControlFramesInfo"])
        )

    @property
    def ExtendedRoutingInfo(self):
        """
        Display Name: Information
        Default Value: 240
        Value Format: decimal
        Available enum values: Vendor Unique, 240
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ExtendedRoutingInfo"])
        )

    @property
    def FcHeaderDstId(self):
        """
        Display Name: Destination ID
        Default Value: 0
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderDstId"]))

    @property
    def FcHeaderCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderCsCTLPriority"])
        )

    @property
    def FcHeaderSrcId(self):
        """
        Display Name: Source ID
        Default Value: 0
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderSrcId"]))

    @property
    def FcHeaderType(self):
        """
        Display Name: Type
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderType"]))

    @property
    def FCTLCustom(self):
        """
        Display Name: Custom
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCTLCustom"]))

    @property
    def BuildFCTLExchangeContext(self):
        """
        Display Name: Exchange Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Originator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLExchangeContext"])
        )

    @property
    def BuildFCTLSequenceContext(self):
        """
        Display Name: Sequence Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Initiator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLSequenceContext"])
        )

    @property
    def BuildFCTLFirstSequence(self):
        """
        Display Name: First Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, First, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLFirstSequence"])
        )

    @property
    def BuildFCTLLastSequence(self):
        """
        Display Name: Last Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLLastSequence"])
        )

    @property
    def BuildFCTLEndSequence(self):
        """
        Display Name: End Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLEndSequence"])
        )

    @property
    def BuildFCTLEndConnection(self):
        """
        Display Name: End Connection
        Default Value: 0
        Value Format: decimal
        Available enum values: Alive, 0, Pending, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLEndConnection"])
        )

    @property
    def BuildFCTLCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0
        Value Format: decimal
        Available enum values: CS_CTL, 0, Priority, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLCsCTLPriority"])
        )

    @property
    def BuildFCTLSequenceInitiative(self):
        """
        Display Name: Sequence Initiative
        Default Value: 0
        Value Format: decimal
        Available enum values: Hold, 0, Transfer, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLSequenceInitiative"])
        )

    @property
    def BuildFCTLFcXIDReassigned(self):
        """
        Display Name: FC XID Reassigned
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLFcXIDReassigned"])
        )

    @property
    def BuildFCTLFcInvalidateXID(self):
        """
        Display Name: FC Invalidate XID
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLFcInvalidateXID"])
        )

    @property
    def BuildFCTLAckForm(self):
        """
        Display Name: ACK_Form
        Default Value: 0
        Value Format: decimal
        Available enum values: No assistance provided, 0, ACK_1 Required, 1, reserved, 2, Ack_0 Required, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLAckForm"])
        )

    @property
    def BuildFCTLFcDataCompression(self):
        """
        Display Name: FC Data Compression
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLFcDataCompression"])
        )

    @property
    def BuildFCTLFcDataEncryption(self):
        """
        Display Name: FC Data Encryption
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLFcDataEncryption"])
        )

    @property
    def BuildFCTLRetransmittedSequence(self):
        """
        Display Name: Retransmitted Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Original, 0, Retransmission, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BuildFCTLRetransmittedSequence"]),
        )

    @property
    def BuildFCTLUnidirectionalTransmit(self):
        """
        Display Name: Unidirectional Transmit
        Default Value: 0
        Value Format: decimal
        Available enum values: Bi-directional, 0, Unidirectional, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BuildFCTLUnidirectionalTransmit"]),
        )

    @property
    def BuildFCTLContinueSeqCondition(self):
        """
        Display Name: Continue Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: No information, 0, Sequence to follow-immediately, 1, Squence to follow-soon, 2, Sequence to follow-delayed, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BuildFCTLContinueSeqCondition"]),
        )

    @property
    def BuildFCTLAbortSeqCondition(self):
        """
        Display Name: Abort Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: 0x00, 0, 0x01, 1, 0x10, 2, 0x11, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLAbortSeqCondition"])
        )

    @property
    def BuildFCTLRelativeOffsetPresent(self):
        """
        Display Name: Relative Offset Present
        Default Value: 0
        Value Format: decimal
        Available enum values: Parameter field defined, 0, Relative offset, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BuildFCTLRelativeOffsetPresent"]),
        )

    @property
    def BuildFCTLExchangeReassembly(self):
        """
        Display Name: Exchange Reassembly
        Default Value: 0
        Value Format: decimal
        Available enum values: off, 0, on, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLExchangeReassembly"])
        )

    @property
    def BuildFCTLFillBytes(self):
        """
        Display Name: Fill Bytes
        Default Value: 0
        Value Format: decimal
        Available enum values: 0 bytes of fill, 0, 1 bytes of fill, 1, 2 bytes of fill, 2, 3 bytes of fill, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BuildFCTLFillBytes"])
        )

    @property
    def FcHeaderSeqID(self):
        """
        Display Name: SEQ_ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderSeqID"]))

    @property
    def FcHeaderDfCTL(self):
        """
        Display Name: DF_CTL
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderDfCTL"]))

    @property
    def FcHeaderSeqCNT(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderSeqCNT"])
        )

    @property
    def FcHeaderOxID(self):
        """
        Display Name: OX_ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderOxID"]))

    @property
    def FcHeaderRxID(self):
        """
        Display Name: RX_ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderRxID"]))

    @property
    def FcHeaderParameter(self):
        """
        Display Name: Parameter
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcHeaderParameter"])
        )

    @property
    def FcCTRevision(self):
        """
        Display Name: Revision
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCTRevision"]))

    @property
    def FcCTInId(self):
        """
        Display Name: IN_ID
        Default Value: 0x000000
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCTInId"]))

    @property
    def FcCTGsType(self):
        """
        Display Name: GS_Type
        Default Value: 252
        Value Format: decimal
        Available enum values: Event Service, 244, Key Distribution Service, 247, Alias Service, 248, Management Service, 250, Time Service, 251, Directory Service, 252
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCTGsType"]))

    @property
    def FcCTGsSubtype(self):
        """
        Display Name: GS_Subtype
        Default Value: 0x02
        Value Format: hex
        Available enum values: X.500 Server (Obsolete), 1, Name Server, 2, IP Address Server (Obsolete), 3, FC-4 specific Servers, 128
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCTGsSubtype"]))

    @property
    def FcCTOptions(self):
        """
        Display Name: Options
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCTOptions"]))

    @property
    def FcCTReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCTReserved"]))

    @property
    def DNSOpcode(self):
        """
        Display Name: Command/Response Code
        Default Value: 370
        Value Format: decimal
        Available enum values: GA_NXT, 256, GID_A, 257, GPN_ID, 274, GNN_ID, 275, GCS_ID, 276, GFT_ID, 279, GSPN_ID, 280, GPT_ID, 282, GIPP_ID, 283, GFPN_ID, 284, GHA_ID, 285, GFD_ID, 286, GFF_ID, 287, GID_PN, 289, GIPP_PN, 299, GID_NN, 305, GPN_NN, 306, GIP_NN, 309, GIPA_NN, 310, GSNN_NN, 313, GNN_IP, 339, GIPA_IP, 342, GID_FT, 369, GPN_FT, 370, GNN_FT, 371, GNN_FF, 384, GPN_FF, 385, GPN_SDFCP, 386, GID_PT, 417, GID_IPP, 433, GPN_IPP, 434, GID_FPN, 449, GPPN_ID, 465, GID_FF, 497, GID_DP, 498, RPN_ID, 530, RNN_ID, 531, RCS_ID, 532, RFT_ID, 535, RSPN_ID, 536, RPT_ID, 538, RIPP_ID, 539, RHA_ID, 541, RFD_ID, 542, RFF_ID, 543, RIP_NN, 565, RIPA_NN, 566, RSNN_NN, 569, DA_ID, 768, SSB, 32761, SSE, 32762
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DNSOpcode"]))

    @property
    def DNSMaxsize(self):
        """
        Display Name: Maximum/Residual Size
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DNSMaxsize"]))

    @property
    def DNSReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DNSReserved"]))

    @property
    def DNSFlags(self):
        """
        Display Name: Flags
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DNSFlags"]))

    @property
    def DNSDomainIdScope(self):
        """
        Display Name: Domain_ID Scope
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DNSDomainIdScope"])
        )

    @property
    def DNSAreaIdScope(self):
        """
        Display Name: Area_ID Scope
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DNSAreaIdScope"])
        )

    @property
    def DNSFc4TypeCode(self):
        """
        Display Name: FC-4 TYPE Code
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DNSFc4TypeCode"])
        )

    @property
    def FcCRCAutoCRC(self):
        """
        Display Name: Auto
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcCRCAutoCRC"]))

    @property
    def FcCRCGenerateBadCRC(self):
        """
        Display Name: Bad CRC
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcCRCGenerateBadCRC"])
        )

    @property
    def FcTrailerEEOF(self):
        """
        Display Name: E-EOF
        Default Value: 65
        Value Format: decimal
        Available enum values: EOFn - Normal, 65, EOFt - Terminate, 66, EOFrt - Remove Terminate, 68, EOFni - Normal Invalid, 73, EOFrti - Remove Terminate Invalid, 79, EOFa - Abort, 80
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FcTrailerEEOF"]))

    @property
    def FcTrailerReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FcTrailerReserved"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
