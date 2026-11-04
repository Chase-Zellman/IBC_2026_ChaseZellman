#1
Toads <- read.table("Toad_Handedness.tsv", header = T)
Toad_Trials <- Toads$N_trials
Toad_Rights <- Toads$N_rights


Toad_odds <- c()
for(i in 1:nrow(Toads)){
  Toad_odds[i] <- Toad_Rights[i]/Toad_Trials[i]
}

toad_right <- c()
p_value<- c()
nexp <- 10000

for(i in 1:nrow(Toads)){
  num_trial <- Toad_Trials[i]
  toad_right <- c()
  for(j in 1:nexp){
    exp <-sample(c("R","L"), size = num_trial, prob = c(0.5,0.5), replace = T)
    right <- sum(exp =="R")
    toad_right[j] <- right
  }
  exp_odds <- toad_right/num_trial
  toad_diff <- abs(Toad_odds[i] - 0.5)
  exp_diff <- abs(exp_odds - 0.5)
  p_value[i] <- sum(exp_diff >= toad_diff)/nexp
}

handed <- c()

for(i in 1:nrow(Toads)){
  if(p_value[i] >= 0.05){
    handed[i] <- "no handedness"
  } else if(Toad_odds[i] > 0.5){
    handed[i] <- "right handedness"
  } else {
    handed[i] <- "left handedness"
  }
}

Toads$P <- p_value
Toads$Handed <- handed
View(Toads)

#2
right_results <- sum(Toads$Handed == "right handedness")
left_results <- sum(Toads$Handed == "left handedness")

if(right_results == left_results){
  print("Equal likely for handedness")
} else {
  print("Not equaly likely for handedness")
}

#3
Toad_right_handed <- Toads$Handed == "right handedness"
Male_right <- mean(Toad_right_handed[Toads$Sex == "M"])
Female_right <- mean(Toad_right_handed[Toads$Sex == "F"]) 
real_diff <- Male_right - Female_right

shuffled <- c()
for(i in 1:nexp){
  Shuffled_frog <- sample(Toads$Sex)
  Shuffled_Male <- mean(Toad_right_handed[Shuffled_frog == "M"])
  Shuffled_Female <- mean(Toad_right_handed[Shuffled_frog == "F"])
  shuffled_diff <- Shuffled_Male - Shuffled_Female
}
Shuffled_p <- sum(abs(shuffled_diff) >= abs(real_diff/nexp))
print(Shuffled_p)

