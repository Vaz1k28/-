def total_votes(input_file, output_file):
    from collections import defaultdict

    votes = defaultdict(int)

    with open(input_file, 'r') as file:
        for line in file:
            candidate, vote_count = line.split()
            vote_count = int(vote_count)
            votes[candidate] += vote_count

    sorted_votes = sorted(votes.keys())

    with open(output_file, 'w') as file:
        for candidate in sorted_votes:
            file.write(f"{candidate} {votes[candidate]}\n")

input_file = "input.txt"
output_file = "output.txt"


input_data = """McCain 10
McCain 5
Obama 9
Obama 8
McCain 1"""


with open(input_file, 'w') as file:
    file.write(input_data)


total_votes(input_file, output_file)


with open(output_file, 'r') as file:
    print(file.read())
