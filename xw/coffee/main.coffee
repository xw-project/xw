Keycodes =
  LEFT: 37
  UP: 38
  RIGHT: 39
  DOWN: 40

$ ->
  rows = $('#crossword').find 'tr'
  window.lights = {}
  for tr, i in rows
    for td, j in $(tr).children 'td'
      td = $ td
      if td.hasClass 'dark' or not td.hasClass 'light'
        continue

      input = td.find 'input'
      input.data 'pos', [i, j]
      if not lights.hasOwnProperty i
        lights[i] = {}
      lights[i][j] = input

  $('td.light input').on 'keydown', (e) ->
    [row, col] = $(e.target).data 'pos'
    dir = (switch e.which
      when Keycodes.LEFT then [0, -1]
      when Keycodes.UP then [-1, 0]
      when Keycodes.RIGHT then [0, 1]
      when Keycodes.DOWN then [1, 0]
    )
    if not dir
      return
    [drow, dcol] = dir
    valid_input = null
    [r, c] = [row+drow, col+dcol]
    while 0 <= r < 15 and 0 <= c < 15
      if lights.hasOwnProperty(r) and lights[r].hasOwnProperty c
          valid_input = lights[r][c]
          break
      [r, c] = [r + drow, c + dcol]
    if valid_input
      valid_input.focus()

# TODO(Darren, 2013/10/20)
# highlight current word
# keep track of typing vertically vs horizontally
# move to next square after typing letter
