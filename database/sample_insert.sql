-- THIS IS A SAMPLE INSERT, SO IT WILL CLEAR EVERYTHING BEFORE INSERTING
DELETE FROM TranslatedSoundName;
DELETE FROM ContributorAlias;
DELETE FROM MadeBy;
DELETE FROM Level;
DELETE FROM Game;
DELETE FROM Charter;
DELETE FROM Contributor;
DELETE FROM ChartBy;
DELETE FROM Sound;
DELETE FROM Album;
DELETE FROM AlbumSound;
DELETE FROM sqlite_sequence; 

-- SOUND
INSERT INTO Sound (main_name, genre, main_bpm, min_bpm, max_bpm, main_audio_source) VALUES
('Xaleid◆scopiX', 'Hardcore', 180, 180, 180, 'https://www.youtube.com/watch?v=-PTe8zkYt9A'),
('系ぎて', 'Artcore', 88, 88, 88, 'https://www.youtube.com/watch?v=q26OmWO8ccg'),
('PANDORA PARADOXXX', 'Artcore', 150, 150, 150, 'https://www.youtube.com/watch?v=TlRv2CmIngw'),
('Designant.', 'Drum & Bass', 200, 75, 400, 'https://www.youtube.com/watch?v=bautietoaBo'),
('Crossmythos Rhapsodia', 'Classical', 198, 198, 198, 'https://www.youtube.com/watch?v=jXv6R6tLW4A'),
('quixotic', 'Polypops', 174, 174, 174, 'https://www.youtube.com/watch?v=Bf6RTUHoBEg'),
('DATAERR0R', 'Artcore',  180, 180, 180, 'https://www.youtube.com/watch?v=mevx85e9QH8');

INSERT INTO TranslatedSoundName (sound_id, language, translated_name) VALUES
(2, 'en', 'Tsunagite');

-- CONTRIBUTOR

INSERT INTO Contributor (name) VALUES
('xi'),
('rintaro soma'),
('削除'),
('名乗る名が無い'),
('Acotto'),
('Potwi'),
('bermei.inazawa'),
('foolen'),
('Cosmograph');

INSERT INTO ContributorAlias (contributor_id, alias) VALUES
(3, 'Sakuzyo'),
(4, 'Nanoru Naganai'),
(9, 'Lunatic Sounds');

-- MADE BY

INSERT INTO MadeBy (sound_id, contributor_id, role) VALUES
(1, 1, 'Composer'),
(2, 2, 'Composer'),
(3, 3, 'Composer'),
(4, 4, 'Composer'),
(5, 5, 'Composer'),
(5, 6, 'Composer'),
(6, 7, 'Composer'),
(6, 8, 'Lyricist, Vocalist'),
(7, 9, 'Composer');

-- GAME
INSERT INTO Game (name, release_date, developer) VALUES
('maimai', '2012-07-11', 'SEGA'),
('CHUNITHM', '2015-07-16', 'SEGA'),
('SOUND VOLTEX', '2012-12-19', 'KONAMI'),
('beatmania IIDX', '1998-10-05', 'KONAMI'),
('jubeat', '2008-11-20', 'KONAMI'),
('Arcaea', '2017-10-13', 'lowiro'),
('DJMAX RESPECT', '2017-08-24', 'NEOWIZ');

-- CHARTER
INSERT INTO Charter (name) VALUES
('Toaster'),
('Nitro');

-- LEVEL
INSERT INTO Level (game_id, sound_id, difficulty_name, difficulty_value, length, release_date) VALUES
(1, 1, 'BASIC', 7.5, 265, '2025-07-13'),
(1, 1, 'ADVANCED', 11, 265, '2025-07-13'),
(1, 1, 'EXPERT', 13.5, 265, '2025-07-13'),
(1, 1, 'MASTER', 14.5, 265, '2025-07-13'),
(1, 1, 'RE:MASTER', 15, 265, '2025-07-13'),

(1, 2, 'BASIC', 7, 170, '2024-02-29'),
(1, 2, 'ADVANCED', 10, 170, '2024-02-29'),
(1, 2, 'EXPERT', 13.5, 170, '2024-02-29'),
(1, 2, 'MASTER', 14.5, 170, '2024-02-29'),
(1, 2, 'RE:MASTER', 15, 170, '2024-02-29'),

(1, 3, 'BASIC', 7.5, 177, '2019-05-10'),
(1, 3, 'ADVANCED', 11, 177, '2019-05-10'),
(1, 3, 'EXPERT', 13.5, 177, '2019-05-10'),
(1, 3, 'MASTER', 14.5, 177, '2019-05-10'),
(1, 3, 'RE:MASTER', 15, 177, '2019-05-10'),

(6, 4, 'Past', 7, 178, '2024-11-21'),
(6, 4, 'Present', 9, 178, '2024-11-21'),
(6, 4, 'Future', 10.5, 178, '2024-11-21'),
(6, 4, 'Beyond', 11.5, 178, '2024-11-21'),

(2, 5, 'BASIC', 6, 167, '2025-06-05'),
(2, 5, 'ADVANCED', 9.5, 167, '2025-06-05'),
(2, 5, 'EXPERT', 14.6, 167, '2025-06-05'),
(2, 5, 'MASTER', 15.7, 167, '2025-06-05'),

(7, 6, '6B-NORMAL', 6, 128, '2022-03-10'),
(7, 6, '6B-MAXIMUM', 12, 128, '2022-03-10'),
(7, 6, '6B-SC', 24, 128, '2022-09-10'),

(7, 6, '8B-NORMAL', 7, 128, '2022-03-10'),
(7, 6, '8B-HARD', 11, 128, '2022-03-10'),
(7, 6, '8B-MAXIMUM', 13, 128, '2022-03-10'),
(7, 6, '8B-SC', 25, 128, '2022-09-10'),

(1, 7, 'BASIC', 5, 135, '2025-04-11'),
(1, 7, 'ADVANCED', 8, 135, '2025-04-11'),
(1, 7, 'EXPERT', 11.5, 135, '2025-04-11'),
(1, 7, 'MASTER', 14, 135, '2025-04-11'),

(2, 7, 'BASIC', 3, 135, '2016-08-25'),
(2, 7, 'ADVANCED', 7, 135, '2016-08-25'),
(2, 7, 'EXPERT', 10.3, 135, '2016-08-25'),
(2, 7, 'MASTER', 14.0, 135, '2016-08-25'),

(6, 7, 'Past', 3, 125, '2017-06-02'),
(6, 7, 'Present', 7, 125, '2017-06-02'),
(6, 7, 'Future', 9, 125, '2017-06-02');

-- CHART CREDIT
INSERT INTO ChartBy (level_id, charter_id) VALUES
(16, 1),
(16, 2),
(17, 1),
(17, 2),
(18, 1),
(18, 2),
(19, 1),
(19, 2),
(39, 1),
(40, 1),
(41, 1);

-- ALBUM
INSERT INTO Album (name, release_date) VALUES
('maimai Collection', '2024-02-12');

INSERT INTO AlbumSound (album_id, sound_id) VALUES
(1, 1),
(1, 2),
(1, 3);