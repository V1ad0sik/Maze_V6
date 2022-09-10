from pymem import *
from re import *


class GlobalWallHack():
    def Start():
        Game = Pymem("csgo.exe")

        Client = pymem.process.module_from_name(Game.process_handle,"client.dll")
        ClientModule = Game.read_bytes(Client.lpBaseOfDll, Client.SizeOfImage)

        Address = Client.lpBaseOfDll + search(rb'\x83\xF8.\x8B\x45\x08\x0F', ClientModule).start() + 2
        Game.write_uchar(Address, 2 if Game.read_uchar(Address) == 1 else 1)

        Game.close_process()