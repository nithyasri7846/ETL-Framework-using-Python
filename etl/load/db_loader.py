import psycopg2
from etl.utils.logger import get_logger

logger = get_logger("DB_LOADER")

def save_to_db(df):
    conn = psycopg2.connect(
        dbname="etl_db",
        user="postgres",
        password="Nithya**26",   # use your pgAdmin password
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(
            """
            INSERT INTO staging.sample_data
            (id, name, email, age, processed_at)
            VALUES (%s, %s, %s, %s, %s)
            """,
            tuple(row)
        )

    conn.commit()
    cur.close()
    conn.close()

    logger.info(f"{len(df)} rows inserted into staging.sample_data")
