
class ConfigFileObj:

    def __init__(self, raw_option_stack, option_tuple_list, option_obj_list, option_count):
        self.raw_option_stack = raw_option_stack
        self.option_tuple_list = option_tuple_list
        self.option_obj_list = option_obj_list
        self.option_count = option_count

        self.option_type_list = [option_obj.option_type for option_obj in option_obj_list]
        self.default_option_value_list = [option_obj.option_value for option_obj in option_obj_list]


