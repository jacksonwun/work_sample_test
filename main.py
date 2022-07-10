import argparse
from transform import Dataitem

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_1", type=str,
                        help="Input a csv file here")
    parser.add_argument("input_2", type=str,
                        help="Input another csv file here")
    parser.add_argument('-o', '--output', dest='target', action='store',
                        help='transform from csv to json file')
    args = vars(parser.parse_args())

    if 'target' in args:
        print('Excuting ...')
        dataitem = Dataitem(args['input_1'], args['input_2'], args['target'])
        dataitem.run()
        print('Transform Success!')