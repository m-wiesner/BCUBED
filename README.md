# B3
-------------------------------------------------------------------------------- 
 This function determines the extrinsic clustering quality b-cubed measure 
 using a set of known labels for a data set, and cluster assignmnets of 
 each data point stored as either vector or cell arrays where each
 cell/row represets a data point in which an array containing class or cluster
 assignments is stored. The multi-class variant (.m) should not yet be used and 
 does not scale well. The single-class variant is on the order of 10-1000 times
 faster than the other bcubed scoring available on pip, depending on the
 dataset, but the multiclass variant has not been implemented in python as it
 suffers from the same slow performace as bcubed.

 Python and (matlab coming) implementations are provided.

## Installation
  Clone or download the repo. (I have to update the pip package)

## Inputs
--------------------------------------------------------------------------------
       L: An NxM matrix containing class labels for each data point (for the
          multiclass case, once implemented). Each row represents the ith data
          point and each column contains a 0, or 1 in the jth column indicating
          membership of label j. Alternatively, if hard class labels are
          available, L can be input as an Nx1 vector where each entry is its
          class label.

       K: Defined identically to L except for this variable stores cluster
          assignments for each data point

## Outputs
--------------------------------------------------------------------------------
      Fmeasure: This F-measure using the b-cubed metric
      precision: The b-cubed precision
      recall: The b-cubed recall

--------------------------------------------------------------------------------
## Performace demonstration
--------------------------------------------------------------------------------
        ./compare\_performance.sh
        Timing shared setup time for 5 random cases using the bcubed package
        real    0m1.351s
        user    0m0.248s
        sys    0m0.071s
  
        Timing full execution time (b3 + shared) for the B3score implementation
        real    0m0.283s
        user    0m0.240s
        sys    0m0.045s
  
        Timing full execution time (bcubed + shared) for the bcubed implementation
        real    0m38.233s
        user    0m36.174s
        sys    0m0.273s
--------------------------------------------------------------------------------
      Author: Matthew Wiesner
      Email : wiesner@jhu.edu 
      Institute: Johns Hopkins University Electrical and Computer Engineering

      Refences: 
           DESCRIPTION OF THE UPENN CAMP SYSTEM AS USED FOR COREFERENCE,
           Breck Baldwin, Tom Morton, Amit Bagga, Jason Baldridge, 
           Raman Chandraseker, Alexis Dimitriadis, Kieran Snyder, 
           Magdalena Wolska, Institute for Research in Cognitive Science

           A.A. Aroch-Villarruel Pattern Recognition 6th Mexican Conference,
           MCPR 2014 Proceedings Paper, p.115
