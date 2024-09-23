import random

# Συνάρτηση που ζητάει από τον χρήστη να δώσει δύο αριθμούς (όρια)
def get_range():
    while True:
        try:
            lower_bound = float(input("Δώσε το κατώτερο όριο: "))
            upper_bound = float(input("Δώσε το ανώτερο όριο: "))
            if lower_bound > upper_bound:
                print("Το κατώτερο όριο πρέπει να είναι μικρότερο ή ίσο με το ανώτερο όριο.")
            else:
                return lower_bound, upper_bound
        except ValueError:
            print("Παρακαλώ δώσε έγκυρους αριθμούς.")

# Συνάρτηση που εκτελεί και εμφανίζει τις πράξεις
def calculate(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    try:
        division = num1 / num2
    except ZeroDivisionError:
        division = None

    # Εμφάνιση των αποτελεσμάτων
    print("\nΑποτελέσματα:")
    print(f"Άθροισμα: {num1} + {num2} = {addition}")
    print(f"Αφαίρεση: {num1} - {num2} = {subtraction}")
    print(f"Πολλαπλασιασμός: {num1} * {num2} = {multiplication}")

    if division is not None:
        print(f"Διαίρεση: {num1} / {num2} = {division}")
    else:
        print("Δεν είναι δυνατή η διαίρεση με το μηδέν.")

# Κύρια συνάρτηση
def main():
    print("Πρόγραμμα αριθμητικών πράξεων")

    # Ζήτηση του διαστήματος από τον χρήστη
    lower_bound, upper_bound = get_range()

    # Επιλογή τυχαίου αριθμού στο διάστημα που έδωσε ο χρήστης
    random_num1 = random.uniform(lower_bound, upper_bound)
    random_num2 = random.uniform(lower_bound, upper_bound)

    print(f"\nΤυχαίοι αριθμοί που επιλέχθηκαν: {random_num1} και {random_num2}")

    # Εκτέλεση των πράξεων
    calculate(random_num1, random_num2)

# Εκτέλεση του προγράμματος
if __name__ == "__main__":
    main()
