import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import KBinsDiscretizer


# Step 1: Load the Dataset
data = pd.read_csv('startup.csv')

continuous_columns = ['R&D Spend', 'Administration', 'Marketing Spend', 'Profit']  # Adjust this list as needed
discretizer = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')  # You can adjust the number of bins as needed
data[continuous_columns] = discretizer.fit_transform(data[continuous_columns])

# Step 3: Convert Categorical Variable to Numerical
state_mapping = {'California': 1, 'Florida': 2, 'New York': 3}
data['State'] = data['State'].map(state_mapping)

# Step 4: Split the data into features and target variable
X = data.drop('Profit', axis=1)  # Features
y = data['Profit']  # Target variable

# Step 5: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Create and Train the Decision Tree Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Step 7: Make Predictions
y_pred = model.predict(X_test)

# Step 8: Evaluate the Model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)



