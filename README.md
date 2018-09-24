# HDT poly-logarithmic fully-dynamic connectivity algorithm

Implementation of the dynamic graph data structure described by Holm,
de Lichtenberg and Thorup in 2001 (HDT algorithm).

The graph is represented as an ensemble of spanning forests where each spanning
tree is stored as a balanced binary Euler tour tree. This enables connectivity
queries in O(log n) as well as insertions and deletions in poly-logarithmic
time.

References:
* Jacob Holm, Kristian de Lichtenberg, and Mikkel Thorup. 
  Poly-logarithmic deterministic fully-dynamic algorithms for 
  connectivity, minimum spanning tree, 2-edge, and biconnectivity. 
  J. ACM, 48(4):723–760, July 2001.
* Monika Rauch Henzinger, Valerie King. Randomized fully dynamic graph 
  algorithms with polylogarithmic time per operation. J. ACM 46(4) 
  July 1999. 502–536.
