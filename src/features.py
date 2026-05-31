def clean_data(df):
    required_cols = ["price", "squareMeters", "rooms", "floor", "floorCount", "city"]
    df = df.dropna(subset=required_cols).copy()
    df = df[df["price"] > 0]
    df = df[df["squareMeters"] > 0]
    return df