# kris-kringle
A simple python app to generate Kris Kringle

# What I learnt
How to send emails via python
Derangements are quite complex

# How to use
1. First you must create a Gmail account for development
  * If you choose to use another email you need to search for their SMTPlib port number and edit line 57 appropriately
2. Turn "Allow less secure apps to ON" 
  * This can be accessed in your account settings
  * Note it reduces security for your account hence why you create a development account
3. Create a contacts.txt file with each line with the following syntax "friends-first-name friends-email@email.com"
4. Go to your terminal run script with "python3 kriskringle.py"
5. Enter in the password of your email

Note. The script generates a results.txt file. If someone doesn't receive the email you may get someone to check the file and let them know who their kris kringle is. This file has all the spoilers.
