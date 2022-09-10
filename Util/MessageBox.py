import ctypes

def MessageBox(Message, Title = " "):
    ctypes.windll.user32.MessageBoxW(0, Message, Title, 0)