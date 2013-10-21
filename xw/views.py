from __future__ import unicode_literals

import itertools
import os.path
import xw
from pyramid.view import view_config

def get_numbers(lines, clues):
    clues_iter = iter(clues)
    clue_num = 1
    clue_positions = {}
    across_tups = []
    down_tups = []
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '.':
                continue

            start = False
            if j == 0 or lines[i][j-1] == '.':
                # start of an across clue
                across_tups.append((clue_num, next(clues_iter)))
                start = True

            if i == 0 or lines[i-1][j] == '.':
                # start of a down clue
                down_tups.append((clue_num, next(clues_iter)))
                start = True

            if start:
                clue_positions[(i, j)] = clue_num
                clue_num += 1
    return clue_positions, across_tups, down_tups

@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    root_dir = os.path.dirname(os.path.dirname(xw.__file__))
    filename = os.path.join(root_dir, 'sample.puz')
    with open(filename) as f:
        contents = f.read()
    grid_and_title_and_creator, clues, _ = contents.split(b'\x00\x00\x00')[3].split(b'\x00\x00')
    grid_and_title, creator = grid_and_title_and_creator.split(b'\x00')
    solution = grid_and_title[:225]
    s = grid_and_title[225:450]
    title = grid_and_title[450:]
    clues = clues.split(b'\x00')
    lines = []
    LINE_SIZE = 15
    for i in itertools.count(0, LINE_SIZE):
        if i >= len(s):
            break
        lines.append(s[i:i+LINE_SIZE])
    clue_positions, across_tups, down_tups = get_numbers(lines, clues)

    return {
        'project': 'xw',
        'lines': lines,
        'clue_positions': clue_positions,
        'across_tups': across_tups,
        'down_tups': down_tups,
    }
