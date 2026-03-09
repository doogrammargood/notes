This folder contains code snippets for the code tracing exercise.

Instructions:
Students break into groups. Each group plays a game with the code

The students take turns:
    -using a token to indicate the current line of code. 
    They write on paper with pencil:
        - the names and values of all of the variables.
        - The step number (how many turns there have been).
        - Anything that gets printed.

If at any point, a player notices an error in another player's answer, that player may "challenge" the incorrect answer. The players deliberate to determine who is correct. If they cannot decide unanimously, then the players consult the debugger. The players must restart the exercise if any challenges occur, correct or incorrect.

Scoring: 
- A player who challenges correctly gets +2.
- A player who challenges incorrectly gets -1.
- A player whose mistake is revealed by a challenge gets -1.
- If a challenge shows that there was a mistake earlier than the step that was challenged, then all players get -1, except the challenger.
- If players complete a game and the debuger had different behavior from their trace, then all players get -1 and they restart the exercise.
--
Start on Exercise_0 and play through in order. After each exercise, run the debugger and check that the program executed as expected.

Exercises 10+ contain functions. There are additional rules for functions:
    1. Be sure to step into any user-defined functions. Don't step over.
    2. You must specify whether variables are local or global, relative to the current line.
    3. You must write the call stack.
--
Note: We want to be very precise with these exercises. Spacing and capitalization matter. An error counts as an error. For example, writing that a has value 5 instead of "5" is an error.