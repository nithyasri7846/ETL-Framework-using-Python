def validate(df, rules):
    """
    Performs basic data quality checks
    """
    report = {}

    for column in rules.get("not_null", []):
        report[column] = int(df[column].isnull().sum())

    return report
