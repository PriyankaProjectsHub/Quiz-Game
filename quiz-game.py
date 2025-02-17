# Importing the random module to shuffle questions
import random

# Set the initial amount of prize money
prize_money = 0

# Create a list of questions with options and answers
questions = [{
   "question": "What is the capital of India?",
   "options": ["1. Delhi", "2. Mumbai", "3. Kolkata", "4. Chennai"],
   "answer": 1
},{
   "question": "Which planet is known as the Red Planet?",
   "options": ["1. Jupiter", "2. Venus", "3. Mars", "4. Saturn"],
   "answer": 3
},{
   "question": "Who painted the Mona Lisa?",
   "options": ["1. Vincent van Gogh", "2. Pablo Picasso", "3. Leonardo da Vinci", "4. Claude Monet"],
   "answer": 3
}]

# Shuffle the questions
random.shuffle(questions)

# Iterate over the questions using a for loop
for question in questions:
   # Display the question and options
   print(question["question"])
   for option in question["options"]:
      print(option)
    
   # Read the user's answer
   user_answer = int(input("Enter your answer (option number): "))
    
   # Check if the user's answer is correct
   if user_answer == question["answer"]:
      print("Correct answer!")
      prize_money += 1000
   else:
      print("Wrong answer!")
      break  # End the game if the answer is incorrect

# Display the final prize money earned by the player
print("Prize Money:", prize_money)
