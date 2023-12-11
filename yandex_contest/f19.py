import re

pattern_key = re.compile(r'([a-zA-Z][1-9][0-9]*$)|([1-9][0-9]*[a-zA-Z]$)')


def check(key):
    if type(key) is str:
        if pattern_key.match(key):
            return
        else:
            raise ValueError
    elif type(key) is tuple:
        if len(key) != 2:
            raise TypeError
        key = str(key[0]) + str(key[1])
        if pattern_key.match(key):
            return
        else:
            raise ValueError
    else:
        raise TypeError


def transform(key) -> str:
    return key.upper() if type(key) is str else (str(key[0])+str(key[1])).upper()


class Field(dict):
    def __getitem__(self, key):
        check(key)
        return super(Field, self).__getitem__(frozenset(transform(key)))

    def __setitem__(self, key, value):
        check(key)
        super(Field, self).__setitem__(frozenset(transform(key)), value)

    def __delitem__(self, key):
        check(key)
        super(Field, self).__delitem__(frozenset(transform(key)))

    def __contains__(self, item):
        check(item)
        item = transform(item)
        return self[item] != self.__missing__(1)

    def __next__(self):
        if self.index < len(self):
            i = self.index
            self.index += 1
            return list(self.items())[i][1]
        else:
            raise StopIteration

    def __iter__(self):
        self.index = 0
        return self

    def __missing__(self, key):
        return None

    def __setattr__(self, name, value):
        if pattern_key.match(name):
            self.__class__.__setitem__(self, name, value)
        else:
            self.__dict__[name] = value

    def __getattr__(self, item):
        if pattern_key.match(item):
            return self.__class__.__getitem__(self, item)

    def __delattr__(self, item):
        if pattern_key.match(item):
            self.__class__.__delitem__(self, item)
        else:
            del self.__dict__[item]
