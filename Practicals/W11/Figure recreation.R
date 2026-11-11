library(ape)

Copy_Tree <- read.tree(text = "(Struthioniformes,
                       ((Anseriformes,Galliformes),
                       (((Pheonicopteriformes, Columbiformes),
                       (Gruiformes, Apodiformes)),
                       (((Sphenisciformes, Procellariiformes),
                       (Cinconiformes, Pelecaniformes)),
                       ((Strigiformes,
                       (Trogoniformes,
                       (Piciformes, Coraciiformes))),
                       (Psittaciformes, Passeriformes))))));")

edge_colors <- rep("blue", nrow(Copy_Tree$edge))

purples <- c("Struthioniformes", "Cinconiformes", "Trogoniformes",
            "Psittaciformes", "Passeriformes")

for(name in purples){
  edge_colors[which.edge(Copy_Tree, name)] <- "purple"
}

plot(Copy_Tree, cex = .75, edge.color = edge_colors, edge.width = 4,
     font = 2)
