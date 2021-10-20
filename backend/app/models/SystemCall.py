from .Artifact import Artifact


class SystemCall(Artifact):
    def __init__(self, timestamp, ip_address, mac_address, annotations, tags, SystemCallName, SystemCallArgument, SystemCallReturnValue, SystemCallType
                 ):
        super().__init__(timestamp, ip_address, mac_address, annotations, tags)
        self.SystemCallName = SystemCallName
        self.SystemCallArgument = SystemCallArgument
        self.SystemCallReturnValue = SystemCallReturnValue
        self.SystemCallReturnValue = SystemCallReturnValue
        self.SystemCallType = SystemCallType

    def toDict(self):
        return __dict__
