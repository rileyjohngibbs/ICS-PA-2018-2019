# Mad Lib

App by Riley John Gibbs for filling out Mad Libs with user input.

## Usage

This is only compatible with Python 3, not Python 2. Run it from the command line from outside the madlib directory like so:

```
python madlib <story_file>
```

If no story file is provided, then the example story will be provided. The example is adapted from "Fear," by Lydia Davis, available [here](http://www.conjunctions.com/print/article/lydia-davis-c24).

## Writing Stories

To write a story for usage with this app, designated placeholders using curly braces `{}`. The text inside the curly braces will be used as the name for that placeholder, and be used to ask the user for input. If the same placeholder name is placed inside of two pairs of curly braces, then the same value will be used for both locations.

For convenience, you can end a placeholder name inside the curly braces with a space or underscore, followed by a number, which will be excluded from the request to the user for their value. For example, `{noun 3}` will be rendered as only "A noun" when asking the user for the value.

Values will be asked for in alphabetical order by placeholder name.

Stories should be saved as raw text files (.txt format). For an example, see `example_story.txt` in this directory.
