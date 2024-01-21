# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler

# # Assuming your dataset is a DataFrame named 'marketplaces'
# # with columns 'latitude', 'longitude', and 'marketplace_name'

# # Step 2: Feature Scaling
# scaler = StandardScaler()
# marketplaces[['latitude', 'longitude']] = scaler.fit_transform(marketplaces[['latitude', 'longitude']])

# # Step 3: Train-Test Split
# X_train, X_test, y_train, y_test = train_test_split(marketplaces[['latitude', 'longitude']], marketplaces['marketplace_name'], test_size=0.2, random_state=42)

# # Step 4: Train the KNN Model
# knn_model = KNeighborsClassifier(n_neighbors=5)  # You can experiment with different values for 'n_neighbors'
# knn_model.fit(X_train, y_train)

# # Step 5: Make Predictions
# current_position = scaler.transform([[current_latitude, current_longitude]])
# nearest_marketplace = knn_model.predict(current_position)

# print("The nearest marketplace is:", nearest_marketplace[0])
