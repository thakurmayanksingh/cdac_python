"""
Assignment 1: Smart Home Appliance Control
Scenario
You are designing a control model for a smart home thermostat. The target temperature must be guarded against invalid bounds (e.g., set too high or too low, causing damage or excessive energy usage).

Problem Description
Create a class named SmartThermostat that implements the following specifications:

Class-level Constant Variables:
MIN_TEMP = 10.0 (float)
MAX_TEMP = 35.0 (float)
Constructor (__init__):
Accepts parameters: appliance_name (string) and initial_temp (float).
Sets a private attribute __appliance_name (assigned from appliance_name).
Sets a private attribute __target_temp (float). Call the setter property inside the constructor or perform checks to ensure that if the initial_temp is out of the [MIN_TEMP, MAX_TEMP] bounds, it defaults to 22.0.
Properties:
target_temp (read-write property):
Getter: Returns the value of __target_temp.
Setter: Checks if the new temperature is within the range [MIN_TEMP, MAX_TEMP] inclusive. If valid, updates __target_temp. If invalid, raises a ValueError with message: "Temperature must be between 10.0 and 35.0 degrees."
appliance_name (read-only property):
Getter: Returns __appliance_name.
(No setter defined, making it read-only after creation).
Example Walkthrough
thermostat = SmartThermostat("Living Room AC", 24.0)
print(thermostat.appliance_name)  # Output: Living Room AC
print(thermostat.target_temp)     # Output: 24.0

thermostat.target_temp = 28.0     # Updates successfully
print(thermostat.target_temp)     # Output: 28.0

try:
    thermostat.target_temp = 5.0  # Out of range!
except ValueError as e:
    print(e)  # Output: Temperature must be between 10.0 and 35.0 degrees.
"""

class SmartThermostat:
    '''Class SmartThermostat for the logic!'''
    MIN_TEMP = 10.0
    MAX_TEMP = 35.0
    DEFAULT_TEMP = 22.0

    def __init__(self, appliance_name:str, initial_temp:float):
        self.__appliance_name = appliance_name
        if initial_temp >= SmartThermostat.MIN_TEMP and initial_temp <= SmartThermostat.MAX_TEMP:
            self.__target_temp = initial_temp
        else:
            self.__target_temp = SmartThermostat.DEFAULT_TEMP

        
    @property
    def target_temp(self):
        return self.__target_temp

    @target_temp.setter
    def target_temp(self, temp):
        if temp <= SmartThermostat.MAX_TEMP and temp >= SmartThermostat.MIN_TEMP:
            self.__target_temp = temp
        else:
            raise ValueError("Temperature must be between 10.0 and 35.0 degrees.")

    @property
    def appliance_name(self):
        return self.__appliance_name



def main():
    '''Main method.
    Input is simply copied as mentioned in the question.'''
    thermostat = SmartThermostat("Living Room AC", 24.0)
    print(thermostat.appliance_name)  # Output: Living Room AC
    print(thermostat.target_temp)     # Output: 24.0

    thermostat.target_temp = 28.0     # Updates successfully
    print(thermostat.target_temp)     # Output: 28.0

    try:
        thermostat.target_temp = 5.0  # Out of range!
    except ValueError as e:
        print(e)  # Output: Temperature must be between 10.0 and 35.0 degrees.


if __name__ == "__main__": main()