Song of The Day Bot!

This bot gives you a song of the day, and is also able to react to certain trigger words. It's made to have a minor obsession with J-Rock (the best music genre, of course).

The bot uses the Audio DB ( https://www.theaudiodb.com/ )'s v1 (free) API to find songs. It does take some time to find a song, since not all IDs it generates are valid in the
Audio DB, but it warns you beforehand. It displays the song's name, artist, and album. If a request for a song of the day is made multiple times in the same day, as long as the bot is continueously being run during that time, the bot will simply display the song it made the first time, so it's daily rather than being a random generator. It also keeps a live list of song ID's, so a song can't be picked as the song of the day multiple times.

Future plans:
- Add more interactivity to it so it can also give information on songs