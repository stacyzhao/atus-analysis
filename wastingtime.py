import pandas as pd

def read_csv():
    atusact = pd.read_csv('data/atusact_2014.dat')
    atuscps = pd.read_csv('data/atuscps_2014.dat')
    atusresp = pd.read_csv('data/atusresp_2014.dat')
    atusrost = pd.read_csv('data/atusrost_2014.dat')
    atusrostec = pd.read_csv('data/atusrostec_2014.dat')
    atussum = pd.read_csv('data/atussum_2014.dat')
    atuswho = pd.read_csv('data/atuswho_2014.dat')
    return atusact, atuscps, atusresp, atusrost, atusrostec, atussum, atuswho
