def count_vowels(word):
    count = 0

    word = "education"

    for letter in word:
        if letter in "aeiou":
          count += 1

    return count

result = count_vowels("education")
print(result)

