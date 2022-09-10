from pymem import *
from re import *


class ShowMoney():
    def Start():
        Game = Pymem("csgo.exe")

        Client = pymem.process.module_from_name(Game.process_handle,"client.dll")
        ClientModule = Game.read_bytes(Client.lpBaseOfDll, Client.SizeOfImage)

        Address = Client.lpBaseOfDll + search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF', ClientModule).start()
        Game.write_uchar(Address, 0xEB if Game.read_uchar(Address) == 0x75 else 0x75)

        Game.close_process()