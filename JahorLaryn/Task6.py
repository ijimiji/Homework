class Sun(object):
    @classmethod
    def inst(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Sun, cls).__new__(cls)
        return cls.instance


s1 = Sun.inst()
s2 = Sun.inst()
print(s1 is s2)
