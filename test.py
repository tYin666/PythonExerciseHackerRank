if __name__ == '__main__':
    students_data = [];
    scores = [];
    names = [];
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_data.append([name, score])
        scores.append(score)
        names.append(name)
    
    sorted_scores = sorted(scores)
    print(students_data)
    print(scores)
    print(sorted_scores)
    print(names)