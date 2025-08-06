import sqlite3

conn = sqlite3.connect('rhythm_game.db')  
cursor = conn.cursor()

# This simply print all the information of a song
# Need data to be sorted and compacted in a very weird way to work
# Would need to be independent for real project
def print_song_info(sound_name, genre, bpm_compacted, contributor_compacted, game, difficulty_compacted):
    print(sound_name + " - " + contributor_compacted)
    print("Genre: " + genre)
    print("BPM: " + bpm_compacted)
    print(difficulty_compacted)

# Fetch all rows
# Print out the sound information
# Current plan:
# Format information when going through each sound_id
# Print information only when the sound_id change
def print_all(rows):
    last_sound_id = None
    contributor_list = []
    game_list = []
    level_list = []

    sound_name_text = ""
    genre_text = ""
    bpm_text = ""
    contributor_text = ""
    game_text = ""
    difficulty_text = ""

    print("FULL Sound Table Records:")

    for sound_id, sound_name, genre, main_bpm, min_bpm, max_bpm, contributor_id, contributor_name, contributor_role, game, game_id, level_id, diff_name, diff_value, length, release_date in rows:
        if last_sound_id != sound_id and last_sound_id:
            print_song_info(sound_name_text, genre_text, bpm_text, contributor_text, game_text, difficulty_text)

            contributor_list = []
            contributor_text = ""
            game_list = []
            level_list = []
            difficulty_text = ""

        last_sound_id = sound_id
        sound_name_text = sound_name
        genre_text = genre
        game_text = game
        
        if (min_bpm == max_bpm):
            bpm_text = str(main_bpm)
        else:
            bpm_text = str(min_bpm) + " - " + str(max_bpm) + " (" + str(main_bpm) + ")"

        # For when there are more than one contributor
        # The contributor needed to be format first before printing at the end
        if (not contributor_id in contributor_list):
            if not contributor_list:
                contributor_text += contributor_name + " (" + contributor_role + ")"
            else:
                contributor_text += ", " + contributor_name + " (" + contributor_role + ")"

            contributor_list.append(contributor_id)

        # Same thing for level list. Be sure to separate by game
        if (not level_id in level_list):
            if (not game_id in game_list):
                difficulty_text += "Level from " + game + ":\n"
                game_list.append(game_id)

            difficulty_text += "   " + diff_name + " " + str(diff_value) + "\n"
            level_list.append(level_id)

    print_song_info(sound_name_text, genre_text, bpm_text, contributor_text, game_text, difficulty_text)

# CLI-like thing

# GET - Just get the rows list
def get_song_list():
    # Fetch every necessary data for a song information page
    cursor.execute("""
        SELECT 
            Sound.id, Sound.main_name, Sound.genre, Sound.main_bpm, Sound.min_bpm, Sound.max_bpm, 
            Contributor.id, Contributor.name, MadeBy.role,
            Game.name,
            Level.game_id, Level.id, Level.difficulty_name, Level.difficulty_value, Level.length, Level.release_date
        FROM MadeBy 
        INNER JOIN Sound ON MadeBy.sound_id = Sound.id
        INNER JOIN Contributor ON MadeBy.contributor_id = Contributor.id
        INNER JOIN Level ON Sound.id = Level.sound_id
        INNER JOIN Game ON Level.game_id = Game.id
        ORDER BY Sound.id, Contributor.id, Level.game_id;
    """)

    return cursor.fetchall()

def get_song_by_game_id(game_id):
    cursor.execute("""
        SELECT 
            Sound.id, Sound.main_name, Sound.genre, Sound.main_bpm, Sound.min_bpm, Sound.max_bpm, 
            Contributor.id, Contributor.name, MadeBy.role,
            Game.name,
            Level.game_id, Level.id, Level.difficulty_name, Level.difficulty_value, Level.length, Level.release_date
        FROM MadeBy 
        INNER JOIN Sound ON MadeBy.sound_id = Sound.id
        INNER JOIN Contributor ON MadeBy.contributor_id = Contributor.id
        INNER JOIN Level ON Sound.id = Level.sound_id
        INNER JOIN Game ON Level.game_id = Game.id
        WHERE Level.game_id = ?
        ORDER BY Sound.id, Contributor.id, Level.game_id
    """, (game_id))

    return cursor.fetchall()

def get_song_by_bpm(min_bpm, max_bpm):
    cursor.execute("""
        SELECT 
            Sound.id, Sound.main_name, Sound.genre, Sound.main_bpm, Sound.min_bpm, Sound.max_bpm, 
            Contributor.id, Contributor.name, MadeBy.role,
            Game.name,
            Level.game_id, Level.id, Level.difficulty_name, Level.difficulty_value, Level.length, Level.release_date
        FROM MadeBy 
        INNER JOIN Sound ON MadeBy.sound_id = Sound.id
        INNER JOIN Contributor ON MadeBy.contributor_id = Contributor.id
        INNER JOIN Level ON Sound.id = Level.sound_id
        INNER JOIN Game ON Level.game_id = Game.id
        WHERE Sound.main_bpm >= ? AND Sound.main_bpm <= ?
        ORDER BY Sound.id, Contributor.id, Level.game_id
    """, (min_bpm, max_bpm))

    return cursor.fetchall()

# CHOICE - print out function for user to use
def choice_game_list():
    cursor.execute("""
        SELECT * FROM Game;
    """)

    rows = cursor.fetchall()

    print("Choose a game: ")
    for row in rows:
        print(str(row[0]) + ". " + row[1])

    command = input()
    return command

isRunning = True

print("Welcome to the Rhythm Game Database viewer. What do you want to do?")

while isRunning:
    print("1. Get every songs/levels")
    print("2. Get song from a specific game")
    print("3. Get song in a specific BPM range")
    print("99. Quit")

    command = input()

    match command:
        case '1':
            rows = get_song_list()
            print_all(rows)

        case '2':
            game_id = choice_game_list()
            rows = get_song_by_game_id(game_id)
            print_all(rows)

        case '3':
            min_bpm = input("Input Min BPM: ")
            max_bpm = input("Input Max BPM: ")
            rows = get_song_by_bpm(min_bpm, max_bpm)
            print_all(rows)

        case '99':
            isRunning = False
            continue

print("Viewer closed!")

# Clean up
cursor.close()
conn.close()