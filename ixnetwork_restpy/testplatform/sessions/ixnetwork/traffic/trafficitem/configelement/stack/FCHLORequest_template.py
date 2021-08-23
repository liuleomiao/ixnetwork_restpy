from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FCHLORequest(Base):
    __slots__ = ()
    _SDM_NAME = 'FCHLORequest'
    _SDM_ATT_MAP = {
        'FcHeaderRCTL': 'fcHLORequest.header.fcHeader.rCTL-1',
        'FcHeaderDstId': 'fcHLORequest.header.fcHeader.dstId-2',
        'FcHeaderCsCTLPriority': 'fcHLORequest.header.fcHeader.csCTLPriority-3',
        'FcHeaderSrcId': 'fcHLORequest.header.fcHeader.srcId-4',
        'FcHeaderType': 'fcHLORequest.header.fcHeader.type-5',
        'FcHeaderSof': 'fcHLORequest.header.fcHeader.sof-6',
        'FCTLCustom': 'fcHLORequest.header.fcHeader.fCTL.custom-7',
        'BuildFCTLExchangeContext': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.exchangeContext-8',
        'BuildFCTLSequenceContext': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.sequenceContext-9',
        'BuildFCTLFirstSequence': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.firstSequence-10',
        'BuildFCTLLastSequence': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.lastSequence-11',
        'BuildFCTLEndSequence': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.endSequence-12',
        'BuildFCTLEndConnection': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.endConnection-13',
        'BuildFCTLCsCTLPriority': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.csCTLPriority-14',
        'BuildFCTLSequenceInitiative': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.sequenceInitiative-15',
        'BuildFCTLFcXIDReassigned': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.fcXIDReassigned-16',
        'BuildFCTLFcInvalidateXID': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.fcInvalidateXID-17',
        'BuildFCTLAckForm': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.ackForm-18',
        'BuildFCTLFcDataCompression': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.fcDataCompression-19',
        'BuildFCTLFcDataEncryption': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.fcDataEncryption-20',
        'BuildFCTLRetransmittedSequence': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.retransmittedSequence-21',
        'BuildFCTLUnidirectionalTransmit': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.unidirectionalTransmit-22',
        'BuildFCTLContinueSeqCondition': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.continueSeqCondition-23',
        'BuildFCTLAbortSeqCondition': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.abortSeqCondition-24',
        'BuildFCTLRelativeOffsetPresent': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.relativeOffsetPresent-25',
        'BuildFCTLExchangeReassembly': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.exchangeReassembly-26',
        'BuildFCTLFillBytes': 'fcHLORequest.header.fcHeader.fCTL.buildFCTL.fillBytes-27',
        'FcHeaderSeqID': 'fcHLORequest.header.fcHeader.seqID-28',
        'FcHeaderDfCTL': 'fcHLORequest.header.fcHeader.dfCTL-29',
        'FcHeaderSeqCNT': 'fcHLORequest.header.fcHeader.seqCNT-30',
        'FcHeaderOxID': 'fcHLORequest.header.fcHeader.oxID-31',
        'FcHeaderRxID': 'fcHLORequest.header.fcHeader.rxID-32',
        'FcHeaderParameter': 'fcHLORequest.header.fcHeader.parameter-33',
        'HeaderFcCmd': 'fcHLORequest.header.fcCmd-34',
        'FspfHeaderFspfCommand': 'fcHLORequest.header.fspfHeader.fspfCommand-35',
        'FspfHeaderFspVersion': 'fcHLORequest.header.fspfHeader.fspVersion-36',
        'FspfHeaderFspfObsolete': 'fcHLORequest.header.fspfHeader.fspfObsolete-37',
        'FspfHeaderFspfAuthType': 'fcHLORequest.header.fspfHeader.fspfAuthType-38',
        'FspfHeaderFspfReserved': 'fcHLORequest.header.fspfHeader.fspfReserved-39',
        'FspfHeaderFspfOrigDID': 'fcHLORequest.header.fspfHeader.fspfOrigDID-40',
        'FspfHeaderFspfAuth': 'fcHLORequest.header.fspfHeader.fspfAuth-41',
        'HeaderReserved1': 'fcHLORequest.header.reserved1-42',
        'HeaderHelloInterval': 'fcHLORequest.header.helloInterval-43',
        'HeaderDeadInterval': 'fcHLORequest.header.deadInterval-44',
        'HeaderRecipientDID': 'fcHLORequest.header.recipientDID-45',
        'HeaderReserved2': 'fcHLORequest.header.reserved2-46',
        'HeaderOrigPortIndex': 'fcHLORequest.header.origPortIndex-47',
    }

    def __init__(self, parent, list_op=False):
        super(FCHLORequest, self).__init__(parent, list_op)

    @property
    def FcHeaderRCTL(self):
        """
        Display Name: R_CTL
        Default Value: 2
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderRCTL']))

    @property
    def FcHeaderDstId(self):
        """
        Display Name: Destination ID
        Default Value: 0
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderDstId']))

    @property
    def FcHeaderCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderCsCTLPriority']))

    @property
    def FcHeaderSrcId(self):
        """
        Display Name: Source ID
        Default Value: 0
        Value Format: fCID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderSrcId']))

    @property
    def FcHeaderType(self):
        """
        Display Name: Type
        Default Value: 22
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderType']))

    @property
    def FcHeaderSof(self):
        """
        Display Name: SOF
        Default Value: -1128974794
        Value Format: decimal
        Available enum values: SOFf - Fabric, 3166001232, SOFi4 - Initiate Class 4, 3166001497, SOFi2 - Initiate Class 2, 3166000469, SOFi3 - Initiate Class 3, 3166000726, SOFn4 - Normal Class 4, 3165993273, SOFn2 - Normal Class 2, 3165992245, SOFn3 - Normal Class 3, 3165992502, SOFc4 - Connect Class 4, 3165985049, SOFn1 - Normal Class 1 or 6, 3165992759
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderSof']))

    @property
    def FCTLCustom(self):
        """
        Display Name: Custom
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FCTLCustom']))

    @property
    def BuildFCTLExchangeContext(self):
        """
        Display Name: Exchange Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Originator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLExchangeContext']))

    @property
    def BuildFCTLSequenceContext(self):
        """
        Display Name: Sequence Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Initiator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLSequenceContext']))

    @property
    def BuildFCTLFirstSequence(self):
        """
        Display Name: First Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, First, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLFirstSequence']))

    @property
    def BuildFCTLLastSequence(self):
        """
        Display Name: Last Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLLastSequence']))

    @property
    def BuildFCTLEndSequence(self):
        """
        Display Name: End Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLEndSequence']))

    @property
    def BuildFCTLEndConnection(self):
        """
        Display Name: End Connection
        Default Value: 0
        Value Format: decimal
        Available enum values: Alive, 0, Pending, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLEndConnection']))

    @property
    def BuildFCTLCsCTLPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0
        Value Format: decimal
        Available enum values: CS_CTL, 0, Priority, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLCsCTLPriority']))

    @property
    def BuildFCTLSequenceInitiative(self):
        """
        Display Name: Sequence Initiative
        Default Value: 0
        Value Format: decimal
        Available enum values: Hold, 0, Transfer, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLSequenceInitiative']))

    @property
    def BuildFCTLFcXIDReassigned(self):
        """
        Display Name: FC XID Reassigned
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLFcXIDReassigned']))

    @property
    def BuildFCTLFcInvalidateXID(self):
        """
        Display Name: FC Invalidate XID
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLFcInvalidateXID']))

    @property
    def BuildFCTLAckForm(self):
        """
        Display Name: ACK_Form
        Default Value: 0
        Value Format: decimal
        Available enum values: No assistance provided, 0, ACK_1 Required, 1, reserved, 2, Ack_0 Required, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLAckForm']))

    @property
    def BuildFCTLFcDataCompression(self):
        """
        Display Name: FC Data Compression
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLFcDataCompression']))

    @property
    def BuildFCTLFcDataEncryption(self):
        """
        Display Name: FC Data Encryption
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLFcDataEncryption']))

    @property
    def BuildFCTLRetransmittedSequence(self):
        """
        Display Name: Retransmitted Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Original, 0, Retransmission, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLRetransmittedSequence']))

    @property
    def BuildFCTLUnidirectionalTransmit(self):
        """
        Display Name: Unidirectional Transmit
        Default Value: 0
        Value Format: decimal
        Available enum values: Bi-directional, 0, Unidirectional, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLUnidirectionalTransmit']))

    @property
    def BuildFCTLContinueSeqCondition(self):
        """
        Display Name: Continue Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: No information, 0, Sequence to follow-immediately, 1, Squence to follow-soon, 2, Sequence to follow-delayed, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLContinueSeqCondition']))

    @property
    def BuildFCTLAbortSeqCondition(self):
        """
        Display Name: Abort Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: 0x00, 0, 0x01, 1, 0x10, 2, 0x11, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLAbortSeqCondition']))

    @property
    def BuildFCTLRelativeOffsetPresent(self):
        """
        Display Name: Relative Offset Present
        Default Value: 0
        Value Format: decimal
        Available enum values: Parameter field defined, 0, Relative offset, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLRelativeOffsetPresent']))

    @property
    def BuildFCTLExchangeReassembly(self):
        """
        Display Name: Exchange Reassembly
        Default Value: 0
        Value Format: decimal
        Available enum values: off, 0, on, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLExchangeReassembly']))

    @property
    def BuildFCTLFillBytes(self):
        """
        Display Name: Fill Bytes
        Default Value: 0
        Value Format: decimal
        Available enum values: 0 bytes of fill, 0, 1 bytes of fill, 1, 2 bytes of fill, 2, 3 bytes of fill, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BuildFCTLFillBytes']))

    @property
    def FcHeaderSeqID(self):
        """
        Display Name: SEQ_ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderSeqID']))

    @property
    def FcHeaderDfCTL(self):
        """
        Display Name: DF_CTL
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderDfCTL']))

    @property
    def FcHeaderSeqCNT(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderSeqCNT']))

    @property
    def FcHeaderOxID(self):
        """
        Display Name: OX_ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderOxID']))

    @property
    def FcHeaderRxID(self):
        """
        Display Name: RX_ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderRxID']))

    @property
    def FcHeaderParameter(self):
        """
        Display Name: Parameter
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FcHeaderParameter']))

    @property
    def HeaderFcCmd(self):
        """
        Display Name: FC Command
        Default Value: 335544320
        Value Format: decimal
        Available enum values: SW_RJT, 16777216, SW_ACC, 33554432, ELP, 268435456, EFP, 285212672, DIA, 301989888, RDI, 318767104, HLO, 335544320, LSU, 352321536, LSA, 369098752, BF, 385875968, RCF, 402653184, SW_RSCN, 452984832, DRLIR, 503316480, DSCN, 536870912, LOOPD, 553648128, MR, 570425344, ACA, 587202560, RCA, 603979776, SFC, 620756992, UFC, 637534208, CEC, 687865856, EACA, 704708608, ESFC, 704774144, EUFC, 704839680, ERCA, 704905216, TCO, 704970752, ESC, 805306368, ESS, 822083584, MRRA, 872415232, STR, 889257984, EVFP, 905969664, FFI, 1342177280
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderFcCmd']))

    @property
    def FspfHeaderFspfCommand(self):
        """
        Display Name: Command
        Default Value: 0x14000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FspfHeaderFspfCommand']))

    @property
    def FspfHeaderFspVersion(self):
        """
        Display Name: Version
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FspfHeaderFspVersion']))

    @property
    def FspfHeaderFspfObsolete(self):
        """
        Display Name: Obsolete
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FspfHeaderFspfObsolete']))

    @property
    def FspfHeaderFspfAuthType(self):
        """
        Display Name: Authentication Type
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FspfHeaderFspfAuthType']))

    @property
    def FspfHeaderFspfReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FspfHeaderFspfReserved']))

    @property
    def FspfHeaderFspfOrigDID(self):
        """
        Display Name: Originating Domain_ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FspfHeaderFspfOrigDID']))

    @property
    def FspfHeaderFspfAuth(self):
        """
        Display Name: Authentication
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FspfHeaderFspfAuth']))

    @property
    def HeaderReserved1(self):
        """
        Display Name: Reserved1
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderReserved1']))

    @property
    def HeaderHelloInterval(self):
        """
        Display Name: Hello_Interval
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderHelloInterval']))

    @property
    def HeaderDeadInterval(self):
        """
        Display Name: Dead_Interval
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderDeadInterval']))

    @property
    def HeaderRecipientDID(self):
        """
        Display Name: Recipient Domain_ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderRecipientDID']))

    @property
    def HeaderReserved2(self):
        """
        Display Name: Reserved2
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderReserved2']))

    @property
    def HeaderOrigPortIndex(self):
        """
        Display Name: Originating Port Index
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderOrigPortIndex']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
