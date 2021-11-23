# Music-Bingo

This program allows a user to select any spotify created playlist by entering their own developer ID/Secret and playlist URI using the spotipy API the "spotify_functions" file. The "music_bingo_algorithm" file then pulls the song list from "spotify_functions" and generates a random set of 24 tracks to fill the bingo boards, inserts them into an HTML string with fstring, and writes a new HTML file containing the tracks and board. The For loop can be adjusted by the user input so any number of boards can be made by appending them to the original file. 

TODO:
- Get HTML into seperate document while allowing variable formatting and enhance visual aesthetics of board.
- User created playlist so boards can be further customized.
