from commands2 import SubsystemBase
import wpilib
import math

class LimelightSubsystem(SubsystemBase):
    def __init__(self):
        super().__init__()

        # NetworkTables for Limelight
        self.limelight_table = wpilib.NetworkTables.getTable("limelight")

    def is_target_detected(self):
        """
        Checks if the Limelight detects a valid target.
        :return: True if a target is detected, False otherwise.
        """
        return self.limelight_table.getNumber("tv", 0) == 1

    def get_horizontal_offset(self):
        """
        Gets the horizontal offset (tx) from the crosshair to the target.
        :return: Horizontal offset in degrees.
        """
        return self.limelight_table.getNumber("tx", 0)

    def get_vertical_offset(self):
        """
        Gets the vertical offset (ty) from the crosshair to the target.
        :return: Vertical offset in degrees.
        """
        return self.limelight_table.getNumber("ty", 0)

    def get_target_area(self):
        """
        Gets the target area (ta), representing how much of the image the target occupies.
        :return: Target area as a percentage (0-100).
        """
        return self.limelight_table.getNumber("ta", 0)

    def get_target_distance(self, camera_mounting_angle, camera_height, target_height):
        """
        Calculates the distance to the target based on the vertical offset (ty).
        :param camera_mounting_angle: Angle (in degrees) of the Limelight above horizontal.
        :param camera_height: Height of the Limelight from the ground (in meters).
        :param target_height: Height of the target from the ground (in meters).
        :return: Distance to the target in meters.
        """
        ty = self.get_vertical_offset()
        angle_to_target = math.radians(camera_mounting_angle + ty)
        distance = (target_height - camera_height) / math.tan(angle_to_target)
        return distance

    def set_led_mode(self, mode: int):
        """
        Sets the LED mode of the Limelight.
        :param mode: 0 = pipeline default, 1 = off, 2 = blink, 3 = on
        """
        self.limelight_table.putNumber("ledMode", mode)

    def set_camera_mode(self, mode: int):
        """
        Sets the camera mode of the Limelight.
        :param mode: 0 = vision processor, 1 = driver camera
        """
        self.limelight_table.putNumber("camMode", mode)

    def set_pipeline(self, pipeline: int):
        """
        Sets the active pipeline on the Limelight.
        :param pipeline: Pipeline number (0-9).
        """
        self.limelight_table.putNumber("pipeline", pipeline)
