# Tic-tac-toe API

An API that plays the game called tic-tac-toe in the US, and called naughts and crosses in some countries.  Instructions for how to play the game are here if you’ve never played before: http://www.exploratorium.edu/brain_explorer/tictactoe.html

## Specifications

*   Server will be provided the current board in a GET request, using the 'board' parameter in the query string.
    *   If the board string doesn't represent a valid
        tic-tac-toe board, or it’s not plausibly o’s turn, we return an HTTP response code 400 (Bad Request)
*   Your server always plays as o.
*   Either player can go first.

### Board representation

The board is encoded as a string of nine characters where each character is either 'o', 'x', or a space. The nine characters are the tic-tac-toe board read left to right, top to bottom -- for example:
x|o|
-+-+-
o| |
-+-+-
 |x|
would be encoded with the string "xo o   x ", and an empty board would be a string of nine spaces.

### Example

`curl YOUR_URL?board=+xxo++o++`

Should return `oxxo  o  ` (o-x-x-o-space-space-o-space-space)
in the body of the HTTP response.

## Implementation

This package is a `flask` server that will play tic-tac-toe with you.
