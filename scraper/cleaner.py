def clean_ml_features(df):
    """Sanitizes text columns by removing bracketed footnotes."""
    bracket_pattern = r'\[.*?\]'
    df = df.astype(str)

    for i in range(len(df.columns)):
        df.iloc[:, i] = df.iloc[:, i].str.replace(bracket_pattern, '', regex=True).str.strip()
            
    return df