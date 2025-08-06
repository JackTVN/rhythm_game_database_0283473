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

def get_id_song():
    cursor.execute("""
        SELECT Sound.id, Sound.main_name FROM Sound;
    """)

    return cursor.fetchall()

def get_id_game():
    cursor.execute("""
        SELECT Game.id, Game.name FROM Game;
    """)

    return cursor.fetchall()

def get_id_contributor():
    cursor.execute("""
        SELECT Contributor.id, Contributor.name FROM Contributor;
    """)

    return cursor.fetchall()

# CLI-like thing
def push_new_song():
    song_name = input("Name: ")
    song_genre = input("Genre: ")
    main_bpm = input("Main BPM: ")
    min_bpm = input("Min BPM: ")
    max_bpm = input("Max BPM: ")
    source = input("Source Link: ")

    cursor.execute('''
        INSERT INTO Sound (main_name, genre, main_bpm, min_bpm, max_bpm, main_audio_source)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (song_name, song_genre, float(main_bpm), float(min_bpm), float(max_bpm), source))

    conn.commit()

    print("New song added successfully")

def push_made_by():
    command = input("Want to check the sound list before crediting? (Y/N): ")

    match command:
        case "Y":
            rows = get_id_song()

            print("Sounds List:")
            for row in rows:
                print(str(row[0]) + ". " + row[1])

    sound_id = input("Sound ID: ")

    isAdding = True
    contributor_id = None
    contributor_role = None
    
    while isAdding:
        command = input("Want to check the contributors list before crediting? (Y/N): ")

        match command:
            case "Y":
                rows = get_id_contributor()

                print("Contributors List:")
                for row in rows:
                    print(str(row[0]) + ". " + row[1])

        command = input("Is the contributor in the current list? (Y/N): ")

        match command:
            case "N":
                contributor_id = push_new_contributor()
                contributor_role = input("What is their role on the song?: ")

            case "Y":
                contributor_id = input("Contributor ID: ")
                contributor_role = input("What is their role on the song?: ")

        cursor.execute("""
            INSERT INTO MadeBy (sound_id, contributor_id, role)
            VALUES (?, ?, ?);
        """, (sound_id, contributor_id, contributor_role))

        conn.commit()

        command = input("Are there other contributors you want to add to the song? (Y/N)")

        match command:
            case "N":
                isAdding = False

    print("Song Credited!")
    
def push_new_level():
    print("Do you want to check the song list and the game list before adding? (Y/N)")
    command = input()

    match command:
        case "Y":
            rows = get_id_song()

            print("Songs List:")
            for row in rows:
                print(str(row[0]) + ". " + row[1])

            rows = get_id_game()

            print("\nGames List:")
            for row in rows:
                print(str(row[0]) + ". " + row[1])

        case "N":
            pass

    print("Song ID for level: ")
    song_id = input()

    print("Game ID for level: ")
    game_id = input()

    print("Difficulty Name: ")
    dif_name = input()

    print("Difficulty Value: ")
    dif_value = input()

    print("Length: ")
    len = input()

    print("Release Date: ")
    date = input()

    cursor.execute("""
        INSERT INTO Level (game_id, sound_id, difficulty_name, difficulty_value, length, release_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (song_id, game_id, dif_name, dif_value, len, date))

    conn.commit()

    print("New level added!")

def push_new_contributor():
    name = input("Add new Contributor: ")

    cursor.execute("""
        INSERT INTO Contributor (name)
        VALUES (?);
    """, (name,))

    conn.commit()

    print("New Contributor Added!")

    return cursor.lastrowid

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

print("Welcome to the Rhythm Game Database Writer. What do you want to do?")

while isRunning:
    print("1. Add a new song")
    print("2. Credit (add a contributor to) a song")
    print("3. Add a level")
    print("99. Quit")

    command = input()

    match command:
        case '1':
            push_new_song()

        case "2":
            push_made_by()

        case '3':
            push_new_level()

        case '99':
            isRunning = False
            continue

print("Writer closed!")

# Clean up
cursor.close()
conn.close()