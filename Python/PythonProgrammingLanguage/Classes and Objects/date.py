# date.py


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, s):
        date = s.split('-')
        return cls(int(date[0]), int(date[1]), int(date[2]))

    @classmethod
    def today(cls):
        import time
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


class DateSubClass(Date):
    def yow(self):
        pass


print("""
>>> d = Date(2016, 12, 6)
>>> e = Date.from_string('2017-09-08')
>>> d.year
2016
>>> d.day
6
>>> e.month
9
>>> e.day
8
>>> e.year
2017
>>> f = Date.today()
>>> f.year
2017
>>> f.day
12
>>> f.month
6
>>> r = DateSubClass(2016, 8, 9)
>>> r.day
9
>>> r.year
2016
>>> s = DateSubClass.from_string('2015-12-3')
>>> s.day
3
>>> s.year
2015
>>> s.month
12
>>> type(s)
<class '__main__.DateSubClass'>
>>> t = DateSubClass.today()
>>> t.day
12
>>> t.month
6
>>> t.year
2017
>>> type(t)
<class '__main__.DateSubClass'>
""")

