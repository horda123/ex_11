

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(index):
        a = self,scores[index]
        if a < 50: return "F"
        elif a < 60: return "E"
        elif a < 70: return "D"
        elif a < 80: return "C"
        elif a < 90: return "B"
        else: return "A"

    def find(self,score):
        copy = self.scores[:]
        i = 0
        while i < len(copy):
            a = 0
            flag = False
            while a < (len(copy) - 1 - i):
                if copy[a] > copy[a + 1]:
                    copy[a], copy[a + 1] = copy[a + 1], copy[a]
                    flag = True
                a += 1
            i += 1
            if flag == False: return copy
        return copy

results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

print(results.count())          # 9
print(results.get_by_index(2))  # 91
print(results.scores)           # [85, 42, 91, 67, 50, 73, 100, 38, 58]

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []
    print(results.count())
    for i, body, znamka in StudentsGrades:
        print(f"Student {i} ziskal {body} znamka {znamka}")
    return None

if __name__ == "__main__":
    main()