#Tree visualization using ggtree
#Load required library
library(tidyverse)
library(ggtree)
library(treeio)


# Read in your tree file (data with 13 tips)

tree <- read.tree("./tree_newick.nwk")
tree

#Basic tree visualization
ggtree(tree)

#The horizontal dimension shows the amount of genetic change, 
#and branches represent evolutionary lineages changing over time.
#The scale will show you the amount of change.


#Add a scale
ggtree(tree)+ theme_tree2()

#By default a phylogram is created. Incase you want a cladogram instead

ggtree(tree,branch.length = "none")

#Add node points,tip points and tip labels
ggtree(tree)+
  geom_nodepoint()+
  theme_tree2()


# add tip points and labels
ggtree(tree)+
  geom_nodepoint()+
  geom_tippoint() +
  geom_tiplab()+
  theme_tree2()

# Make the tree fancy



#Tree annotation
#What is tree annotation?
#Process of adding additional information or metadata to a phylogenetic tree.


#Internal node number
#To get the internal node number, user can use geom_text
#hjust option ensures the labels aren’t sitting right on top of the nodes

ggtree(tree) + geom_text(aes(label=node),hjust=-.3)

#Labelling clades

ggtree(tree) + 
  geom_tiplab() + 
  geom_cladelabel(node=17, label="Some random clade", 
                  color="red2",offset = 0.8)

#Highlight a clade

ggtree(tree) + 
  geom_tiplab() + 
  geom_hilight(node=17, fill="gold") + 
  geom_hilight(node=21, fill="purple")


#Advanced tree annotation/visualization
#We will use data from a paper :https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4178866/
#76 H3 hemagglutinin gene sequences of a lineage: swine and human influenza A viruses
#Data : https://4va.github.io/biodatasci/data.html

#Reading your tree

tree <- read.beast("./flu_tree_beast.tree")


# supply a most recent sampling date so you get the dates

ggtree(tree, mrsd="2013-01-01") + 
  theme_tree2() 

# Finally, add tip labels and adjust axis
ggtree(tree, mrsd="2013-01-01") + 
  theme_tree2() + 
  geom_tiplab(align=TRUE, linesize=.7) +
  xlim(1990, 2020)

