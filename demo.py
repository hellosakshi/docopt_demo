# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: docopt.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [<arg123>]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[<arg123>]        Takes any value (this is a optional positional argument)  
"""

from docopt import docopt
opt = docopt(__doc__)  

def main(opt1, opt2, opt3, opt4):


    print(opt)
    print(type(opt)) 

if __name__ == "__main__":
    main(opt["<arg1>"], opt["--arg2"], opt["--arg3"], opt["<arg123>"])
