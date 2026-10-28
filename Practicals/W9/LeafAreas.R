library(EBImage)
source("leafarea/getArea.R")

file_list <- list.files(path = "leafarea/", pattern = "\\.JPG$")
print(file_list)

results <- data.frame(Time = character(),
                      ID = character(), 
                      Area = numeric())

for (file in file_list) {
 area <- getArea(paste0("leafarea/", file))
 name <- strsplit(file, "[_.]")[[1]]
 time <- name[1]
 id <- name[2]
 results <- rbind(results, data.frame(Time = time, ID = id, Area = area))
}

View(results)

t1_area <- results$Area[results$Time == "t1"]
t2_area <- results$Area[results$Time == "t2"]

area_change <- t2_area - t1_area
mean(area_change)

results$Change <- NA
results$Change[results$Time == "t2"] <- area_change

View(results)

write.table(results, file = "Results.csv", sep = ",", row.names = F )
