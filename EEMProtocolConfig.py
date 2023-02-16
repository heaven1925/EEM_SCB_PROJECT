"""
EEM_SCB_PROJECT
@a.ertekin
Protocol functions and bitfield operations
"""

import ctypes
import array as arr
from bitstring import BitArray


# Define a C-style structure using ctypes
class canPacked(ctypes.Structure):
    _fields_ = [
        ('canByte1', ctypes.c_byte),
        ('canByte2', ctypes.c_byte),
        ('canByte3', ctypes.c_byte),
        ('canByte4', ctypes.c_byte),
        ('canByte5', ctypes.c_byte),
        ('canByte6', ctypes.c_byte),
        ('canByte7', ctypes.c_byte),
        ('canByte8', ctypes.c_byte),
    ]

class canPackHandle(ctypes.Union):
    _fields_ = [
        ('rawpack', ctypes.c_uint64),
        ('canPack', canPacked),
    ]

def getCanPackHandle(param):
    canRawBytes = canPackHandle()
    canRawBytes.canPack.canByte1 = param[0]
    canRawBytes.canPack.canByte2 = param[1]
    canRawBytes.canPack.canByte3 = param[2]
    canRawBytes.canPack.canByte4 = param[3]
    canRawBytes.canPack.canByte5 = param[4]
    canRawBytes.canPack.canByte6 = param[5]
    canRawBytes.canPack.canByte7 = param[6]
    canRawBytes.canPack.canByte8 = param[7]
    return canRawBytes

class HVAC_MESSAGE01():
    def __init__(self):
        self.HVAC_LED01     = 0
        self.HVAC_LED02     = 0
        self.HVAC_LED03     = 0
        self.HVAC_LED04     = 0
        self.HVAC_LED05     = 0
        self.HVAC_LED06     = 0
        self.HVAC_LED07     = 0
        self.HVAC_LED08     = 0
        self.HVAC_LED09     = 0
        self.HVAC_LED10     = 0
        self.HVAC_LED11     = 0
        self.HVAC_LED12     = 0
        self.HVAC_FIRE      = 0
        self.HVAC_PRESSURE  = 0
        self.HVAC_RTC_CALIB = 0
        self.HVAC_RTC_SEC   = 0
        self.HVAC_RTC_MIN   = 0
        self.HVAC_RTC_HOUR  = 0
        self.HVAC_RTC_DAY   = 0
        self.HVAC_RTC_MONTH = 0
        self.HVAC_RTC_YEAR  = 0
        #######################
        self.bits64 = 0
    ################################################################################################################
    def getBits(self, bits):
        self.bits64 = bits
    ################################################################################################################
    def getLed01(self): # 1 Bit
        self.HVAC_LED01 =       ( self.bits64 & 0x0000000000000001 )
        return self.HVAC_LED01
    def getLed02(self): # 1 Bit
        self.HVAC_LED02 = (     ( self.bits64 & 0x0000000000000002 ) >> 1 )
        return self.HVAC_LED02
    def getLed03(self): # 1 Bit
        self.HVAC_LED03 = (     ( self.bits64 & 0x0000000000000004 ) >> 2 )
        return self.HVAC_LED03
    def getLed04(self): # 1 Bit
        self.HVAC_LED04 = (     ( self.bits64 & 0x0000000000000008 ) >> 3 )
        return self.HVAC_LED04
    def getLed05(self): # 1 Bit
        self.HVAC_LED05 = (     ( self.bits64 & 0x0000000000000010 ) >> 4 )
        return self.HVAC_LED05
    def getLed06(self): # 1 Bit
        self.HVAC_LED06 = (     ( self.bits64 & 0x0000000000000020 ) >> 5 )
        return self.HVAC_LED06
    def getLed07(self): # 1 Bit
        self.HVAC_LED07 = (     ( self.bits64 & 0x0000000000000040 ) >> 6 )
        return self.HVAC_LED07
    def getLed08(self): # 1 Bit
        self.HVAC_LED08 = (     ( self.bits64 & 0x0000000000000080 ) >> 7 )
        return self.HVAC_LED08
    def getLed09(self): # 1 Bit
        self.HVAC_LED09 = (     ( self.bits64 & 0x0000000000000100 ) >> 8 )
        return self.HVAC_LED09
    def getLed10(self): # 1 Bit
        self.HVAC_LED10 = (    ( self.bits64 & 0x0000000000000200 ) >> 9 )
        return self.HVAC_LED10
    def getLed11(self): # 1 Bit
        self.HVAC_LED11 = (     ( self.bits64 & 0x0000000000000400 ) >> 10 )
        return self.HVAC_LED11
    def getLed12(self): # 1 Bit
        self.HVAC_LED12 = (     ( self.bits64 & 0x0000000000000800 ) >> 11 )
        return self.HVAC_LED12
    def getFire(self):  # 3 Bit
        self.HVAC_FIRE = (      ( self.bits64 & 0x0000000000007000 ) >> 12 )
        return self.HVAC_FIRE
    def getPressure(self): # 8 Bit
        self.HVAC_PRESSURE = (  ( self.bits64 & 0x0000000000078000 ) >> 15 )
        return self.HVAC_PRESSURE
    def getRTC_Calib(self): # 1 Bit
        self.HVAC_RTC_CALIB = ( (self.bits64 & 0x0000000000008000) >> 23)
        return self.HVAC_RTC_CALIB
    def getRTC_Second(self): # 8 bit
        self.HVAC_RTC_SEC =  (  (self.bits64 & 0x0000000000FF0000) >> 24)
        return self.HVAC_RTC_SEC
    def getRTC_Minutes(self): # 8 bit
        self.HVAC_RTC_MIN = (   (self.bits64 & 0x00000000FF000000) >> 32)
        return self.HVAC_RTC_MIN
    def getRTC_Hour(self): # 8 bit
        self.HVAC_RTC_HOUR = (  (self.bits64 & 0x000000FF00000000) >> 40)
        return self.HVAC_RTC_HOUR
    def getRTC_Day(self): # 8 bit
        self.HVAC_RTC_DAY = (   (self.bits64 & 0x0000FF0000000000) >> 48)
        return self.HVAC_RTC_DAY
    def getRTC_MONTH(self): # 8 bit
        self.HVAC_RTC_MONTH = ( (self.bits64 & 0x00FF000000000000 ) >> 52)
        return self.HVAC_RTC_MONTH
    def getRTC_YEAR(self): # 8 bit
        self.HVAC_RTC_MONTH = ( (self.bits64 & 0xFF00000000000000 ) >> 56)
        return self.HVAC_RTC_MONTH
    def getAllparam(self):
        self.getLed01()
        self.getLed02()
        self.getLed03()
        self.getLed04()
        self.getLed05()
        self.getLed06()
        self.getLed07()
        self.getLed08()
        self.getLed09()
        self.getLed10()
        self.getLed11()
        self.getLed12()
        self.getFire()
        self.getPressure()
        self.getRTC_Calib()
        self.getRTC_Second()
        self.getRTC_Minutes()
        self.getRTC_Hour()
        self.getRTC_Day()
        self.getRTC_MONTH()
        self.getRTC_YEAR()
