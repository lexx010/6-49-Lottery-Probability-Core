# Lottery Probability Calculator & Historical Checker

This project provides Python functions to calculate lottery winning probabilities and check historical lottery data for previous winning combinations. It focuses on the classic 6/49 lottery format.

## Features

* Calculate the probability of winning the jackpot with a single ticket
* Calculate probability of winning when playing multiple tickets
* Calculate probabilities of matching 2, 3, 4, or 5 winning numbers
* Check whether a chosen combination has occurred in historical lottery data (Canada, 1982–2018)
* Functions use efficient combinatorial math and set operations for accuracy and speed

## Getting Started

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/lottery-probability.git
   cd lottery-probability
   ```

2. Install dependencies (if any):

   ```bash
   pip install pandas
   ```

3. Place the historical lottery CSV dataset (`649.csv`) in the project folder.

4. Import and use the provided functions in your Python scripts or notebooks.

## Example Usage

```python
from lottery import one_ticket_probability, check_historical_occurrence

user_numbers = [3, 41, 11, 12, 43, 14]

print("Probability of winning with one ticket:", one_ticket_probability())
print("Number of times combination appeared historically:", check_historical_occurrence(user_numbers, winning_numbers_series))
```

## Data Source

Historical lottery data is from the [Kaggle Lottery Dataset](https://www.kaggle.com/datasets/datascienceai/lottery-dataset).

Sure! Here’s a concise **“Streamlit App”** section you can add to your main README:

---

## Streamlit App

This project includes an interactive Streamlit web app that allows users to:

* Input their 6 unique lottery numbers
* Select the number of tickets to play
* Calculate the probability of winning the big prize
* Check historical occurrence of their numbers in past lottery draws

### How to run the Streamlit app

1. Make sure you have Streamlit installed:

```bash
pip install streamlit pandas
```

2. Ensure the historical data file `649.csv` is in the project folder or update the path in the app code.

3. Run the app with:

```bash
streamlit run app.py
```

4. Your default browser will open the interactive app interface.



