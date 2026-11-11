par(mfrow=c(6,5), mar = c(1, 2, .5, .5))
pch <- 0:25

for(pch_symbol in pch){
  plot(1, 1, pch = pch_symbol, cex = 2.5, xaxt = "n", yaxt = "n",
       ann = FALSE, bty = "n")
  mtext(pch_symbol, side = 2, line = 0.5, las = 1)
}

