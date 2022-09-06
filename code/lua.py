import sys

if __name__ == '__main__':

    if "-h" in sys.argv[1]: 
        print("fill in info about help here")
        exit() 

    if "-e" in sys.argv: 
        pos = sys.argv.indexOf("-e")
        val = sys.argv[pos + 1]

        # run all tests 
        if val == "ALL": 
            print('run tests')
        elif val == "task": 
            print("run these tasks")