 # B3
 ===============================================================================
 This function determines the extrinsic clustering quality b-cubed measure 
 using a set of known labels for a data set, and cluster assignmnets of 
 each data point stored as either vector or cell arrays where each
 cell/row represets a data point in which an array containing class or cluster
 assignments is stored. The multi-class variant should not yet be used and 
 does not scale well.

 Inputs
 -------------------------------------------------------------------------------
       L: An NxM matrix containing class labels for each data point. Each 
          row represents the ith data point and each column contains a 0, or 1
          in the jth column indicating membership of label j.
          Alternatively, if hard class labels are available, L can be input 
          as an Nx1 vector where each entry is its class label

       K: Defined identically to L except for this variable stores cluster
          assignments for each data point

 Outputs
--------------------------------------------------------------------------------
 Fmeasure: This F-measure using the b-cubed metric
 precision: The b-cubed precision
 recall: The b-cubed recall

--------------------------------------------------------------------------------
 Author: Matthew Wiesner
 Email : wiesner@jhu.edu 
 Institute: Johns Hopkins University Electrical and Computer Engineering

 Refences: DESCRIPTION OF THE UPENN CAMP SYSTEM AS USED FOR COREFERENCE,
           Breck Baldwin, Tom Morton, Amit Bagga, Jason Baldridge, 
           Raman Chandraseker, Alexis Dimitriadis, Kieran Snyder, 
           Magdalena Wolska, Institute for Research in Cognitive Science

           A.A. Aroch-Villarruel Pattern Recognition 6th Mexican Conference,
           MCPR 2014 Proceedings Paper, p.115
 ----------------------------------------------
