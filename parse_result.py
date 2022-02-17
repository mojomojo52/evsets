import sys
import argparse
import re

# TODO: create histogram

DEBUG = False
do_hist = False
stats = True


def parse(input_file):

    with open(input_file,'r') as reader:
        line_num = 1
        num_err = 0
        try:
            for line in reader:
                if bool(re.search("Error: exceeded max repetitions", line)):
                    #print(line)
                    num_err += 1
                if bool(re.search("Total execution time", line)):
                    idx = line.index("time")+6
                    print(line[idx:idx+7])
                line_num += 1
        except:
            print("Err @", line_num)
            print(line)

        print(num_err, "num err")


def main(argv):
    global do_hist
    global stats

    parser = argparse.ArgumentParser(description="Parses output data from tresspass")

    parser.add_argument('INPUT_FILE_LIST', nargs='+', help="Name of the file to parse")

    args = parser.parse_args()

    inputs = args.INPUT_FILE_LIST


    for input in inputs:
        parse(input)


if __name__ == "__main__":
    main(sys.argv)
