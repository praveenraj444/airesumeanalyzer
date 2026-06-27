import sqlite3

def fix_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    # Create new table without NOT NULL constraint on password
    c.execute('''CREATE TABLE IF NOT EXISTS users_new
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE,
                  email TEXT UNIQUE NOT NULL,
                  password TEXT,  -- Removed NOT NULL
                  google_id TEXT UNIQUE,
                  name TEXT,
                  profile_pic TEXT,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # Copy data from old table to new table
    c.execute('''INSERT INTO users_new (id, username, email, password, google_id, name, profile_pic, created_at)
                 SELECT id, username, email, password, google_id, name, profile_pic, created_at FROM users''')
    
    # Drop old table
    c.execute("DROP TABLE users")
    
    # Rename new table
    c.execute("ALTER TABLE users_new RENAME TO users")
    
    conn.commit()
    conn.close()
    
    print("✅ Database fixed! Password column no longer has NOT NULL constraint.")
    print("📋 Google Login will now work properly.")

if __name__ == "__main__":
    fix_database()