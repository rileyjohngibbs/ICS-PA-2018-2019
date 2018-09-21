import os
import sys

import madlib

if len(sys.argv) > 1:
    filepath = sys.argv[1]
else:
    filepath = os.path.dirname(os.path.abspath(__file__)) + '/example_story.txt'
with open(filepath, 'r') as storyfile:
    story = storyfile.read()
completed_mad_lib = madlib.do_mad_lib(story)
print()
print(completed_mad_lib)
