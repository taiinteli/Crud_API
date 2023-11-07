#!/bin/sh

# Path to the database file
DB_FILE="/data/mydatabase.db"

# Check if the database file already exists
if [ ! -f "$DB_FILE" ]; then
    echo "Creating database file..."
    sqlite3 $DB_FILE "VACUUM;"
fi

# If you have any initialization SQL commands, you could run them here
# sqlite3 $DB_FILE < /path/to/init.sql

# Keep the container running (if needed)
tail -f /dev/null