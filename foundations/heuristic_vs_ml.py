# Our training examples: (study hours, result: 1 for Pass, 0 for Fail)
data = [
    (1.0, 0),
    (2.0, 0),
    (3.0, 0),
    (4.5, 1),
    (6.0, 1),
    (8.0, 1),
]

print("--- 1. Regular Human Rule ---")
# Human manually assumed 5.0 hours is the passing mark
human_threshold = 5.0

def human_predict(hours):
    return 1 if hours >= human_threshold else 0

# Test how many mistakes the human rule makes
mistakes = 0
for hours, actual_result in data:
    prediction = human_predict(hours)
    if prediction != actual_result:
        mistakes += 1
        print(f"Human rule failed for {hours} hours (predicted {prediction}, actual was {actual_result})")

print(f"Total mistakes by human rule: {mistakes}")

print("\n--- 2. Machine Learning (Finds the rule from data) ---")

best_threshold = 0.0
lowest_mistakes = 9999

# The computer tries every cutoff from 0.0 to 10.0 in steps of 0.5
test_cuts = [i * 0.5 for i in range(21)]

for cut in test_cuts:
    mistakes_with_this_cut = 0
    for hours, actual_result in data:
        prediction = 1 if hours >= cut else 0
        if prediction != actual_result:
            mistakes_with_this_cut += 1

    # Keep track of the cutoff that made the fewest mistakes
    if mistakes_with_this_cut < lowest_mistakes:
        lowest_mistakes = mistakes_with_this_cut
        best_threshold = cut

print(f"The computer found the best passing cutoff: {best_threshold} hours")
print(f"Total mistakes by machine learned rule: {lowest_mistakes}")
