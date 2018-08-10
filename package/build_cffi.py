import cffi

ffibuilder = cffi.FFI()
ffibuilder.cdef(
    """
typedef wchar_t thwchar_t;
typedef ... ThBrk;

ThBrk *th_brk_new(const char *dictpath);
void th_brk_delete(ThBrk *brk);
int th_brk_wc_find_breaks (ThBrk *brk, const thwchar_t *s, int pos[], size_t pos_sz);
size_t th_wnormalize(thwchar_t dest[], const thwchar_t *src, size_t n);
"""
)
ffibuilder.set_source(
    "libthai_cffi._libthai",
    """
#include <thai/thwchar.h>
#include <thai/thwbrk.h>
#include <thai/thwstr.h>
""",
    libraries=["thai"],
)
