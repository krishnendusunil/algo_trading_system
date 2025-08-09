from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import ta

def prepare_ml_data(df):
    """
    Prepares data for the ML model by adding indicators and a target variable.
    Target: 1 if the next day's close is higher, 0 otherwise.
    """
    df = df.copy()

    # Add indicators
    df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
    macd = ta.trend.MACD(df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_Signal'] = macd.macd_signal()
    df['SMA_20'] = ta.trend.sma_indicator(df['Close'], window=20)
    df['SMA_50'] = ta.trend.sma_indicator(df['Close'], window=50)

    # Target variable
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)

    df.dropna(inplace=True)

    features = ['RSI', 'MACD', 'MACD_Signal', 'SMA_20', 'SMA_50', 'Volume']
    X = df[features]
    y = df['Target']

    return X, y, features

def train_and_evaluate_model(df):
    """
    Trains a Decision Tree model and evaluates its accuracy.
    """
    try:
        X, y, features = prepare_ml_data(df)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        model = DecisionTreeClassifier(random_state=42)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        return model, accuracy, features
    except Exception as e:
        print(f"Error in ML model training: {e}")
        return None, 0.0, None
