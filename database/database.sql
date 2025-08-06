-- SOUND
CREATE TABLE IF NOT EXISTS Sound (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    main_name TEXT NOT NULL,
    genre TEXT,
    main_bpm FLOAT,
    min_bpm FLOAT,
    max_bpm FLOAT,

    main_audio_source TEXT,
);

CREATE TABLE IF NOT EXISTS TranslatedSoundName (
    sound_id INTEGER REFERENCES Sound(id),
    language TEXT NOT NULL,
    translated_name TEXT NOT NULL,

    PRIMARY KEY (sound_id, language)
);

-- SOUND/CONTRIBUTOR CONNECTION
CREATE TABLE IF NOT EXISTS MadeBy (
    sound_id INTEGER REFERENCES Sound(id),
    contributor_id INTEGER REFERENCES Contributor(id),

    role TEXT NOT NULL,

    PRIMARY KEY (sound_id, contributor_id)
);

-- CONTRIBUTOR
CREATE TABLE IF NOT EXISTS Contributor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ContributorAlias (
    contributor_id INTEGER REFERENCES Contributor(id),
    alias TEXT NOT NULL,
    PRIMARY KEY (contributor_id, alias)
);

-- CHARTER
CREATE TABLE IF NOT EXISTS Charter (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS CharterAlias (
    charter_id INTEGER REFERENCES Charter(id),
    alias TEXT NOT NULL,
    PRIMARY KEY (charter_id, alias)
);

-- GAME
CREATE TABLE IF NOT EXISTS Game (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    release_date DATE NOT NULL,
    developer TEXT NOT NULL
);

-- LEVEL
CREATE TABLE IF NOT EXISTS Level (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    game_id INTEGER NOT NULL REFERENCES Game(id),
    sound_id INTEGER NOT NULL REFERENCES Sound(id),
    charter_id INTEGER REFERENCES Charter(id),

    difficulty_name TEXT,
    difficulty_value FLOAT,

    length INTEGER,
    release_date DATE,

    chart BLOB
);

-- ALBUM
CREATE TABLE IF NOT EXISTS Album (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    release_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS AlbumSound (
    album_id INTEGER REFERENCES Album(id),
    sound_id INTEGER REFERENCES Sound(id),
    PRIMARY KEY (album_id, sound_id)
);