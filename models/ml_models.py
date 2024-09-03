from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from joblib import dump




def preprocess_data(data):
    data["Age"] = data["Age"].fillna(data["Age"].mean())
    data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])
    data['Sex'] = data['Sex'].map({'female': 0, 'male': 1})

    data = pd.get_dummies(data, columns=["Embarked"])

    data.drop(columns=['PassengerId', 'Ticket', 'Name', 'Cabin'], inplace=True)
    return data


def train_model(data):
    X = data.drop(['Survived'], axis=1)
    Y = data['Survived']

    estimators = [i for i in range(10, 210, 10)]
    depth = [i for i in range(1, 24, 4)]
    params = {"n_estimators": estimators,
              "max_depth": depth}
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    random_forest = RandomForestClassifier(criterion='entropy', random_state=42)
    grid_search = GridSearchCV(random_forest, params, scoring='accuracy', n_jobs=4)
    grid_search.fit(X_train, y_train)

    print(f"Best Parameters: {grid_search.best_params_}")
    print(f"Best mean cv accuracy: {grid_search.best_score_}")

    y = grid_search.best_estimator_.predict(X_test)
    print(f'Accuracy after GridSearch: {accuracy_score(y_test, y)}')

    return grid_search.best_estimator_


if __name__ == "__main__":
    data = pd.read_csv("../train.csv")
    data = preprocess_data(data)
    best_model = train_model(data)
    dump(best_model, "best_model.joblib")
