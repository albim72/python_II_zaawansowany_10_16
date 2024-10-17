class AttributeValidator(type):
    def __new__(cls,name,bases,attrs):
        print(attrs.items())

        for attr_name,attr_value in attrs.items():
            if not attr_name.startswith("__"):
                if not isinstance(attr_value,int):
                    raise TypeError(f"{attr_name} musi by w typie int")
        return super().__new__(cls,name,bases,attrs)

try:
    class SpecClass(metaclass=AttributeValidator):
        x=89
        y=534
        z=2

except TypeError as te:
    print(te)

