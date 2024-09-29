# Design Online Blackjack Game

### Game Details:
- Blackjack is a game where several players play against dealer
- Goal of this game is to get closer to 21 than the dealer without exceeding the 21 points .
- This Game is played with deck of cards
- Where the value of an ace card can be 1 or 11 points .
- While cards of 10 , jack , queen and king value 10 points .
- Whereas , cards 2-9 have the same values as the number written on them
- Hence the player having one ace card and a face card (king,queen or jack card) or a 10 card has 21 Points . this is called blackjack

### Requirements:
- How many players can play blackjack ? -> (1,7)
- Is there any limit of cards , a player can have . (no limit)
- Can players play again each other ? -> no
- Upto how many points can the player or the dealer hit the card? -> till 21 points

### Class Diagram [10 mins ]
#### Find Nouns or Components
- Game
- Dealer 
- Player
- Card


### Design Patterns involved ?
- Singleton ( for creating game class)
- Strategies ( for dealer playing level )

