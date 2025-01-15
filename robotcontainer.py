import wpilib
from commands2 import CommandScheduler
from elevator import ElevatorSubsystem
from move_elevator import MoveElevatorCommand

class RobotContainer:
    def __init__(self):
        # Joystick
        self.joystick = wpilib.Joystick(0)

        # Subsystems
        self.elevator = ElevatorSubsystem(motor_id=5, upper_limit_channel=0, lower_limit_channel=1)
        self.drivetrain = DriveTrain()  
        self.limelight = limelight()
        # Commands
        self.elevator_up_command = MoveElevatorCommand(self.elevator, 0.5)  # Move up
        self.elevator_down_command = MoveElevatorCommand(self.elevator, -0.5)  # Move down
        self.align_to_target_command = AlignToTargetCommand(self.drivetrain, self.limelight)

        # Button bindings
        self.configureButtonBindings()

    def configureButtonBindings(self):
        # Assign joystick buttons to elevator commands
        wpilib.Button(self.joystick, 1).whenHeld(self.elevator_up_command)  # Button 1 moves up
        wpilib.Button(self.joystick, 2).whenHeld(self.elevator_down_command)  # Button 2 moves down
        wpilib.Button(self.joystick, 3).whenHeld(self.align_to_target_command)
    def getAutonomousCommand(self):
        # No autonomous commands in this example
        return None

if __name__ == "__main__":
    wpilib.run(RobotContainer)