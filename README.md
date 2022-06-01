# wordle_statistics
This is part of a project that me and two of my peers completed for a class at school. The class was Data Science II, and we were tasked with choosing a data set to analyze. We were very interested in the NYT game Wordle at the time, so we decided to use Wordle data for our project. The issue was - not all of the data we needed/wanted was publicly available. So, myself and one of my teammates decided to recreate wordle in a python command line interface. I did the majority of the physical coding, and my teammate (Rachel Foye) helped with the processes and overall methods to make it work. We then needed to test our application in two different fashions. We used a supervised learning model and unsupervised learning model to achieve this. Our supervised learning model was based on the list of possible wordle solutions (publically available online). We considered the list of solutions and found the most likely letters to appear and the most likely starting letters. That code is model1.py in the repository. Our second model was unsupervised. We recruited friends and classmates to play wordle using our app, and we saved their data per round (words guessed, number of guesses to solve, etc.) but did not save the actual solution. This way, our model was unsupervised because it had no knowledge of the possible solutions - it just knew what letters and words were effective at statistically limiting the number of guesses to solve. I then developed a bot to "play" wordle using both models lists of words, and the average number of guessses to sovle per round using each list was how we determined which model was the best model to predict the optimal words to guess. Less is better. We certainly could have improved run time in the models' methods and testing method, but we were very restricted with time for the deadline of the project so going back to perfect something that didn't change our results was not feasible. We did discuss ways to do this amongst ourselves, but the actual implementation we simply did not have time to complete before we had to present our findings.  
