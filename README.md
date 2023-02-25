# 1.Game description:
- Kalah is a board game that requires two players to start the game.
- Initial state of the game: There will be 6 holes on your side and 6 holes on your opponent’s side, each hole with value 6, there will be 2 kalahs between you and your opponent’s holes, the left kalah is your opponent’s kalah and the right one is yours.
- You can pick a non-zero hole on your turn, take the value on the hole as S, set the value of this hole to 0, then start from the next hole(both players’) or kalah(only your), we will move S steps counter-clockwise, every kalah and holes that we’ve been through will increase by one. If your last step is on your own kalah, you can move again, if your last step filled a hole on your side that is originally empty, then you can take your opponent’s corresponding hole value and your last step 1 value to your kalah.
- If one player’s kalah has score more than 36, the player wins. If one side of holes are all empty, the opponent can collect values in every hole to their kalah. If both player has 36 on their kalah, then this is a draw.
# 2.Heuristic function choice:
- My Heuristic function: 18 * (a_fin - b_fin) + all(a) - all(b).
- We use the Heuristic function to evaluate the current state of the game board and return a number, if the number is greater, it means that the situation is better for AI, if the number is smaller, it means that the situation is worse for AI.
## Why this Heuristic function:
- 1.Kalah score is the most important factor in the game, so I first choose a_fin - b_fin (the difference of two kalah), if AI has a higher score on kalah, then the score will be positive.
- 2.But when two player has the same or similar kalah score, it could be a hard decision for AI to make, so we will need some kind of factor to break tie. I choose difference of Sum(hole values) on each side. First of all, one of the way to end the game is that one side has all 0 hole and the opponent can collect all hole values, so the sum of hole values can be a win condition. Secondly, with a higher sum hole values, it means that we can do more operations, hence we can have a higher chance to move to kalah and move again, or go to an empty hole to steal values.
- 3.But when the game just started, kalah scores will be very small, so I pick a factor 18 to make the difference weights more, so that AI can mainly focus on evaluating kalah difference.

- Example: Suppose Ai is my opponent
3, 12, 12, 13, 0, 4
5						8
6,  5,  3, 2, 0, 0
In this case, the state after moving index 2 gives us 270 score, which is the state with highest heuristic value(the only step that gives us positive score) after evaluating every possible next step for AI. Moving index 2 can earn 3 points, and doing any other operation will earn only less point, from this example we can see that the heuristic function is doing a decent job!

# 3.Details of Program Design, Experiments and results
Program Design: I use the Minimax algorithm that allows the AI to explore possibilities in future 6 rounds, assuming that our opponent is doing its best decision(least Heuristic function value), and the AI will try to pick the best decision(max Heuristic function value). We also use Alpha-Beta Prunning to do some cutoff when we are doing recursive function, that greatly improve our algorithm’s runtime.

- My computer’s CPU: CPU @ 2.60GHz
Depth = 4: Longest step: 0.008s  |  Shortest step: 0.001s  
Depth = 6: Longest step: 0.52s  |  Shortest step: 0.03s  
Depth = 8: Longest step: 6.77s  |  Shortest step: 0.04s   

Heuristic function analysis: I will choose depth = 6 to run this comparison with random choice  
Random#1: 27 rounds, I beat AI  
Random#2: 23 rounds, I beat AI  
Random#3: 17 rounds, I beat AI  
Random#4: 22 rounds, I beat AI  
Random#5: 13 rounds, I beat AI  
Random#6: 15 rounds, I beat AI  
Random#7: 26 rounds, I beat AI  
Random#8: 19 rounds, I beat AI  
Random#9: 21 rounds, I beat AI  
Random#10: 18 rounds, I beat AI  

Heuristic#1: 23rounds, AI beats me  
Heuristic#2: 20rounds, I beat AI  
Heuristic#3: 23rounds, I beat AI  
Heuristic#4: 28rounds, AI beats me  
Heuristic#5: 26rounds, I beat AI  
Heuristic#6: 27rounds, AI beats me  
Heuristic#7: 21rounds, I beat AI  
Heuristic#8: 18rounds, I beat AI  
Heuristic#9: 29rounds, AI beats me  
Heuristic#10: 24rounds, I beat AI  

I am using my best knowledge to play agains AI, with my best game strategy. When facing random baseline AI, my win rate is 100%, there is one round that I only take 13 rounds to beat the AI. But when facing AI with smart decision with heuristic function, I have win rate at 60%, the fastest game takes 18 games. This comparision can see that the smart AI with Heuristic function has much better performace comparing to baseline random AI,
