from random import *
import sympy
p = {guess}
q = {guess}
n = p * q
phin = (p - 1) * (q - 1)
e = 10
m = int.from_bytes(b'flag{falg_or_f14g}', 'big')
c = pow(m, e, n)
print('N='+hex(n))
print('e='+hex(e))
print('c='+hex(c))
# N=0x6930226480915caa2bb96907be66543b5884b36ae84d5edc2b67c8395628aeede638f47dbfe59ce653a2f6ae673a78d9b1faa83f97f428cabf9f71797c33cd941f93a86a43d285ceb70fc585c25024c57678cdff6e76d9ce6b1570b44fe7a21dd802996f60259f39b8cc5ef17647a937f3272cb105f9522b43ef3e6a95aaf1b22e3ce5738d8c5b53b838036576a9ea0cd4e7312adf4c889a2d873dc7e2ccf70fb0647cf1fdbead98f59bdc00e3e080c17742dd34e5b5dd112d813815fbec45a89b4cad393a17ec19a9e1be6be8a7df8e96e577792e72d93d2fe0c32e308a426f0aa2728e78e46c555114d12f161bae0a1b79c72a8e99b066a00d
# e=0xa
# c=0x6e33c752ca1a0f08da9475284f5875770dac999f16f3256656dc1e6e1f7b96fba0cce79ee69f58b695e75a594c763adf25e27eebb854a8987edfb696feb0bad47489debfec9d1ee5af5c70868509a0a39bc5d550a66a60afd9b516a0c6c16aa881c316cc085a23204c2e53af1a06fa376cd09a584f3c121cc3789921f0ecef9d18f7274e1e17c1f0e8ee9a96bb812b2870c63b59d704b7a0f81701a461680a61ded0a7fb4420651eee9ea5c5b8aea67829861bc62f7dee038e98862e470f6ddbc364543fb5e28839368397fc5fc0cda389377afdc6ce5beb2d7fd4205b16628b2c7b8c07ddf9c16cff011633839473b1f7b37bb9229ff59a9