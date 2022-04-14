from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class FipElpSwAccFcf(Base):
    __slots__ = ()
    _SDM_NAME = "fipElpSwAccFcf"
    _SDM_ATT_MAP = {
        "HeaderFipVersion": "fipElpSwAccFcf.header.fipVersion-1",
        "HeaderFipReserved": "fipElpSwAccFcf.header.fipReserved-2",
        "FipOperationCodeFipVirtualLinkInstantiation": "fipElpSwAccFcf.header.fipOperation.fipOperationCode.fipVirtualLinkInstantiation-3",
        "FipOperationFipOperationReserved1": "fipElpSwAccFcf.header.fipOperation.fipOperationReserved1-4",
        "FipSubcodeFipSubcode02h": "fipElpSwAccFcf.header.fipOperation.fipSubcode.fipSubcode02h-5",
        "FipOperationFipDescriptorListLength": "fipElpSwAccFcf.header.fipOperation.fipDescriptorListLength-6",
        "FipOperationFipFp": "fipElpSwAccFcf.header.fipOperation.fipFp-7",
        "FipOperationFipSp": "fipElpSwAccFcf.header.fipOperation.fipSp-8",
        "FipOperationFipReserved2": "fipElpSwAccFcf.header.fipOperation.fipReserved2-9",
        "FipOperationFipABit": "fipElpSwAccFcf.header.fipOperation.fipABit-10",
        "FipOperationFipSBit": "fipElpSwAccFcf.header.fipOperation.fipSBit-11",
        "FipOperationFipFBit": "fipElpSwAccFcf.header.fipOperation.fipFBit-12",
        "FipElpDescriptorFipElpDescriptorType": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorType-13",
        "FipElpDescriptorFipElpDescriptorLength": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorLength-14",
        "FipElpDescriptorFipElpDescriptorReserved": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorReserved-15",
        "FipElpDescriptorFibreChannelRCtlExchangeLinkParametersFipElpDescriptorFibreChannelRCtlExchangeLinkParametersRequestReply": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelRCtl.fipElpDescriptorFibreChannelRCtlExchangeLinkParameters.fipElpDescriptorFibreChannelRCtlExchangeLinkParametersRequestReply-16",
        "FipElpFibreChannelFipElpDescriptorFibreChannelDId": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelDId-17",
        "FipElpFibreChannelFipElpDescriptorFibreChannelCsCtlPriority": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelCsCtlPriority-18",
        "FipElpFibreChannelFipElpDescriptorFibreChannelSId": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelSId-19",
        "FipElpFibreChannelFipElpDescriptorFibreChannelType": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelType-20",
        "FCtlExchangeContext": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.exchangeContext-21",
        "FCtlSequenceContext": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.sequenceContext-22",
        "FCtlFirstSequence": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.firstSequence-23",
        "FCtlLastSequence": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.lastSequence-24",
        "FCtlEndSequence": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.endSequence-25",
        "FCtlEndConnection": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.endConnection-26",
        "FCtlCsCtlPriority": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.csCtlPriority-27",
        "FCtlSequenceInitiative": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.sequenceInitiative-28",
        "FCtlFcXidReassigned": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.fcXidReassigned-29",
        "FCtlFcInvalidateXid": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.fcInvalidateXid-30",
        "FCtlAckForm": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.ackForm-31",
        "FCtlFcDataCompression": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.fcDataCompression-32",
        "FCtlFcDataEncryption": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.fcDataEncryption-33",
        "FCtlRetransmittedSequence": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.retransmittedSequence-34",
        "FCtlUnidirectionalTransmit": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.unidirectionalTransmit-35",
        "FCtlContinueSeqCondition": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.continueSeqCondition-36",
        "FCtlAbortSeqCondition": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.abortSeqCondition-37",
        "FCtlRelativeOffsetPresent": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.relativeOffsetPresent-38",
        "FCtlExchangeReassembly": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.exchangeReassembly-39",
        "FCtlFillBytes": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelFCtl.fCtl.fillBytes-40",
        "FipElpFibreChannelFipElpDescriptorFibreChannelSeqId": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelSeqId-41",
        "FipElpFibreChannelFipElpDescriptorFibreChannelDfCtl": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelDfCtl-42",
        "FipElpFibreChannelFipElpDescriptorFibreChannelSeqCnt": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelSeqCnt-43",
        "FipElpFibreChannelFipElpDescriptorFibreChannelOxId": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelOxId-44",
        "FipElpFibreChannelFipElpDescriptorFibreChannelRxId": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelRxId-45",
        "FipElpFibreChannelFipElpDescriptorFibreChannelParameter": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpFibreChannel.fipElpDescriptorFibreChannelParameter-46",
        "FipElpDescriptorFcElpCommandCodeFipElpDescriptorFcElpCommandCodeExchangeLinkParametersReply": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommandCode.fipElpDescriptorFcElpCommandCodeExchangeLinkParametersReply-47",
        "FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersRevision": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParameters.fipElpDescriptorFcElpCommonServiceParametersRevision-48",
        "FipElpDescriptorFcElpCommonServiceParametersFlagsFipElpDescriptorFcElpCommonServiceParametersFlagsBridgePortBit": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParameters.fipElpDescriptorFcElpCommonServiceParametersFlags.fipElpDescriptorFcElpCommonServiceParametersFlagsBridgePortBit-49",
        "FipElpDescriptorFcElpCommonServiceParametersFlagsFipElpDescriptorFcElpCommonServiceParametersFlagsBridgeVirtualFabricsBit": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParameters.fipElpDescriptorFcElpCommonServiceParametersFlags.fipElpDescriptorFcElpCommonServiceParametersFlagsBridgeVirtualFabricsBit-50",
        "FipElpDescriptorFcElpCommonServiceParametersFlagsFipElpDescriptorFcElpCommonServiceParametersFlagsReserved": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParameters.fipElpDescriptorFcElpCommonServiceParametersFlags.fipElpDescriptorFcElpCommonServiceParametersFlagsReserved-51",
        "FipElpDescriptorFcElpCommonServiceParametersBbScNumberFipElpDescriptorFcElpCommonServiceParametersBbScNumberReserved": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParameters.fipElpDescriptorFcElpCommonServiceParametersBbScNumber.fipElpDescriptorFcElpCommonServiceParametersBbScNumberReserved-52",
        "FipElpDescriptorFcElpCommonServiceParametersBbScNumberFipElpDescriptorFcElpCommonServiceParametersBbScNumberBbSnN": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParameters.fipElpDescriptorFcElpCommonServiceParametersBbScNumber.fipElpDescriptorFcElpCommonServiceParametersBbScNumberBbSnN-53",
        "FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersRATov": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParameters.fipElpDescriptorFcElpCommonServiceParametersRATov-54",
        "FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersEDTov": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParameters.fipElpDescriptorFcElpCommonServiceParametersEDTov-55",
        "FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersRequesterInterconnectPortName": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParameters.fipElpDescriptorFcElpCommonServiceParametersRequesterInterconnectPortName-56",
        "FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricNodeName": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParameters.fipElpDescriptorFcElpCommonServiceParametersFabricNodeName-57",
        "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersVal": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParameters.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersVal-58",
        "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReserved1": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParameters.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReserved1-59",
        "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersXIdInterlock": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParameters.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersXIdInterlock-60",
        "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReserved2": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParameters.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReserved2-61",
        "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReceiveDataFieldSize": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParameters.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReceiveDataFieldSize-62",
        "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersConcurrentSequences": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParameters.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersConcurrentSequences-63",
        "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersEndToEndCredit": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParameters.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersEndToEndCredit-64",
        "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersOpenSequencesPerExchange": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParameters.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersOpenSequencesPerExchange-65",
        "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReserved3": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParameters.fipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReserved3-66",
        "FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpClass1InterconnectPortParameters": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpClass1InterconnectPortParameters-67",
        "FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpClass2InterconnectPortParameters": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpClass2InterconnectPortParameters-68",
        "FipElpDescriptorFcElpRequestReplyFipElpDescriptorClass3InterconnectPortParameters": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorClass3InterconnectPortParameters-69",
        "FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpReserved": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpReserved-70",
        "FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeVendorSpecific": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpIslFlowControlMode.fipElpDescriptorFcElpIslFlowControlModeVendorSpecific-71",
        "FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeRRdyFlowControl": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpIslFlowControlMode.fipElpDescriptorFcElpIslFlowControlModeRRdyFlowControl-72",
        "FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeVcRdyFlowControl": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpIslFlowControlMode.fipElpDescriptorFcElpIslFlowControlModeVcRdyFlowControl-73",
        "FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeReservedForAe2Use": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpIslFlowControlMode.fipElpDescriptorFcElpIslFlowControlModeReservedForAe2Use-74",
        "FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeReserved": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpIslFlowControlMode.fipElpDescriptorFcElpIslFlowControlModeReserved-75",
        "FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpFlowControlParameterLength": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpFlowControlParameterLength-76",
        "FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpFlowControlParameters": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipElpDescriptor.fipElpDescriptorFcElp.fipElpDescriptorFcElpRequestReply.fipElpDescriptorFcElpFlowControlParameters-77",
        "FipMacAddressDescriptorFipMacAddressDescriptorType": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorType-78",
        "FipMacAddressDescriptorFipMacAddressDescriptorLength": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorLength-79",
        "FipMacAddressDescriptorFipMacAddressDescriptorValue": "fipElpSwAccFcf.header.fipDescriptors.fipSelectFipDescriptor.fipMacAddressDescriptor.fipMacAddressDescriptorValue-80",
    }

    def __init__(self, parent, list_op=False):
        super(FipElpSwAccFcf, self).__init__(parent, list_op)

    @property
    def HeaderFipVersion(self):
        """
        Display Name: Version
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFipVersion"])
        )

    @property
    def HeaderFipReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderFipReserved"])
        )

    @property
    def FipOperationCodeFipVirtualLinkInstantiation(self):
        """
        Display Name: Virtual Link Instantiation
        Default Value: 0x0002
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipOperationCodeFipVirtualLinkInstantiation"]
            ),
        )

    @property
    def FipOperationFipOperationReserved1(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["FipOperationFipOperationReserved1"]),
        )

    @property
    def FipSubcodeFipSubcode02h(self):
        """
        Display Name: Subcode 02h
        Default Value: 0x02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipSubcodeFipSubcode02h"])
        )

    @property
    def FipOperationFipDescriptorListLength(self):
        """
        Display Name: FIP Descriptor List Length
        Default Value: 35
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipOperationFipDescriptorListLength"]
            ),
        )

    @property
    def FipOperationFipFp(self):
        """
        Display Name: FP
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipFp"])
        )

    @property
    def FipOperationFipSp(self):
        """
        Display Name: SP
        Default Value: 1
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipSp"])
        )

    @property
    def FipOperationFipReserved2(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipReserved2"])
        )

    @property
    def FipOperationFipABit(self):
        """
        Display Name: A bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipABit"])
        )

    @property
    def FipOperationFipSBit(self):
        """
        Display Name: S bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipSBit"])
        )

    @property
    def FipOperationFipFBit(self):
        """
        Display Name: F bit
        Default Value: 0
        Value Format: decimal
        Available enum values: False, 0, True, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FipOperationFipFBit"])
        )

    @property
    def FipElpDescriptorFipElpDescriptorType(self):
        """
        Display Name: ELP Descriptor Type
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpDescriptorFipElpDescriptorType"]
            ),
        )

    @property
    def FipElpDescriptorFipElpDescriptorLength(self):
        """
        Display Name: ELP Descriptor Length
        Default Value: 33
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpDescriptorFipElpDescriptorLength"]
            ),
        )

    @property
    def FipElpDescriptorFipElpDescriptorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpDescriptorFipElpDescriptorReserved"]
            ),
        )

    @property
    def FipElpDescriptorFibreChannelRCtlExchangeLinkParametersFipElpDescriptorFibreChannelRCtlExchangeLinkParametersRequestReply(
        self,
    ):
        """
        Display Name: Request/Reply
        Default Value: 3
        Value Format: decimal
        Available enum values: Request, 2, Reply, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFibreChannelRCtlExchangeLinkParametersFipElpDescriptorFibreChannelRCtlExchangeLinkParametersRequestReply"
                ]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelDId(self):
        """
        Display Name: D_ID
        Default Value: 0xFFFFFD
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelDId"]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpFibreChannelFipElpDescriptorFibreChannelCsCtlPriority"
                ]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelSId(self):
        """
        Display Name: S_ID
        Default Value: 0xFFFFFD
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelSId"]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelType(self):
        """
        Display Name: Type
        Default Value: 0x22
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelType"]
            ),
        )

    @property
    def FCtlExchangeContext(self):
        """
        Display Name: Exchange Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Originator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlExchangeContext"])
        )

    @property
    def FCtlSequenceContext(self):
        """
        Display Name: Sequence Context
        Default Value: 0
        Value Format: decimal
        Available enum values: Initiator, 0, Receipient, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlSequenceContext"])
        )

    @property
    def FCtlFirstSequence(self):
        """
        Display Name: First Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, First, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFirstSequence"])
        )

    @property
    def FCtlLastSequence(self):
        """
        Display Name: Last Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlLastSequence"])
        )

    @property
    def FCtlEndSequence(self):
        """
        Display Name: End Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Other, 0, Last, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlEndSequence"])
        )

    @property
    def FCtlEndConnection(self):
        """
        Display Name: End Connection
        Default Value: 0
        Value Format: decimal
        Available enum values: Alive, 0, Pending, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlEndConnection"])
        )

    @property
    def FCtlCsCtlPriority(self):
        """
        Display Name: CS_CTL/Priority Enable
        Default Value: 0
        Value Format: decimal
        Available enum values: CS_CTL, 0, Priority, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlCsCtlPriority"])
        )

    @property
    def FCtlSequenceInitiative(self):
        """
        Display Name: Sequence Initiative
        Default Value: 0
        Value Format: decimal
        Available enum values: Hold, 0, Transfer, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlSequenceInitiative"])
        )

    @property
    def FCtlFcXidReassigned(self):
        """
        Display Name: FC XID Reassigned
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcXidReassigned"])
        )

    @property
    def FCtlFcInvalidateXid(self):
        """
        Display Name: FC Invalidate XID
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcInvalidateXid"])
        )

    @property
    def FCtlAckForm(self):
        """
        Display Name: ACK_Form
        Default Value: 0
        Value Format: decimal
        Available enum values: No assistance provided, 0, ACK_1 Required, 1, reserved, 2, Ack_0 Required, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCtlAckForm"]))

    @property
    def FCtlFcDataCompression(self):
        """
        Display Name: FC Data Compression
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcDataCompression"])
        )

    @property
    def FCtlFcDataEncryption(self):
        """
        Display Name: FC Data Encryption
        Default Value: 0
        Value Format: decimal
        Available enum values: No, 0, Yes, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlFcDataEncryption"])
        )

    @property
    def FCtlRetransmittedSequence(self):
        """
        Display Name: Retransmitted Sequence
        Default Value: 0
        Value Format: decimal
        Available enum values: Original, 0, Retransmission, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlRetransmittedSequence"])
        )

    @property
    def FCtlUnidirectionalTransmit(self):
        """
        Display Name: Unidirectional Transmit
        Default Value: 0
        Value Format: decimal
        Available enum values: Bi-directional, 0, Unidirectional, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlUnidirectionalTransmit"])
        )

    @property
    def FCtlContinueSeqCondition(self):
        """
        Display Name: Continue Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: No information, 0, Sequence to follow-immediately, 1, Squence to follow-soon, 2, Sequence to follow-delayed, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlContinueSeqCondition"])
        )

    @property
    def FCtlAbortSeqCondition(self):
        """
        Display Name: Abort Sequence Condition
        Default Value: 0
        Value Format: decimal
        Available enum values: 0x00, 0, 0x01, 1, 0x10, 2, 0x11, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlAbortSeqCondition"])
        )

    @property
    def FCtlRelativeOffsetPresent(self):
        """
        Display Name: Relative offset present
        Default Value: 0
        Value Format: decimal
        Available enum values: Parameter field defined, 0, Relative offset, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlRelativeOffsetPresent"])
        )

    @property
    def FCtlExchangeReassembly(self):
        """
        Display Name: Exchange Reassembly
        Default Value: 0
        Value Format: decimal
        Available enum values: off, 0, on, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FCtlExchangeReassembly"])
        )

    @property
    def FCtlFillBytes(self):
        """
        Display Name: Fill Bytes
        Default Value: 0
        Value Format: decimal
        Available enum values: 0 bytes of fill, 0, 1 bytes of fill, 1, 2 bytes of fill, 2, 3 bytes of fill, 3
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FCtlFillBytes"]))

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelSeqId(self):
        """
        Display Name: SEQ_ID
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelSeqId"]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelDfCtl(self):
        """
        Display Name: DF_CTL
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelDfCtl"]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelSeqCnt(self):
        """
        Display Name: SEQ_CNT
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpFibreChannelFipElpDescriptorFibreChannelSeqCnt"
                ]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelOxId(self):
        """
        Display Name: OX_ID
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelOxId"]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelRxId(self):
        """
        Display Name: RX_ID
        Default Value: 0xFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipElpFibreChannelFipElpDescriptorFibreChannelRxId"]
            ),
        )

    @property
    def FipElpFibreChannelFipElpDescriptorFibreChannelParameter(self):
        """
        Display Name: Parameter
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpFibreChannelFipElpDescriptorFibreChannelParameter"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommandCodeFipElpDescriptorFcElpCommandCodeExchangeLinkParametersReply(
        self,
    ):
        """
        Display Name: ELP Reply
        Default Value: 0x02000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommandCodeFipElpDescriptorFcElpCommandCodeExchangeLinkParametersReply"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersRevision(
        self,
    ):
        """
        Display Name: Revision
        Default Value: 0x03
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersRevision"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFlagsFipElpDescriptorFcElpCommonServiceParametersFlagsBridgePortBit(
        self,
    ):
        """
        Display Name: Bridge Port Bit
        Default Value: 0
        Value Format: decimal
        Available enum values: E_Port, 0, B_Port, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFlagsFipElpDescriptorFcElpCommonServiceParametersFlagsBridgePortBit"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFlagsFipElpDescriptorFcElpCommonServiceParametersFlagsBridgeVirtualFabricsBit(
        self,
    ):
        """
        Display Name: Bridge Virtual Fabrics Bit
        Default Value: 0
        Value Format: decimal
        Available enum values: Does not support VFT tagged frames, 0, Supports VFT tagged frames, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFlagsFipElpDescriptorFcElpCommonServiceParametersFlagsBridgeVirtualFabricsBit"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFlagsFipElpDescriptorFcElpCommonServiceParametersFlagsReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFlagsFipElpDescriptorFcElpCommonServiceParametersFlagsReserved"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersBbScNumberFipElpDescriptorFcElpCommonServiceParametersBbScNumberReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersBbScNumberFipElpDescriptorFcElpCommonServiceParametersBbScNumberReserved"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersBbScNumberFipElpDescriptorFcElpCommonServiceParametersBbScNumberBbSnN(
        self,
    ):
        """
        Display Name: BB_SN_N
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersBbScNumberFipElpDescriptorFcElpCommonServiceParametersBbScNumberBbSnN"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersRATov(
        self,
    ):
        """
        Display Name: R_A_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersRATov"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersEDTov(
        self,
    ):
        """
        Display Name: E_D_TOV
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersEDTov"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersRequesterInterconnectPortName(
        self,
    ):
        """
        Display Name: Requester Interconnect_Port_Name
        Default Value: 0x2000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersRequesterInterconnectPortName"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricNodeName(
        self,
    ):
        """
        Display Name: Requester Switch_Name
        Default Value: 0x1000000000000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricNodeName"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersVal(
        self,
    ):
        """
        Display Name: VAL
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersVal"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReserved1(
        self,
    ):
        """
        Display Name: Reserved1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReserved1"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersXIdInterlock(
        self,
    ):
        """
        Display Name: X_ID Interlock
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersXIdInterlock"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReserved2(
        self,
    ):
        """
        Display Name: Reserved2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReserved2"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReceiveDataFieldSize(
        self,
    ):
        """
        Display Name: Receive Data Field Size
        Default Value: 2112
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReceiveDataFieldSize"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersConcurrentSequences(
        self,
    ):
        """
        Display Name: Concurrent Sequences
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersConcurrentSequences"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersEndToEndCredit(
        self,
    ):
        """
        Display Name: End-to-End Credit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersEndToEndCredit"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersOpenSequencesPerExchange(
        self,
    ):
        """
        Display Name: Open Sequences per Exchange
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersOpenSequencesPerExchange"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReserved3(
        self,
    ):
        """
        Display Name: Reserved3
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersFipElpDescriptorFcElpCommonServiceParametersFabricControllerClassFServiceParametersReserved3"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpClass1InterconnectPortParameters(
        self,
    ):
        """
        Display Name: Class 1 Interconnect_Port Parameters
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpClass1InterconnectPortParameters"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpClass2InterconnectPortParameters(
        self,
    ):
        """
        Display Name: Class 2 Interconnect_Port Parameters
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpClass2InterconnectPortParameters"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpRequestReplyFipElpDescriptorClass3InterconnectPortParameters(
        self,
    ):
        """
        Display Name: Class 3 Interconnect_Port Parameters
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpRequestReplyFipElpDescriptorClass3InterconnectPortParameters"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0000000000000000000000000000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpReserved"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeVendorSpecific(
        self,
    ):
        """
        Display Name: Vendor Specific
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeVendorSpecific"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeRRdyFlowControl(
        self,
    ):
        """
        Display Name: R_RDY Flow Control
        Default Value: 0x0002
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeRRdyFlowControl"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeVcRdyFlowControl(
        self,
    ):
        """
        Display Name: VC_RDY Flow Control
        Default Value: 0x2000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeVcRdyFlowControl"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeReservedForAe2Use(
        self,
    ):
        """
        Display Name: Reserved for AE Use
        Default Value: 0xAE02
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeReservedForAe2Use"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeReserved(
        self,
    ):
        """
        Display Name: Reserved
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpIslFlowControlModeFipElpDescriptorFcElpIslFlowControlModeReserved"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpFlowControlParameterLength(
        self,
    ):
        """
        Display Name: Flow Control Parameter Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpFlowControlParameterLength"
                ]
            ),
        )

    @property
    def FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpFlowControlParameters(
        self,
    ):
        """
        Display Name: Flow Control Parameters
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipElpDescriptorFcElpRequestReplyFipElpDescriptorFcElpFlowControlParameters"
                ]
            ),
        )

    @property
    def FipMacAddressDescriptorFipMacAddressDescriptorType(self):
        """
        Display Name: MAC Address Descriptor Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipMacAddressDescriptorFipMacAddressDescriptorType"]
            ),
        )

    @property
    def FipMacAddressDescriptorFipMacAddressDescriptorLength(self):
        """
        Display Name: MAC Address Descriptor Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "FipMacAddressDescriptorFipMacAddressDescriptorLength"
                ]
            ),
        )

    @property
    def FipMacAddressDescriptorFipMacAddressDescriptorValue(self):
        """
        Display Name: MAC Address Descriptor Value
        Default Value: 00:EE:00:00:00:00
        Value Format: mAC
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["FipMacAddressDescriptorFipMacAddressDescriptorValue"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
