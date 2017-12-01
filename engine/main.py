import sys
import getopt


class Engine(object):
    @staticmethod
    def main(argv):
        try:
            opts, args = getopt.getopt(argv, "hb:w:", ["help", "black", "white"])
        except getopt.GetoptError:
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print("main.py -h")
                sys.exit()
            elif opt in ("-b", "--black"):
                print("main.py -b")
                sys.exit()
            elif opt in ("-w", "--white"):
                print("main.py -w")
                sys.exit()


if __name__ == "__main__":
    Engine.main(sys.argv[1:])
