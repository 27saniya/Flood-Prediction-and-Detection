# Flood Prediction and Detection using Satellite Imagery

## Targeted Problem and Goal:
The flood prediction model is complex due to the consideration of various factors like geographical location, hydrology and human activities.
Previous research paper review: Supervised Machine learning algorithms can face challenges in predictions due to complexity of the data, the amount of time required for computation.
Hence the goal is to implement supervised as well as unsupervised machine learning models on satellite imagery, tidal, rainfall data to understand which method is more robust and gives better flood prediction accuracy.

## Data Description:
1. INSAT Images (jpg format) extracted with Python Script from IMD website. https://mausam.imd.gov.in 
2. Weather Data (json format) collected from OpenWeather API. https://openweathermap.org
3. Tidal Data (json format) collected from MareaAPI https://api.marea.ooo/ <br>
All these data were collected for a duration of one month after every 15 minutes

### Data Exploration:

![image](https://github.com/27saniya/Flood-Prediction-and-Detection/assets/101293878/d6489cec-5357-432b-a31d-34b19bf715ae)
![image](https://github.com/27saniya/Flood-Prediction-and-Detection/assets/101293878/6506a3ef-3c85-40cc-a6fe-15fcb1f3fd60)

### Data Pre-processing:
- Data not relevant for the analysis was removed
- Missing values were handled
- For image data, the images were cropped to eliminate noise and image enhancing was performed <br>

### Data Integration:

- Data from these sources was then merged based on the timestamp
- One hot encoding and normalization was also performed

### Data Preparation:
- Data was then split into training and testing sets (80:20)
- The data was imbalanced, hence SMOTE was performed
- 3 fold cross validation was also performed

### Machine Learning:
Models Used:
1. Support Vector Machines
2. Random Forest
3. XG Boost Classifier
4. K-means Clustering

### Results:

![image](https://github.com/27saniya/Flood-Prediction-and-Detection/assets/101293878/a360ade7-4178-446d-883f-e3a4cac269a8)














