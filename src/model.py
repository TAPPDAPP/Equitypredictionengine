from sklearn.ensemble import RandomForestRegressor

def train_model(X_train, y_train):
    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=10,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model
