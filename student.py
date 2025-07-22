class Student:
    def __init__(self, name, math_score, science_score):
        self.name = name
        self.math_score = math_score
        self.science_score = science_score
    def calculate_average(self):
        return(self.math_score + self.science_score)/2

    def display_result(self):
        average = self.calculate_average()
        print(f"nom de l'etudiant : {self.name}")
        print(f"moyenne des notes : {average:.2f}")

#creer un objet de la classe student
etudiant = Student("jodelle", 85, 40)

#appeler la methode display_result()
etudiant.display_result()