# CAN 'den gelen 8 byte data

canTest = [0xAA , 0xFA , 0xFF , 0xFF , 0xFF , 0xFF , 0xFF , 0xFF ]
# CAN 'den gelen data byte byte handle ediliyor.
HVAC_MSG01 = getCanPackHandle(canTest)

print(hex(HVAC_MSG01.rawpack))
print(hex(HVAC_MSG01.canPack.canByte1))
print(hex(HVAC_MSG01.canPack.canByte2))
print(hex(HVAC_MSG01.canPack.canByte2))
print(hex(HVAC_MSG01.canPack.canByte3))
print(hex(HVAC_MSG01.canPack.canByte4))
print(hex(HVAC_MSG01.canPack.canByte5))
print(hex(HVAC_MSG01.canPack.canByte6))
print(hex(HVAC_MSG01.canPack.canByte7))
print(hex(HVAC_MSG01.canPack.canByte8))

bits = BitArray(uint=HVAC_MSG01.rawpack, length=64)
HVAC_MSG01_PACK = HVAC_MESSAGE01()
HVAC_MSG01_PACK.getBits(HVAC_MSG01.rawpack)
HVAC_MSG01_PACK.getAllparam()

print(HVAC_MSG01_PACK.getLed01())
print(HVAC_MSG01_PACK.getLed02())
print(HVAC_MSG01_PACK.getLed03())
print(HVAC_MSG01_PACK.getLed04())
print(HVAC_MSG01_PACK.getLed05())
print(HVAC_MSG01_PACK.getLed06())
print(HVAC_MSG01_PACK.getLed07())
print(HVAC_MSG01_PACK.getLed08())
print(HVAC_MSG01_PACK.getLed09())
print(HVAC_MSG01_PACK.getLed10())
print(HVAC_MSG01_PACK.getLed11())
print(HVAC_MSG01_PACK.getLed12())
print(HVAC_MSG01_PACK.getFire())
print(HVAC_MSG01_PACK.getPressure())


