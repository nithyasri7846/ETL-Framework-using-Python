import pandas as pd
from etl.utils.logger import get_logger

logger = get_logger("CSV_INGEST")

def ingest(path):
    logger.info(f"Reading CSV file from {path}")
    df = pd.read_csv(path)
    logger.info(f"Ingested {len(df)} rows")
    return df
