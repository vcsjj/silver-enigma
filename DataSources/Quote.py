def readonly_property(name):
    def ro_property_decorator(c):
        setattr(c, name, property(lambda o: o.__dict__["_" + name]))
        return c

    return ro_property_decorator


@readonly_property('date')
@readonly_property('open')
@readonly_property('high')
@readonly_property('low')
@readonly_property('close')
@readonly_property('volume')
class Quote:
    def __init__(self, date, open, high, low, close, volume):
        self._date = date
        self._open = open
        self._high = high
        self._low = low
        self._close = close
        self._volume = volume
