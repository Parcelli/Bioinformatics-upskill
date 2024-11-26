#Tree Visualization using ggtree
What are phylogenetics trees and what are they used for?

## ggtree Package

ggtree is an R package available on Bioconductor for visualizing and annotating phylogenetics tree.
First you'll need to install it if you dont have it already in your R environment.

```
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("ggtree")

```
### Load your library

