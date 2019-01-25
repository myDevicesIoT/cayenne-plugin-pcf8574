"""
This module provides classes for interfacing with MCP23XXX digital I/O extensions.
"""
from myDevices.devices.i2c import I2C
from myDevices.devices.digital import GPIOPort
from myDevices.plugins.digital import DigitalInput, DigitalOutput


class PCF8574(I2C, GPIOPort):
    """Class for interacting with PCF8574 devices."""
    FUNCTIONS = [GPIOPort.IN for i in range(8)]
    
    def __init__(self, slave=0x20):
        """Initializes PCF8574 device.

        Arguments:
        slave: The slave address
        """
        slave = int(slave)
        if slave in range(0x20, 0x28):
            self.name = "PCF8574"
        elif slave in range(0x38, 0x40):
            self.name = "PCF8574A"
        else:
            raise ValueError("Bad slave address for PCF8574(A) : 0x%02X not in range [0x20..0x27, 0x38..0x3F]" % slave)     
        I2C.__init__(self, slave)
        GPIOPort.__init__(self, 8)
        self.portWrite(0xFF)
        self.portRead()
    
    def __str__(self):
        """Returns friendly name."""
        return "%s(slave=0x%02X)" % (self.name, self.slave)
        
    def __getFunction__(self, channel):
        """Returns the current IN/OUT function for the specified channel. Overrides GPIOPort.__getFunction__."""
        return self.FUNCTIONS[channel]
    
    def __setFunction__(self, channel, value):
        """Sets the IN/OUT function for the specified channel. Overrides GPIOPort.__setFunction__."""
        if not value in [self.IN, self.OUT]:
            raise ValueError("Requested function not supported")
        self.FUNCTIONS[channel] = value
        
    def __digitalRead__(self, channel):
        """Returns the value for the specified channel. Overrides GPIOPort.__digitalRead__."""
        mask = 1 << channel
        d = self.readByte()
        return (d & mask) == mask 

    def __portRead__(self):
        """Returns all values for the GPIO device as bits in an int. Overrides GPIOPort.__portRead__."""
        return self.readByte()
    
    def __digitalWrite__(self, channel, value):
        """Writes the value to the specified channel. Overrides GPIOPort.__digitalWrite__."""
        mask = 1 << channel
        b = self.readByte()
        if value:
            b |= mask
        else:
            b &= ~mask
        self.writeByte(b)

    def __portWrite__(self, value):
        """Writes all values for the GPIO device using the bits in the specified value. Overrides GPIOPort.__portWrite__."""
        self.writeByte(value)

        
class PCF8574A(PCF8574):
    """Class for interacting with PCF8574 devices."""

    def __init__(self, slave=0x38):
        """Initializes PCF8574 device.

        Arguments:
        slave: The slave address
        """
        PCF8574.__init__(self, slave)
        

class PCFTest(PCF8574):
    """Class for simulating a PCF8574 device."""

    def __init__(self):
        """Initializes the test class."""
        self.byte = 0
        PCF8574.__init__(self)

    def readByte(self):
        """Read a byte."""
        return self.byte

    def writeByte(self, data):
        """Write data byte."""
        self.byte = data      