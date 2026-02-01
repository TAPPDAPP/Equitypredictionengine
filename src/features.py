import pandas as pd
import ta

def create_features(df):
    df["return"] = df["Close"].pct_change()
    df["log_return"] = np.log(df["Close"] / df["Close"].shift(1))
    df["volatility"] = df["return"].rolling(21).std()

    df["rsi"] = ta.momentum.RSIIndicator(df["Close"]).rsi()
    df["macd"] = ta.trend.MACD(df["Close"]).macd()
    df["sma_50"] = df["Close"].rolling(50).mean()
    df["sma_200"] = df["Close"].rolling(200).mean()

    df.dropna(inplace=True)
    return df
