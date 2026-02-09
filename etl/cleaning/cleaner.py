def clean(df, config):
    """
    Cleans the dataframe based on config rules
    """
    if config.get("drop_duplicates"):
        df = df.drop_duplicates()

    if config.get("fillna") == "mean":
        df = df.fillna(df.mean(numeric_only=True))

    return df
