if __name__ == '__main__':
    students_data = []
    scores = []
    names = []
    names_secondLow = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_data.append([name, score])
        scores.append(score)
        names.append(name)
       
    sorted_scores = sorted(scores)
    second_low = 0.0;
    n = len(scores);
    for i in range (n):
        if sorted_scores[i] > sorted_scores[0]:
            second_low = sorted_scores[i]
            break
    ind = scores.index(second_low)
  
    for j in range(ind, n):
        if scores[j] == second_low:
            names_secondLow.append(names[j])   
    
    for k in range(len(sorted(names_secondLow))):
        print(sorted(names_secondLow)[k])