## Task 4 — Data Visualization & Machine Learning

A student performance dataset was analyzed to produce meaningful visualizations, and build a machine learning model to predict whether a student will pass or fail — end to end.

In this task, a Logistic Regression model is built to predict whether a student will pass or fail based on their academic performance and study habits.

The dataset is divided into features (subject scores, attendance, study hours) and a target variable (`passed`). The data is then split into training and testing sets. Since the features are on different scales, they are standardised using `StandardScaler` before training the model.

The model is trained on the training data and evaluated on the test data using accuracy. Predictions are compared with actual results to understand model performance.

Feature importance is analysed using model coefficients, showing which factors most influence the prediction. A positive coefficient indicates a higher chance of passing, while a negative coefficient indicates a higher chance of failing.

Finally, the model is used to predict the result of a new student based on given input values, along with the probability of the prediction.
