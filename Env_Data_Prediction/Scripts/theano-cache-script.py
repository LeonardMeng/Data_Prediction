#!D:/Users/MengLingjun/Anaconda3/envs/ECI_TAXFORECAST\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Theano==1.0.3+2.g3e47d39ac.dirty','console_scripts','theano-cache'
__requires__ = 'Theano==1.0.3+2.g3e47d39ac.dirty'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Theano==1.0.3+2.g3e47d39ac.dirty', 'console_scripts', 'theano-cache')()
    )
