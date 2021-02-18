# Conditional Median Inference

Consider the problem of constructing a confidence interval for the median of a real-valued response Y conditional on features X = x in a situation where we are not willing to make any assumptions on the underlying distribution of the data (X, Y). This package contains a Python implementation of an algorithm based upon ideas from conformal prediction that guarantees coverage of the conditional median at any given level, as well as code for testing the performance of this algorithm on different distributions and with different conformity scores.

This package is intended as a supplement to [1]. It provides an implementation for Algorithm 2 and tests its performance on Distributions 1, 2, and 3 using Conformity Scores 1, 2, 3, and 4. It also provides a script to generate any remaining figures seen in [1].

[1] Dhruv Medarametla and Emmanuel Candès, "Distribution-Free Conditional Median Inference." 2021.


## Getting Started

This package is self-contained and implemented in Python.

### Prerequisites
- python
- numpy
- matplotlib
- scipy
- datetime
- sklearn
- pickle
- tqdm
- scikit-learn
- scikit-garden
