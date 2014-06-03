import random
import sys

import numpy
import matplotlib
# Don't display figures, render them as png
matplotlib.use('Agg')

from matplotlib import pyplot

ERROR_ARGUMENT = 10

def poisson(lam, n):
    """ Returns an array with the observed number of decays during one second. The mean number of decays (lambda) for our sample should be "lam". There should be "n" measurements. These should be integers since we are actually counting them (well, virtually). """
    return numpy.random.poisson(lam, n)

def print_poisson(lam, n):
    """ Return a string with "n" results from a poisson distribution in the format:
    1,22
    2,17
    3,20
    <id>,<measurement>
    ...
    n,p_n
    """
    # Start with a new string
    out = ""
    for i, value in enumerate(poisson(lam,n)):
        # for each result, append it to the result
        out += str(i+1)+","+str(value) + "\n"
    return out

def hist(filename, bins):
    """ Load a csv file and return a histogram using pyplot.hist. "bins" specifies the number of bins. """
    # load the data
    data = numpy.loadtxt(filename, delimiter=",")
    # Get the second column, we don't care about the measurement id.
    values = data[:, 1]
    return pyplot.hist(values)

def usage(error=0):
    print >>sys.stderr, "python", sys.argv[0], """{generate,plot} <args>

    python {arg} generate <lamda> <samples>
    python {arg} plot <datafile> <bins>
"""
    sys.exit(error)

# This only runs if we call the script from the command line (not if we import the module).
if __name__ == "__main__":
    # sys.argv are the arguments passed to the command line including
    # the name of the script.
    # python geiger_counter.py a 1 hello => 
    #        sys.argv = ["geiger_counter.py", "a", "1", "hello"]
    if len(sys.argv) != 4:
        usage()

    command = sys.argv[1]

    if command == "generate":
        lam, n = int(sys.argv[2]), int(sys.argv[3])
        print print_poisson(lam, n),

    elif command == "plot":
        datafile, bins = sys.argv[2:]
        assert datafile.endswith(".csv"), "Please give me a csv file."
        bins = int(bins)
        pyplot.figure()
        hist_values = hist(datafile, bins)

        # save it to a png in the graph folder
        image_file = datafile[:-4].replace("data/", "graphs/")
        pyplot.savefig(image_file)

    # Wrong arguments
    else:
        usage(ERROR_ARGUMENT)

