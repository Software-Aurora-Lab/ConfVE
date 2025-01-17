class OptionTuningItem:

    def __init__(self, position, option_type, option_key, pre_value, cur_value, option_obj):
        self.position = position
        self.option_type = option_type
        self.option_key = option_key
        self.pre_value = pre_value
        self.cur_value = cur_value
        self.option_obj = option_obj

    def __str__(self):
        return f"position: {self.position}, type:{self.option_type}, key: {self.option_key}, pre_value: {self.pre_value}, cur_value: {self.cur_value}"
