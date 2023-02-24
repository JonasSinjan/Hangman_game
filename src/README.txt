I think I have a working code. 

I would still like to test more on border cases.

I know I have essentially used one huge class.

This I would try to split up, into the game, and a class for the logger to print to the user.

I might also separatae the reading of the words from the file, since that is only done once, and therefore the _word_file_rel_path attribute is only ever used once.

I would now also do type hints. Since I only did one.

Also I am not happy that half the attrs are private and half are not.

Nested if else in the _do_round method is not good.

Did Edit and Pray for the case where the user enters a letter that has already been guessed and therefore doesn't count as a round.

Jonas Sinjan.