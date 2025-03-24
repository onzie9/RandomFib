# RandomFib

I learned about Viswanath's number from a recreational math book called Mathematical Mysteries by Calvin Clawson. I used my Ti-83 calculator to write a basic script that varied the fairness of the coin toss, and then plotted the results. The Viswanath-type numbers formed a curve that looked like a parabola.  

Over the years, I have kept this problem in my head and occasionally skimmed a paper or two about it.  In this code, I decided to do some long simulations and then check on some regressions to see if the resulting "parabola" was actually parabolic.  It wasn't.  I also tried to fit an arcsine distribution curve since the underlying process is sort of like a random walk, but that wasn't accurate, either.  I tried a catenary for the fun of it, and a degree 4 polynomial. 

I want to take a closer look at Makover and McGowan's 2005 paper and see if I can add an unfair probability into their inequalities to get an upper and lower bounding function in p.  That would be a nice result, but since the paper is 20 years old, maybe someone already did it.  
