import sqlite3

def update_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    # Check existing columns
    c.execute("PRAGMA table_info(users)")
    columns = [col[1] for col in c.fetchall()]
    
    print(f"📋 Existing columns: {columns}")
    
    # Add name column if not exists
    if 'name' not in columns:
        c.execute("ALTER TABLE users ADD COLUMN name TEXT")
        print("✅ Added 'name' column")
    else:
        print("ℹ️ 'name' column already exists")
    
    # Add profile_pic column if not exists
    if 'profile_pic' not in columns:
        c.execute("ALTER TABLE users ADD COLUMN profile_pic TEXT")
        print("✅ Added 'profile_pic' column")
    else:
        print("ℹ️ 'profile_pic' column already exists")
    
    # Add google_id column if not exists
    if 'google_id' not in columns:
        c.execute("ALTER TABLE users ADD COLUMN google_id TEXT UNIQUE")
        print("✅ Added 'google_id' column")
    else:
        print("ℹ️ 'google_id' column already exists")
    
    # Update existing users with default name if name is NULL
    c.execute("UPDATE users SET name = username WHERE name IS NULL")
    
    conn.commit()
    conn.close()
    
    print("\n✅ Database update completed successfully!")
    print("📋 New columns: name, profile_pic, google_id")

if __name__ == "__main__":
    update_database()