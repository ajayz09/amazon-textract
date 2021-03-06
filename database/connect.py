#!/usr/bin/python
import psycopg2
from config import config
 
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
      
        # create a cursor
        cur = conn.cursor()
        
   # execute a statement
        print('PostgreSQL database version:')
        # cur.execute("SELECT file_record.id,subdir FROM document_processor.file_record JOIN document_processor.client_document on client_document.file=file_record.id and type='Distribution' and subdir LIKE 'unprocessed_file/%';")
        # sql = "SELECT file_record.id,subdir FROM document_processor.file_record JOIN document_processor.client_document on client_document.file=file_record.id and type='Distribution' and subdir LIKE 'unprocessed_file/%';"
        # sql = "SELECT * from document_processor.file_record;"
        # cur.execute(sql)
        
        sql = "SELECT * FROM document_processor.file_record JOIN document_processor.dividend_statement ON dividend_statement.file_record_id = file_record.id;" 
        number_of_rows = cur.execute(sql)
        
        while True:
            row = cur.fetchone()
            if row == None:
                break
            print(row)

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
       # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    connect()