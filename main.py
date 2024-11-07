questions = ("What is the capital of France?:",
             "Which planet is known as the Red Planet?:",
             "Who wrote the play 'Romeo and Juliet'?:",
             "What is the chemical symbol for salt?:",
             "Which counrty hosted the 2016 Summer Olympics?:",
             "How many bones in the human body?:",
             "Who painted the famous artwork 'The Starry Night?:",
             "What is the largest ocean on Earth?:",
             "What is the capital of Australia?:",
             "In which year did the Titanic sink?:")

options = (("A. Berlin", "B. London", "C. Paris", "D. Rome"),
           ("A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"),
           ("A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"),
           ("A. CO2", "B. HCl", "C. KCl", "D. NaCl"),
           ("A. China", "B. USA", "C. Brazil", "D. UK"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Claude Monet", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Vincent van Gogh"),
           ("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"),
           ("A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"),
           ("A. 1912", "B. 1913", "C. 1914", "D. 1915"))

answers = ("C", "B", "A", "D", "C", "A", "D", "D", "C", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
  print("----------------------")
  print(question)
  for option in options[question_num]:
    print(option)

  guess = input("Enter (A, B, C, D): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score += 1
    print("CORRECT!")
  else:
    print("INCORRECT!")
    print(f"{answers[question_num]} is the correct answer")
  question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
  print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
  print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")