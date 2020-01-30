import sys

def solution(command, buttons, scores):
    skills_enable = [x for x in buttons if x in command]#enable skills
    score_list = [len(command)]
    temp = command
    for i, skill in enumerate(skills_enable):
        score = 0
        usable = skills_enable[i:]
        temp = temp.replace(skill, '')
        score += scores[buttons.index(skill)]
        temp2 = temp
        prev = score
        print(temp, skill)

        while usable:
            print(skill, 'in!', usable, score)
            for u in usable:
                if u in temp2:
                    print(temp2, u)
                    temp2 = temp2.replace(u, '')
                    score += scores[buttons.index(u)]
            usable = usable[1:]
            if not usable:
                score += len(temp2)
            temp2 = temp
            if not score in score_list:
                score_list.append(score)
            score = prev
        temp = command
    print(score_list)
    
    answer = max(score_list)
    return answer

if __name__ == '__main__':
	solution("<v>AB^CYv^XAZ", ["v>AB^CYv^XA", "<v>A", "^XAZ", "Yv^XA", ">AB^"], [50, 18, 20, 30, 25])