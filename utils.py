class Utils:
    @staticmethod
    def get_bone_height(horizontal_position, old):
        if horizontal_position > Constants.bone_rect_width / 2:
            horizontal_position = Constants.bone_rect_width - horizontal_position
        base = Constants.bone_rect_height - horizontal_position * (Constants.bone_rect_height / 2) / (Constants.bone_rect_width / 2)
        if old:
            base = Constants.bone_rect_height - base
        return base


class Constants:
    screen_width = 700
    screen_height = 600

    bone_rect_width = screen_height
    bone_rect_height = 100
