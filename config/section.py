import enum


class SectionName(enum.Enum):
    BSS = '.bss'
    CORMETA = '.cormeta'
    DATA = '.data'
    DEBUGDOLARF = '.debug$F'
    DEBUGDOLARP = '.debug$P'
    DEBUGDOLARS = '.debug$S'
    DEBUGDOLART = '.debug$T'
    DRECTIVE = '.drective'
    EDATA = '.edata'
    IDATA = '.idata'
    IDLSYM = '.idlsym'
    PDATA = '.pdata'
    RDATA = '.rdata'
    RELOC = '.reloc'
    RSRC = '.rsrc'
    SBSS = '.sbss'
    SDATA = '.sdata'
    SRDATA = '.srdata'
    SXDATA = '.sxdata'
    TEXT = '.text'
    TLS = '.tls'
    TLSDOLAR = '.tls$'
    VSDATA = '.vsdata'
    XDATA = '.xdata'
