def get_word_count(f):
    try:
        with open(f,'r') as file:
            content = file.read().replace("\n"," ").replace("  "," ").replace("  "," ").replace("  "," ")
            wordcount = len(content.split())
            print(f'Word count of file: {wordcount}')
    except FileNotFoundError:
        print(f"Error: The file '{f}' was not found.")
get_word_count("sample.txt")

def comp_strings(l):
    Len = len(l)#-1
    with open('output.txt', 'w') as file:
        
        for i in range(Len):
            content = f'{l[i]}'
            nl = '\n' if i < Len-1 else ''
            file.write(content+nl)
        print(file.read())

comp_strings(["abcd1234","☺☺☺☺"])