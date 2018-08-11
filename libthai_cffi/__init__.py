from . import _libthai, exception


class Breaker:
    def __init__(self, dictpath=_libthai.ffi.NULL):
        breaker = _libthai.lib.th_brk_new(dictpath)

        if breaker == _libthai.ffi.NULL:
            raise exception.InitError

        self._breaker = _libthai.ffi.gc(breaker, _libthai.lib.th_brk_delete)

    def find_breaks(self, text, count=100):
        positions = _libthai.ffi.new("int[]", count)

        actual_count = _libthai.lib.th_brk_wc_find_breaks(self._breaker, text, positions, count)

        out = []
        for i in range(actual_count):
            out.append(positions[i])

        return out

    def find_breaks_text(self, text, count=100):
        breaks = self.find_breaks(text, count)
        out = []

        last_index = 0

        for index in breaks:
            out.append(text[last_index:index])
            last_index = index

        out.append(text[last_index:])

        return out


def find_breaks(text, count=100):
    return Breaker().find_breaks(text, count)


def find_breaks_text(text, count=100):
    return Breaker().find_breaks_text(text, count)


def normalize(text):
    size = len(text)
    out = _libthai.ffi.new("thwchar_t[]", size)
    _libthai.lib.th_wnormalize(out, text, size)

    return _libthai.ffi.string(out, size)
