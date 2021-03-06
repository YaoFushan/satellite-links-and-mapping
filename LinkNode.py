# LinkNode.py
# Author: Danny Flynn
# Date Modified: 20210602
from AntennaPattern import *

class LinkNode():
    """ LinkNode represents a top-level link budget component, such as a
        ground station or satellite. Supported link types are terminal to
        satellite, satellite to terminal, satellite to satellite, or
        terminal to terminal. """
    def __init__(self):
        """ Initializes a new LinkNode """
        self.type = "generic"
    
    def get_type(self):
        """ Gets the type of LinkNode """
        return self.type

class Transmitter(LinkNode):
    """ Transmitter extends LinkNode and represents a Transmitting
        node in a link. A transmitting node has an associated antenna
        pattern."""
    def __init__(self, antenna_pattern: AntennaPattern, peak_power_output):
        """ Initializes a new Transmitter with an associated antenna
            pattern. Power output in dBm"""
        self.type = "tx_generic"
        self.tx_pattern = antenna_pattern
        self.peak_power_output = peak_power_output

    def get_eirp(self):
        return self.tx_pattern.get_gain_pattern() + self.peak_power_output

    
class TransmitSatellite(Transmitter):
    """ TransmitSatellite extends Transmitter and represents a
        transmitting satellite node in a link. The transmitting satellite
        has associated physical properties and an antenna pattern."""
    def __init__(self, antenna_pattern, peak_power_output):
        """ Initializes a new TransmitSatellite with associated antenna
            pattern and peak power amplifier output."""
        self.type = "tx_satellite"
        super.__init__(self, antenna_pattern, peak_power_output)

class TransmitTerminal(Transmitter):
    """ TransmitTerminal extends Transmitter and represents the
        characteristics of a transmitting ground station (terminal) with
        an associated antenna pattern and peak power output. The location
        of the terminal is not stored as most links will want to map out
        many possible terminal locations."""
    def __init__(self, antenna_pattern, peak_power_output):
        """ Initializes a new TransmitTerminal with associated antenna
            pattern and peak power amplifier output."""
        self.type = "tx_terminal"
        super().__init__(antenna_pattern, peak_power_output)

class Receiver(LinkNode):
    """ Receiver is the receive node in any type of link. The receive 
        node, like the transmit node, has an associated antenna pattern."""
    def __init__(self, antenna_pattern: AntennaPattern):
        """ Initializes a new Receiver with specified antenna pattern."""
        self.type = "rx_generic"
        self.rx_pattern = antenna_pattern

class ReceiveSatellite(Receiver):
    """ ReceiveSatellite represents a satellite with specified orbit and
        receiving antenna pattern."""
    def __init__(self, antenna_pattern):
        self.rx_pattern = antenna_pattern

class ReceiveTerminal(Receiver):

    def __init__(self, antenna_pattern):
        pass