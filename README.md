# Ceelo-Game-In-Python

"Cee-lo" is a game of chance played with three dice. It gets its name from the Chinese phrase "四五六" meaning 4-5-6. The game is played with two or more players, each starting with the same number of coins. In each round, one player acts as the banker and the others bet against the banker. The banker has a slight advantage in winning bets. The role of the banker rotates among players throughout the game.

At the beginning of each round, the banker places an amount B in the center. Starting with the player next to the banker, each player takes turns betting an amount, which cannot exceed B minus the total amount bet by previous players. If the total bet amount does not cover B, the remaining amount is returned to the banker.

After all bets are placed, the banker rolls the dice. There are four possible outcomes: automatic win, automatic loss, scoring, or re-rolling. An automatic win occurs when the banker rolls 4-5-6, triples, or two identical numbers with a 6. An automatic loss happens when the banker rolls 1-2-3 or a pair of identical numbers (other than 1) and a 1. Scoring occurs when the banker rolls a pair of matching numbers and a third number (2, 3, 4, or 5). The third number becomes the banker's score. If none of these combinations occur, the banker re-rolls the dice until an automatic win, automatic loss, or score is achieved.

If the banker has a score, players take turns rolling the dice to settle individual bets. A player wins if they roll 4-5-6, triples, or a higher score than the banker. A player loses if they roll 1-2-3 or a lower score than the banker. Ties result in no player winning. If a roll does not result in a win, loss, or score, the player re-rolls the dice.

At the end of the round, if the banker loses all bets with the players, they lose the bank. The next player becomes the banker. The banker retains the bank if they achieve an automatic win, do not lose all bets, and are not beaten by a player with 4-5-6 or triples. The game ends when a player loses all their coins. The player with the highest number of coins is declared the winner.

The objective is to write a Python program that simulates the game. It should prompt the user for the number of players (2-6) and the number of coins (5-100) each player has at the start.
