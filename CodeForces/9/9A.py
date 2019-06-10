x = list(map(int, input().split()))
# She wins if she gets a number equal to or higher than the highest number they've got
prob = (6 - max(x) + 1) / 6

probs = {1/6: '1/6', 1/3: '1/3', 1/2: '1/2', 2/3: '2/3', 5/6: '5/6', 1: '1/1'}

for i in probs:
    if prob == i:
        print(probs[i])
        break
