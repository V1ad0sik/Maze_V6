from ctypes import *
from ctypes.wintypes import *


class Memory():
    class Read():
        def int(Address):
            Buffer = c_int()
            windll.kernel32.ReadProcessMemory(Memory.Handle, Address, byref(Buffer), sizeof(Buffer), 0)

            return Buffer.value


    class Write():
        def float(Address, Value):
            _Value = c_float(Value)
            windll.kernel32.WriteProcessMemory(Memory.Handle, Address, byref(_Value), sizeof(_Value), 0)


        def bool(Address, Value):
            _Value = c_bool(Value)
            windll.kernel32.WriteProcessMemory(Memory.Handle, Address, byref(_Value), sizeof(_Value), 0)