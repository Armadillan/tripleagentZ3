# tripleagentZ3

This project aims to use the Z3 theorem prover to find optimal strategies for the social deduction game Triple Agent by Tasty Rook.

All documentation assumes familiarity with the game.

The goal is to extract all the logic from the game, and operate only on what is known to be true, with minimal assumptions. Some assumptions are required to play the game effectively, but these are not used by default, and must be explicitly applied on each operation.

## Goals
- [X] 1. Implement logic from all operations in base game, except Hidden Agenda, given each assumption. Continuously update this as more assumptions are added.
- [ ] 2. Implement ServiceAgent class providing information on possible virus/service configurations after each piece of info it is given.
- [ ] 3. Create interactive app providing real time-information as a game progresses, usable during (service) gameplay.
- [ ] 4. Write documentation on basic functionality of package and interactive app.
- [ ] 5. Add vote suggestion functionality to ServiceAgent.
- [ ] 6. Add victim suggestion functionality to ServiceAgent.
- [ ] 7. Create VirusAgent, which finds optimal strategy for virus players.
- [ ] 8. Create autonomous bot capable of playing the game, and corresponding documentation.
- [ ] 9. Allow the interactive tool and bot to use multiple Agents to dynamically tweak assumptions, to always assume as little as possible. 
- [ ] 10. Implement Hidden Agenda
- [ ] 11. Implement more roles/factions and operations.

## Terms
Terms from the game, such as operation, generally hold the same meaning here. There are some exceptions (like agent), and some new terms (like call).

**Call:** A, not necessarily true, statement made by a player, including information they claim to have and the operation they gained that information from.

__Agent:__ A class within this software, instances of which operate a single Z3 Solver. Agents receive calls and assumptions and play operations, and make decisions based on this information.

__Vote call:__ A, not necessarily true, statement made by a player, stating how they will be voting and urgining others to vote alike.

__Base game:__ The free version of Triple Agent.

__Victim__: A player in any way involved in an operation other than the currently active player.

## TODO/IDEAS/NOTES
* Preset number of agents:
    * One (helper or service player)
    * One Z3 + one for each player
    * When Z3 plays virus it can run an agent to simulate knowledge other players have
    * Also allow custom number of custom agents irrespective of number of players
* To run multiple models, for example for Z3 knowledge and player knowledge, or with different assumptions, use multiple Agents
* Allow other players to retract calls
    * Live tool able to retract calls/suggests retracting call
    * Each call can have a corresponding bool that implies it and is assumed to be True, and is set to False if call is retracted
        * Alternatively, start a new solver with all the current calls (solver.assertions()), minus the retracted ones
* Incorporate extra roles (triple agent, suspicious service etc)
* Incorporate Hidden Agenda
* Create "live" tool, usable during gameplay
    * Prompt for new info
    * Give updated variants after each new piece of information
         * Alert when at least one virus is identified
         * Calculate percent chance that each player is virus?
    * Suggest which players to pick for secret intel, confession etc
         * Calculate bits of information aquired from each option
* Create bot
