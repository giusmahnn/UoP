import os
import sqlite3
import csv

def extract_data_to_csv(db_file, tables, csv_folder):
    try:
        # Create the CSV folder if it doesn't exist
        if not os.path.exists(csv_folder):
            os.makedirs(csv_folder)
        
        # Connect to the SQLite database
        conn = sqlite3.connect('chinook.db')
        cursor = conn.cursor()

        for table_name in tables:
            # Execute a query to fetch data from the specified table
            cursor.execute(f"SELECT * FROM {table_name}")

            # Fetch all rows from the result
            rows = cursor.fetchall()

            # Get the column names
            column_names = [description[0] for description in cursor.description]

            # Write the data to a CSV file
            csv_file = os.path.join(csv_folder, f"{table_name}.csv")
            with open(csv_file, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                # Write the column names as the header
                csv_writer.writerow(column_names)
                # Write the rows of data
                csv_writer.writerows(rows)

            print(f"Data from table '{table_name}' extracted and saved to '{csv_file}' successfully.")

    except sqlite3.Error as e:
        print("Error extracting data:", e)

    finally:
        # Close the database connection
        if conn:
            conn.close()

# Example usage:
tables = ['albums', 'artists', 'customers', 'employees', 'genres', 'invoice_items',
          'invoice', 'media_types', 'playlist_track', 'playlist', 'tracks']
extract_data_to_csv('example.db', tables, 'csv_folder')
