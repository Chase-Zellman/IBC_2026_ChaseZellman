MatrixStats <- data.frame()

for(i in 1:59){
  File <- paste0("n",i,".txt")
  Current_File <- as.matrix(read.table(paste0("Saavedra2013/", File), header = F))
  Current_Nrow <- nrow(Current_File)
  Current_Ncol <- ncol(Current_File)
  Current_p_1 <- sum(Current_File == 1) / length(Current_File)
  Current_p_0 <- sum(Current_File == 0) / length(Current_File)
  append <- data.frame(File = File,
                       Nrow = Current_Nrow,
                       Ncol = Current_Ncol,
                       p_1 = Current_p_1,
                       p_0 = Current_p_0)
  MatrixStats <- rbind(MatrixStats, append)
}

write.table(MatrixStats, file = "MatrixStats.tsv", sep = "\t", row.names = F )


