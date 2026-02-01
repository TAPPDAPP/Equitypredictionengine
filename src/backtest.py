import numpy as np

def backtest(preds, actual):
    strategy_returns = np.sign(preds - actual.shift(1)) * actual.pct_change()
    cumulative = (1 + strategy_returns.fillna(0)).cumprod()
    return cumulative
