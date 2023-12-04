with open('preproinsulin-seq.txt', 'r') as file:
    text = file.read();
#print(text);

lines = text.split('/n');
#print(lines);

filtered_lines = [line for line in lines[1:-1] if line.strip()]
print(filtered_lines);
print(lines[0])