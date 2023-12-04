# filtered_lines = [];
# new_filtered_lines = [];

with open('preproinsulin-seq.txt', 'r') as file:
    text = file.read();

lines = text.split('\n');

# Line 11 is what is known as a List Comprehension
# for line in lines[1:-1]:
#   filtered_lines.append(line);
filtered_lines = [line for line in lines[1:-1] if line.strip()];

# Line 17 is also a List Comprehension
# for line in filtered_lines:
    # new_filtered_lines.append(line.replace('1', '').replace('6', ''));
filtered_lines = [line.replace('1', '').replace('6', '').replace(' ', '').strip() for line in filtered_lines];

result = ('\n'.join(filtered_lines)).replace('\n', '');

# print(len(result));
# print(result);
if len(result) == 110:
    print("Cleaning done");
    with open('preproinsulin-seq-clean.txt', 'w') as output:
        output.write(result);