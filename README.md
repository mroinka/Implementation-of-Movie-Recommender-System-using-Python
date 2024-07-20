# Implementation-of-Movie-Recommender-System-using-Python
This repository contains a simple movie recommendation system based on user inputs for age, gender, and movie type preferences. The system uses these inputs to recommend a suitable movie.

Project of fundamental programming

Overview
The recommendation system utilizes three primary input features:

Age (feature1): The user's age.
Gender (feature2): The user's gender, represented by 'M' for male and 'F' for female.
Movie Type (feature3): The type of movie the user is interested in, represented by 'I' for type "I" or 'II' for type "II".
The system checks the values of these features and recommends a movie based on predefined criteria.

Features
feature1 (Age):

Defines the age range of the user.
Age ranges: 0-16, 16-35, 35 and above.
feature2 (Gender):

Specifies the gender of the user.
Options: 'M' (Male), 'F' (Female).
feature3 (Movie Type):

Indicates the type of movie the user prefers.
Options: 'I', 'II'.
Recommendation Logic
The logic for recommending movies is based on nested if-else statements. Here’s how the system works:

It first checks the age range of the user.
Based on the age range, it then checks the user's gender and movie type preferences.
Depending on the combination of these features, the system recommends a movie.
Examples
If the user's age is between 16 and 35, gender is 'M', and movie type is 'II', the system recommends the movie "Peaky Blinders".
If the user's age is between 0 and 16, gender is 'F', and movie type is 'I', the system recommends the movie "Frozen".
If the combination of features does not match any predefined criteria, the system prints an error message.

Conclusion
This simple movie recommendation system demonstrates the basic principles of a recommendation algorithm. While it uses a limited dataset and straightforward logic, a real-world application would involve a more extensive database of movies and more sophisticated recommendation algorithms to provide accurate and personalized suggestions.

Reviewer: Morteza Karimi
Instructor: Dr. Maryam Bajelan


