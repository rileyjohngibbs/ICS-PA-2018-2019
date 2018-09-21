import re
import sys


def do_mad_lib(story):
    user_inputs = get_user_inputs(story)
    return story.format(**user_inputs)


def get_user_inputs(story):
    print('Please provide...')
    return {
        entry: input(f'{display_entry_name(entry).capitalize()}: ')
        for entry in get_entries(story)
    }


def get_entries(story):
    return sorted([word[1:-1] for word in set(re.findall(r'\{[^}]*\}', story))])


def display_entry_name(entry_name):
    number_stripped = re.match(r'(.*[^0-9])([_\s][0-9]+)?$', entry_name).groups()[0]
    with_spaces = number_stripped.replace('_', ' ')
    if with_spaces[0] in 'aeiouAEIOU':
        article = 'an'
    else:
        article = 'a'
    return f'{article} {with_spaces}'
