#1
library(readr)
Jiang2013_data <- read_delim("Jiang2013_data.csv", 
                             delim = "\t", escape_double = FALSE, 
                             trim_ws = TRUE)

Mating_Data <- Jiang2013_data

mean_r <- function(taxon){
  mean_value <- mean(Mating_Data$r[Mating_Data$Taxon == taxon])
  return(mean_value)
}

mean_r("Fish")

#2
Taxon_r <- Mating_Data$r
fish_mean <- mean_r("Fish")
cor_coef <- c()
num_random <- 50000
for(i in 1:num_random){
  exp <- sample(Taxon_r, size=37, replace = F)
  cor_coef[i] <- mean(exp)
}
fish_sample_p <- sum(cor_coef >= fish_mean)/num_random
print(fish_mean)
print(fish_sample_p)

#3
Taxons <- unique(Mating_Data$Taxon)
taxon_mean <- c()
taxon_p <- c()

for(i in 1:length(Taxons)){
  real_mean <- mean_r(Taxons[i])
  nexp <- sum(Mating_Data$Taxon == Taxons[i])
  cor_coef <- c()
  for(j in 1:num_random){
    taxon_exp <- sample(Taxon_r, size = nexp, replace = F)
    cor_coef[j] <- mean(taxon_exp)
  }
  taxon_mean[i] <- real_mean
  taxon_p[i] <- sum(cor_coef >= real_mean)/num_random
}
taxon_table <- data.frame(Taxon = Taxons, r = taxon_mean, p = taxon_p)
View(taxon_table)

