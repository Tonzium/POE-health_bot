from pymem import *
from pymem.process import *

mem = Pymem("PathOfExileSteam.exe")
module = module_from_name(mem.process_handle, "PathOfExileSteam.exe").lpBaseOfDll

def getPointerAddr(base, offsets):
    addr = mem.read_ulonglong(base)
    for offset in offsets:
        if offset != offsets[-1]:
            addr = mem.read_ulonglong(addr + offset)
    addr = addr + offsets[-1]
    return addr

def getCurrentHealth():
    base = module + 0x02F679F8
    offsets = [0x10, 0x2D8, 0x5E8, 0x50, 0x588]
    current_health = mem.read_int(getPointerAddr(base, offsets))
    return current_health

#def getMaximumHealth_noAura():
    #base = module + 0x030D8780
    #offsets = [0x710, 0x28, 0x50, 0x58C]
    #absolutemax_Health = mem.read_int(getPointerAddr(base, offsets))
    #return absolutemax_Health

def getMaximumHealth():
    base = module + 0x02F6ACC8
    offsets = [0x88, 0x328, 0x290]
    max_Health = mem.read_int(getPointerAddr(base, offsets))
    return max_Health

def getCurrentMana():
    base = module + 0x02F6ACC8
    offsets = [0x298, 0x80, 0x288]
    current_mana = mem.read_int(getPointerAddr(base, offsets))
    return current_mana

def getMaximumMana():
    base = module + 0x02F6ACC8
    offsets = [0x298, 0x288, 0x290]
    maximum_mana = mem.read_int(getPointerAddr(base, offsets))
    return maximum_mana

def getCurrentEnergyShield():
    base = module + 0x02F6ACC8
    offsets = [0x290, 0x48, 0x294]
    current_energyshield = mem.read_int(getPointerAddr(base, offsets))
    return current_energyshield

def getMaximumEnergyShield():
    base = module + 0x02F6ACC8
    offsets = [0x290, 0x288, 0x298]
    maximum_energyshield = mem.read_int(getPointerAddr(base, offsets))
    return maximum_energyshield
