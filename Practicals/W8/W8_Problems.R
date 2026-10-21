#Disease Risk
#1
Euro_geno <- read.table("H938_Euro_chr6.geno", sep = " ", h=T)
str(Euro_geno)

maxsum <- Euro_geno$nA1A1 + Euro_geno$nA1A2 + Euro_geno$nA2A2
max(maxsum)

#2
max(rowSums(Euro_geno[, 5:7], na.rm = T))

#3
SNP_risk <- read.table("SNP_risks.csv", sep = ",", h=T)

Euro_geno_risk <- cbind(Euro_geno, SNP_risk[3])
str(Euro_geno_risk)

#4
mean(Euro_geno_risk$nA1A2[Euro_geno_risk$Risk == "Risk"])
mean(Euro_geno_risk$nA1A2[Euro_geno_risk$Risk == "Non-Risk"])

#Data Cleanup
#1
Smith_Data <- read.table("Smith2003_data.txt", sep = "\t", h=F)
str(Smith_Data)
View(Smith_Data)
length(Smith_Data$V6)

#2
Smith_Data$V7 <- gsub("-999", "NA", Smith_Data$V7)
Smith_Data$V8 <- gsub("-999", "NA", Smith_Data$V8)
write.table(Smith_Data, file="Smith2003_data_clean.tsv", sep="\t", row.names=F)
View(Smith_Data)
