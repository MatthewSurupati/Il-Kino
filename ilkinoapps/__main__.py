import argparse
from ilkinoapps.ilkino import *
# from ilkinoapps.rev_ilkino import *

if __name__ == '__main__':
    ilkino = IlKino(RealGenerator.generate(), RealPrinter())
    # import_cmd = argparse.ArgumentParser()
    # import_cmd.add_argument('gift_')
    # args = import_cmd.parse_args()
    # gift_list = args.gift_.split(',')
    # ilkino.setup(gift_list)
    ilkino.setup('teddy bear')
    ilkino.run()