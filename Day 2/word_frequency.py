import string
try:

    with open("sample.txt","r",encoding = 'utf-8') as file:
        text = file.read()

    text = text.translate(str.maketrans("","", string.punctuation))

    text = text.lower()

    words = text.split()


    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    sorted_words = sorted(frequency.items(),key=lambda x: x[1],reverse=True)

    if not words:
        print("No words found in the file.")

    else:
        frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    sorted_words = sorted(
        frequency.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("===== WORD FREQUENCY COUNTER =====")
    print("Top 10 Most Frequent Words:\n")

    for i, (word, count) in enumerate(sorted_words[:10], start=1):
        print(f"{i}. {word}: {count}")
          

except FileNotFoundError:
    print("File not found")
