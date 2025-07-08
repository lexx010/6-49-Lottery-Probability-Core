import streamlit as st
import pandas as pd


# Load the historical lottery data
df = pd.read_csv(r"C:\Users\wolf0\Documents\data_analys_science\dq\Guided_DS\Probability_lottery\649.csv")

# Extract winning numbers as sets from the relevant columns
def extract_numbers(row):
    return set(row.iloc[4:10].values)

winning_numbers = df.apply(extract_numbers, axis=1)


# Assume combinations and factorial functions already defined
# Also assume winning_numbers is a pandas Series of sets from historical data

def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

def combinations(n, k):
    if k > n:
        raise ValueError("k cannot be greater than n.")
    return factorial(n) // (factorial(k) * factorial(n - k))

def one_ticket_probability():
    total = combinations(49, 6)
    return 1 / total

def multi_ticket_probability(tickets):
    total = combinations(49, 6)
    success = min(tickets, total)
    return success / total

def check_historical_occurrence(user_nums, historical_nums):
    user_set = set(user_nums)
    return historical_nums.apply(lambda x: x == user_set).sum()

st.title("6/49 Lottery Probability & History Checker")

st.header("Enter your 6 unique lottery numbers (1-49):")
numbers = []
cols = st.columns(6)
for i in range(6):
    with cols[i]:
        num = st.number_input(f"Number {i+1}", min_value=1, max_value=49, step=1, key=i)
        numbers.append(num)

# Validate unique numbers
if len(set(numbers)) != 6:
    st.warning("Please enter 6 unique numbers.")
    st.stop()

tickets = st.number_input("Number of different tickets to play:", min_value=1, max_value=13983816, value=1, step=1)

# Calculate probabilities
prob_one = one_ticket_probability()
prob_multi = multi_ticket_probability(tickets)

st.subheader("Probability Results:")
st.write(f"Probability of winning with your single ticket: {prob_one:.8%} (1 in {int(1/prob_one):,})")
st.write(f"Probability of winning with {tickets:,} tickets: {prob_multi:.8%} (1 in {int(1/prob_multi):,})")

# Check historical occurrences — make sure winning_numbers is defined
if 'winning_numbers' in globals():
    occurrences = check_historical_occurrence(numbers, winning_numbers)
    st.subheader("Historical Data Check:")
    st.write(f"Your combination has appeared **{occurrences}** time(s) in the historical Canada lottery data.")
else:
    st.info("Historical lottery data not loaded. Load it as 'winning_numbers' Series of sets to enable this check.")
