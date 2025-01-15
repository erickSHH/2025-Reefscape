import wpilib
from wpilib.drive import DifferentialDrive
from wpilib import MotorControllerGroup
from rev import CANSparkMax

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.leftMotor1 = CANSparkMax(1, CANSparkMax.MotorType.kBrushless)
        self.leftMotor2 = CANSparkMax(2, CANSparkMax.MotorType.kBrushless)
        self.rightMotor1 = CANSparkMax(3, CANSparkMax.MotorType.kBrushless)
        self.rightMotor2 = CANSparkMax(4, CANSparkMax.MotorType.kBrushless)
        # Group motors for the drivetrain
        self.left_motors = MotorControllerGroup(self.left_front_motor, self.left_rear_motor)
        self.right_motors = MotorControllerGroup(self.right_front_motor, self.right_rear_motor)

        # Invert one side of the drivetrain to ensure proper direction
        self.right_motors.setInverted(True)

        # DifferentialDrive for arcade or tank drive control
        self.drive = DifferentialDrive(self.left_motors, self.right_motors)

        # Joystick for user input
        self.joystick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        # Use joystick for arcade drive control
        forward = -self.joystick.getY()  # Invert Y axis
        rotation = self.joystick.getX()
        self.drive.arcadeDrive(forward, rotation)

    def autonomousInit(self):
        # Example of autonomous initialization
        print("Autonomous mode initialized")

    def autonomousPeriodic(self):
        # Example of a simple autonomous drive forward
        self.drive.arcadeDrive(0.5, 0)  # Drive forward at 50% speed

    def disabledInit(self):
        # Stop motors when disabled
        self.drive.stopMotor()

if __name__ == "__main__":
    wpilib.run(MyRobot)
