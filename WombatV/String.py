class String:
    custom_value = ""

    @staticmethod
    def any(value, chain):
        return chain in value

    @staticmethod
    def concat(*values):
        final_string = ""
        for v in values:
            final_string = "{0} {1}".format(final_string, str(v))
        return final_string

    @staticmethod
    def count(value):
        return len(value)

    @staticmethod
    def compare(value1, value2):
        return value1 == value2
            
    @staticmethod
    def compare_values(*values):
        for v in values:
            if v != values[0]:
                return False
        return True

    @staticmethod
    def empty():
        return ""

    @staticmethod
    def ends_with(value, chain):
        return value[ len(value)-1] == str(chain)
            
    @classmethod
    def get_default_value(cls):
        return cls.custom_value

    @staticmethod
    def get_last_index(value):
        return value[-1]
        
    @staticmethod
    def get_firts_index(value):
        return  value[0]

    @staticmethod
    def more_common_word(value):
       words = value.lower().split(" ")

    @staticmethod
    def more_common_character(value):
       value = 0
       common_character = ""
       for v in value:
        if value.count(v) > value:
            value = v
            common_character = v
        return common_character

    @staticmethod
    def get_chain_to_index(value, index):
        return value[index:]

    @staticmethod
    def index_of(value, index):
        try:
            return value[index]
        except Exception as e:
            return None

    @staticmethod
    def is_empty(value):
        return value == ""
            
    @staticmethod
    def is_None_or_empty(value):
        return value == "" or value == None:
            
    @staticmethod
    def is_string(value):
        return type(value) == type(""):
            
    @staticmethod
    def is_valid_values(*values):
        for value in values:
            if type(value) == type(""):
                return False
        return True

    @staticmethod
    def remove_to_index(value, index):
        final_string = ""
        for idx, val in enumerate(value):
            if idx != index:
                final_string = "{}{}".format(final_string, val)
        return final_string          

    @classmethod
    def set_default_value(cls, value):
        cls.custom_value = value

    @staticmethod
    def start_with(value, chain):
        return value[0:len(chain)] == chain
