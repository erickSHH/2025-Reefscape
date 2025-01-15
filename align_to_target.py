from commands2 import CommandBase

class AlignToTargetCommand(CommandBase):
    def __init__(self, drivetrain, limelight):
        super().__init__()
        self.drivetrain = drivetrain  # Assumes a drivetrain subsystem exists
        self.limelight = limelight

        # Declare subsystem dependencies
        self.addRequirements([self.drivetrain, self.limelight])

    def initialize(self):
        # Turn on Limelight LEDs for vision
        self.limelight.set_led_mode(3)

    def execute(self):
        if self.limelight.is_target_detected():
            # Get horizontal offset
            tx = self.limelight.get_horizontal_offset()

            # Apply a proportional correction factor
            kP = 0.02
            turn_speed = kP * tx

            # Drive to correct alignment
            self.drivetrain.arcadeDrive(0, turn_speed)
        else:
            # Stop if no target is detected
            self.drivetrain.arcadeDrive(0, 0)

    def end(self, interrupted: bool):
        # Stop drivetrain and turn off Limelight LEDs
        self.drivetrain.arcadeDrive(0, 0)
        self.limelight.set_led_mode(1)

    def isFinished(self):
        # Finish if the horizontal offset is close enough to 0
        return abs(self.limelight.get_horizontal_offset()) < 1.0
