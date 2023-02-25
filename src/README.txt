I think I have a working code. 

I would still like to test more on border cases.

I know I have essentially used one huge class.

This I would try to split up, into the game, and a class for the logger to print to the user.

I might also separate the reading of the words from the file, since that is only done once, and therefore the _word_file_rel_path attribute is only ever used once.

I would now also do type hints. Since I only did one.

Also I am not happy that half the attrs are private and half are not.

Missing report summary.

printer.assert_called_with seems to have problems with the underscores. It's return value is missing any underscore

Don't know how to create a mocker that has several return values.

Jonas Sinjan.