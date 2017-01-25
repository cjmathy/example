# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
import time
import matplotlib.pyplot as plt
from .algs import quicksort, bubblesort


def run_stuff():
    """
    This function is called in `__main__.py`
    """
    bs_avg_times = np.empty(10)
    qs_avg_times = np.empty(10)
    n = np.linspace(100,1000,10)

    for i in n:
    	i = int(i)
    	#first, make 100 arrays of length i to be sorted, and store them in separate dictionaries
    	bs_arrays = {}
    	qs_arrays = {}
    	for j in range(100):
    		array = np.random.rand(i)
    		bs_arrays[j] = array
    		qs_arrays[j] = np.copy(array)

    	#measure how long it takes to sort all 100 arrays with bubblesort, then compute an average time and store that value for plotting
    	t0 = time.time()
    	for array in bs_arrays: bubblesort(bs_arrays[array])
    	bs_avg_times[i/100-1] = float(time.time() - t0)/100.0
    	
    	#measure how long it takes to sort all 100 arrays with quicksort, then compute an average time and store that value for plotting	
    	t0 = time.time()
    	for array in qs_arrays: quicksort(qs_arrays[array])
    	qs_avg_times[i/100-1] = float(time.time() - t0)/100.0

    #plot runtimes of both sorting algorithms to compare
    fig = plt.figure()
    plt.plot(n,bs_avg_times)
    plt.plot(n,qs_avg_times)
    plt.title('Quicksort vs. Bubblesort')
    plt.ylabel('Average time to sort vector')
    plt.xlabel('Number of elements in vector')
    plt.legend(['Bubblesort','Quicksort'])
    fig.savefig('bs_vs_qs')

    return