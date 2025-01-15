import wpilib
from wpilib import DigitalInput
from commands2 import SubsystemBase
from ctre import TalonFX, ControlMode
import ctre
class ElevatorSubsystem(SubsystemBase):
    def __init__(self, motor_id: int, upper_limit_channel: int, lower_limit_channel: int):
        super().__init__()

        # Falcon 5000 motor controller
        self.motor = TalonFX(motor_id)

        # Limit switches
        self.upper_limit_switch = DigitalInput(upper_limit_channel)
        self.lower_limit_switch = DigitalInput(lower_limit_channel)

        # Motor safety configuration
        self.motor.configFactoryDefault()
        self.motor.setNeutralMode(ctre.NeutralMode.Brake)

    def move(self, speed: float):
        """
        Moves the elevator up or down at the specified speed.

        :param speed: Speed of the motor (-1.0 to 1.0).
        """
        if speed > 0 and not self.upper_limit_switch.get():
            # Prevent upward movement if the upper limit is hit
            self.motor.set(ControlMode.PercentOutput, 0)
        elif speed < 0 and not self.lower_limit_switch.get():
            # Prevent downward movement if the lower limit is hit
            self.motor.set(ControlMode.PercentOutput, 0)
        else:
            # Normal movement
            self.motor.set(ControlMode.PercentOutput, speed)

    def stop(self):
        """
        Stops the elevator motor.
        """
        self.motor.set(ControlMode.PercentOutput, 0)

    def at_upper_limit(self):
        """
        Checks if the upper limit switch is triggered.
        """
        return not self.upper_limit_switch.get()

    def at_lower_limit(self):
        """
        Checks if the lower limit switch is triggered.
        """
        return not self.lower_limit_switch.get()
