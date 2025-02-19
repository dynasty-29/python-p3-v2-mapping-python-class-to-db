from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"
    @classmethod
    def create_table(cls):
        """Create the departments table"""
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                location TEXT
            )
        """)
        CONN.commit()
    @classmethod    
    def drop_table(cls):
        """Drop the table that persists Department instances"""
        CURSOR.execute("DROP TABLE IF EXISTS departments;")
        CONN.commit()
        
    def save(self):
        """Insert a new department into the database and set its ID"""
        CURSOR.execute("""
            INSERT INTO departments (name, location) 
            VALUES (?, ?)
        """, (self.name, self.location))

        CONN.commit()
        self.id = CURSOR.lastrowid  # Get assigned ID
        
    @classmethod
    def create(cls, name, location):
        """Initialize a new department instance and save the object to the database """ 
        department = cls(name, location)
        department.save()
        return department
    
    def update(self):
        """Update the table row corresponding to the current Department instance. """   
        CURSOR.execute("""
                       UPDATE departments
                       SET name = ?, location = ?
                       WHERE id = ?
                       """, (self.name, self.location, self.id))
        CONN.commit()
    def delete(self):
        """Delete the table row corresponding to the current Department instance""" 
        CURSOR.execute("""
                       DELETE FROM departments
                       WHERE id = ?
                       """, (self.id,))   
        CONN.commit()