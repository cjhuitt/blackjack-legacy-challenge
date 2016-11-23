# Blackjack Refactoring Challenge #

**_IN PROGRESS.  The code is already terrible, but it's not complete._**

You've been hired by an online casino to maintain their blackjack program.
Apparently, the previous developers all quit.  Good luck.

Your first day, you are given commit access and the following priority-sorted
list of feature requests:

- Support multiple players on the same server.  Each player sees an independent
  game state (deck contents and order, dealer cards, etc) and is unaffected by
  the presence and actions of other players.
- Allow player to split
- Support for up to 8 decks (specific value configurable per table)
- Allow player to buy insurance
- Allow player to surrender (configurable per server)
- Place each player at a "table" with up to 4 other players.  Players at the
  same table have a shared game state (deck contents and order, dealer cards,
  etc) and can see each other's progress.
- Dealer hits on soft 17 (configurable per table)

You are also told to fix any bugs if they represent a substantial risk to your
employer's profits.  Anything that enables cheating or irritates the gaming
commision falls into this category.  Such bugs take top priority.  Any other
bugs are lowest priority, so you can work on them if you manage to fix all
high-priority bugs _and_ implement all the feature requests.

One more thing: The protocol used to communicate between the client and the
server must remain backwards-compatible.  It should be possible to connect any
version of the client to any version of the server and use the features that
are present in both.
