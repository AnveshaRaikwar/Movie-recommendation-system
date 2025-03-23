
# Movie Recommendation System

## Overview
This project is a **Movie Recommendation System** that suggests movies based on user preferences and sentiment. It utilizes **K-Nearest Neighbors (KNN)** for recommendations and incorporates **sentiment-based filtering** to adjust suggestions accordingly.

## Tech Stack Used
- **Python**
- **Pandas** 
- **Scikit-learn**: Machine learning library for implementing KNN.
  
##  Some imp Features
- Taken movie details like `name`, `rating`, `genre`, and `score`.
- Added a column of **ID** to assign each movie a id.
- Converts **categorical ratings** into numerical values:
  - `R` = 5
  - `PG-13` = 4
  - `PG` = 3
  - `G` = 1
  - `Not Rated` = 0
  - **All other ratings** = 2 (default)
- Uses **KNN (K-Nearest Neighbors)** for movie recommendations.
- **Handles invalid inputs**:
  - **Negative IDs** → Converted to positive.
  - **IDs > 1000** → Adjusted using modulus (`% 1000`).
  - **Invalid mood input** → Defaults to "Neutral".

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.8+** and the following dependencies installed:
```bash
pip install pandas scikit-learn
```

### Dataset
- Download a **movie dataset** from **Kaggle** and save it as `your_dataset.csv`.
- Ensure it contains columns: `name`, `rating`, `genre`, `score`.

### Running the Program
1. Place the dataset in the same directory as `main.py`.
2. Run the script:
```bash
python main.py
```

## How It Works
1. Loads and preprocesses the **first 1000 movies** from the dataset.
2. Builds a **User-Movie matrix** for recommendations.
3. Prompts the user to enter a **Movie ID**.
4. Asks the user: **"How's your mood?"** (Positive, Negative, Neutral).
5. Adjusts recommendations based on the user's mood.

## Example Usage
### **Input 1:**
```
Enter user index (movie ID) to get recommendations: -45
How's your mood? (Enter Positive, Negative, or Neutral): Positive
```

### **Adjusted Input & Output:**
```
User 45 has a positive sentiment. Recommending movies with positive ratings...
Recommended movies for User 45:
 - Movie A
 - Movie B
 - Movie C
```
(_Negative ID `-45` was converted to `45` automatically._)





