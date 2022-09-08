# tripleagentZ3

### TODO/IDEAS/NOTES
* To run multiple models, for example for Z3 knowledge and player knowledge, or with different assumptions, use multiple Agents
* Allow other players to retract calls
    * Live tool able to retract calls/suggests retracting call
        * Each call can have a corresponding bool that implies it and is assumed to be True, and is set to False if call is retracted
        * Alternatively, start a new solver with all the current calls (solver.assertions()), minus the retracted ones
* Incorporate extra roles (triple agend, suspicious service etc)
* Incorporate Hidden Agenda
* Create "live" tool, usable during gameplay
    * Prompt for new info
    * Give updated variants after each new piece of information
         * Alert when at least one virus is identified
         * Calculate percent chance that each player is virus?
    * Suggest which players to pick for secret intel, confession etc
         * Calculate bits of information aquired from each option
* Create bot
