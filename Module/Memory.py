from ctypes import *
from ctypes.wintypes import *
from win32process import *
from win32event import *

from Module.Game import *


class Memory():
    class Read():
        def int(Address):
            Buffer = c_int()
            windll.kernel32.ReadProcessMemory(Game.Handle, Address, byref(Buffer), sizeof(Buffer), 0)

            return Buffer.value


        def float(Address):
            Buffer = c_float()
            windll.kernel32.ReadProcessMemory(Game.Handle, Address, byref(Buffer), sizeof(Buffer), 0)

            return Buffer.value


        def bool(Address):
            Buffer = c_bool()
            windll.kernel32.ReadProcessMemory(Game.Handle, Address, byref(Buffer), sizeof(Buffer), 0)

            return Buffer.value


        def byte(Address):
            Buffer = c_byte()
            windll.kernel32.ReadProcessMemory(Game.Handle, Address, byref(Buffer), sizeof(Buffer), 0)

            return Buffer.value


        def short(Address):
            Buffer = c_short()
            windll.kernel32.ReadProcessMemory(Game.Handle, Address, byref(Buffer), sizeof(Buffer), 0)

            return Buffer.value


    class Write():
        def int(Address, Value):
            _Value = c_int(Value)
            windll.kernel32.WriteProcessMemory(Game.Handle, Address, byref(_Value), sizeof(_Value), 0)


        def float(Address, Value):
            _Value = c_float(Value)
            windll.kernel32.WriteProcessMemory(Game.Handle, Address, byref(_Value), sizeof(_Value), 0)


        def bool(Address, Value):
            _Value = c_bool(Value)
            windll.kernel32.WriteProcessMemory(Game.Handle, Address, byref(_Value), sizeof(_Value), 0)
