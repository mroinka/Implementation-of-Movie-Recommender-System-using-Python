feature1 = 33  # Age
feature2 = "M"  # Gender
feature3 = "I"  # Movie Type

ages = [0, 16, 35, 50]
gender = ['M', 'F']
m_or_s = ['I', 'II']

def recommend_movie(age, gender, movie_type):
    if ages[0] < age <= ages[1]:
        if gender == gender[0]:
            if movie_type == m_or_s[0]:
                return "Coco"
            elif movie_type == m_or_s[1]:
                return "Stranger Things"
        elif gender == gender[1]:
            if movie_type == m_or_s[0]:
                return "Frozen"
            elif movie_type == m_or_s[1]:
                return "Madrese Moushha"
    elif ages[1] < age <= ages[2]:
        if gender == gender[0]:
            if movie_type == m_or_s[0]:
                return "Fight Club"
            elif movie_type == m_or_s[1]:
                return "Peaky Blinders"
        elif gender == gender[1]:
            if movie_type == m_or_s[0]:
                return "Titanic"
            elif movie_type == m_or_s[1]:
                return "Friends"
    elif ages[2] < age <= ages[3]:
        if gender == gender[0]:
            if movie_type == m_or_s[0]:
                return "It's a Wonderful Life"
            elif movie_type == m_or_s[1]:
                return "Fargo"
        elif gender == gender[1]:
            if movie_type == m_or_s[0]:
                return "Gone with the Wind"
            elif movie_type == m_or_s[1]:
                return "Shahrzad"
    return "Invalid input"

def get_user_input():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                raise ValueError("Age cannot be negative.")
            break
        except ValueError as e:
            print(e)
    
    gender = input("Enter your gender (M/F): ").strip().upper()
    while gender not in ['M', 'F']:
        print("Invalid gender. Please enter 'M' or 'F'.")
        gender = input("Enter your gender (M/F): ").strip().upper()
    
    movie_type = input("Enter your movie type (I/II): ").strip().upper()
    while movie_type not in ['I', 'II']:
        print("Invalid movie type. Please enter 'I' or 'II'.")
        movie_type = input("Enter your movie type (I/II): ").strip().upper()
    
    return age, gender, movie_type

age, gender, movie_type = get_user_input()
recommended_movie = recommend_movie(age, gender, movie_type)
print(f"See {recommended_movie} and enjoy your time.")
