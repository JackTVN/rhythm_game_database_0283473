import sqlite3

conn = sqlite3.connect('rhythm_game.db')  
cursor = conn.cursor()

'''
cursor.execute("""
    SELECT 
        Sound.id, Sound.main_name, Sound.genre, Sound.main_bpm, Sound.min_bpm, Sound.max_bpm, 
        Contributor.id, Contributor.name, MadeBy.role,
        Game.name,
        Level.game_id, Level.id, Level.difficulty_name, Level.difficulty_value, Level.length, Level.release_date
    FROM MadeBy 
    INNER JOIN Sound ON MadeBy.sound_id = Sound.id
    INNER JOIN Contributor ON MadeBy.contributor_id = Contributor.id
    LEFT OUTER JOIN Level ON Sound.id = Level.sound_id
    LEFT OUTER JOIN Game ON Level.game_id = Game.id
    ORDER BY Sound.id, Contributor.id, Level.game_id;
""")

rows = cursor.fetchall()

for row in rows:
    print(row)
'''

cursor.execute("DELETE FROM Level WHERE game_id = 8;")
conn.commit()

# Clean up
cursor.close()
conn.close()