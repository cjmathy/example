import numpy as np
from example import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():

    # Check odd length vector
    x = np.array([1,2,4,0,1])
    assert np.array_equal(algs.bubblesort(x), np.array([0,1,1,2,4]))

    # Check even length vector
    x = np.array([1,2,4,0])
    assert np.array_equal(algs.bubblesort(x), np.array([0,1,2,4]))

    # Check empty vector
    x = np.array([])
    assert np.array_equal(algs.bubblesort(x), np.array([]))

    # Check single element vector
    x = np.array([1])
    assert np.array_equal(algs.bubblesort(x), np.array([1]))

    # Check duplicated elements vector
    x = np.array([1,1,2,4,5,1])
    assert np.array_equal(algs.bubblesort(x), np.array([1,1,1,2,4,5]))

    # Check char vector
    x = np.array(['a','b','d','c'])
    assert np.array_equal(algs.bubblesort(x), np.array(['a','b','c','d']))


def test_quicksort():

    # Check odd length vector
    x = np.array([1,2,4,0,1])
    assert np.array_equal(algs.quicksort(x), np.array([0,1,1,2,4]))

    # Check even length vector
    x = np.array([1,2,4,0])
    assert np.array_equal(algs.quicksort(x), np.array([0,1,2,4]))

    # Check empty vector
    x = np.array([])
    assert np.array_equal(algs.quicksort(x), np.array([]))

    # Check single element vector
    x = np.array([1])
    assert np.array_equal(algs.bubblesort(x), np.array([1]))

    # Check duplicated elements vector
    x = np.array([1,1,2,4,5,1])
    assert np.array_equal(algs.quicksort(x), np.array([1,1,1,2,4,5]))

    # Check char vector
    x = np.array(['a','b','d','c'])
    assert np.array_equal(algs.quicksort(x), np.array(['a','b','c','d']))
