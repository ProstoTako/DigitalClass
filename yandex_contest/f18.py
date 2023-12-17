import re


class Field(dict):
    pattern_key = re.compile(r'([a-zA-Z][1-9][0-9]*$)|([1-9][0-9]*[a-zA-Z]$)')

    def __getitem__(self, key):
        Field.check(key)
        return super(Field, self).__getitem__(frozenset(Field.transform(key)))

    def __setitem__(self, key, value):
        Field.check(key)
        super(Field, self).__setitem__(frozenset(Field.transform(key)), value)

    def __delitem__(self, key):
        Field.check(key)
        super(Field, self).__delitem__(frozenset(Field.transform(key)))

    def __contains__(self, item):
        Field.check(item)
        item = Field.transform(item)
        return self[item] != self.__missing__(1)

    def __next__(self):
        if self.value < len(self):
            i = self.value
            self.value += 1
            return list(self.items())[i][1]
        else:
            raise StopIteration

    def __iter__(self):
        self.value = 0
        return self

    def __missing__(self, key):
        return None
                
    @classmethod
    def check(cls, key) -> None:
        if not isinstance(key, (str, tuple)):
            raise TypeError
        if isinstance(key, str):
            if cls.pattern_key.match(key) == None:
                raise ValueError
        elif isinstance(key, tuple):
            if len(key) != 2:
                raise TypeError
            key = str(key[0]) + str(key[1])
            if cls.pattern_key.match(key) == None:
                raise ValueError                

    @staticmethod
    def transform(key) -> str:
        return key.upper() if isinstance(key, str) else (str(key[0])+str(key[1])).upper()

