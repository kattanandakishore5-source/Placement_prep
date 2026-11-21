import string
try:

    with open("sample.txt","r",encoding = 'utf-8') as file:
        text = file.read()

    text = text.translate(str.maketrans("","", string.punctuation))

    text = text.lower()

    words = text.split()

    if not words:
        print("No words found in the file.")

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    sorted_words = sorted(frequency.items(),key=lambda x: x[1],reverse=True)

    print("===== WORD FREQUENCY COUNTER =====")
    print("Top 10 Most Frequent Words:\n")

    for i in range(min(10,len(sorted_words))):
        word,count = sorted_words[i]
        print(f"{i+1}. {word} : {count}")
          

except FileNotFoundError:
    print("File not found")
