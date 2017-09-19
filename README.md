# optics
OPTICS clustering algorithm

This is an implementation of the OPTICS algorithm as described in
OPTICS: Ordering Points To Identify the Clustering Structure (1999) by Mihael Ankerst , Markus M. Breunig , Hans-peter Kriegel , Jörg Sander
(http://www.dbs.informatik.uni-muenchen.de/Publikationen/Papers/OPTICS.pdf)

OPTICS algorithm does not split points into clusters but arranges them in so-called cluster ordering, from which actual clusters can be deduced.

Cluster ordering stores information about clustering results for all eps` <= eps, where eps` is used for computing actual clustering result, eps has been used by optics for building the cluster ordering.

For clusters derivation, an algorithm that is also proposed by the article has been used. It is called ExtractDBSCAN-Clustering in the article and is aimed to extract clustering results from the cluster ordering as if the clustering has been made with DBSCAN algorithm with the given eps` <= eps.

A special thanks should be given to pyclustering (https://github.com/annoviko/pyclustering) project since pyclustering OPTICS implementation has been used to generate results for testing the current algorithm.
