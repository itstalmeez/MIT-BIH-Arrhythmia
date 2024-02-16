import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv("MIT-BIH Arrhythmia Database.csv")

# Select relevant columns for features and labels
feature_columns = [
    '0_pre-RR', '0_post-RR', '0_pPeak', '0_tPeak', '0_rPeak', '0_sPeak', '0_qPeak',
    '0_qrs_interval', '0_pq_interval', '0_qt_interval', '0_st_interval', '0_qrs_morph0', '0_qrs_morph1',
    '0_qrs_morph2', '0_qrs_morph3', '0_qrs_morph4', '1_pre-RR', '1_post-RR', '1_pPeak', '1_tPeak', '1_rPeak',
    '1_sPeak', '1_qPeak', '1_qrs_interval', '1_pq_interval', '1_qt_interval', '1_st_interval', '1_qrs_morph0',
    '1_qrs_morph1', '1_qrs_morph2', '1_qrs_morph3', '1_qrs_morph4'
]

target_column = 'type'

# Extract features and labels
X = data[feature_columns]
y = data[target_column]

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the machine learning model (Random Forest as an example)
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
