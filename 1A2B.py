#!/usr/bin/env python
# coding: utf-8

# In[9]:


#黑窗版
import random
from time import sleep

class game_1A2B:
    def __init__(self):
        self.AnswerList = []
        
    #函式區
    def GenerateAnswer(self):
        '''
        抽取出四個數字作為答案
        '''
        source = [0,1,2,3,4,5,6,7,8,9]
        for i in range(4):
            number = (random.randint(0,9)) % len(source)
            answer0 = str(source.pop(number))
            self.AnswerList.append(answer0)
        
        #number = (random.randint(0,9) + number) % len(source)
        #answerB = str(source.pop(number))
        
        #number = (random.randint(0,9) + number) % len(source)
        #answerC = str(source.pop(number))
        
        #number = (random.randint(0,9) + number) % len(source)
        #answerD = str(source.pop(number))
        
        #self.AnswerList.append(answerA)
        #self.AnswerList.append(answerB)
        #self.AnswerList.append(answerC)
        #self.AnswerList.append(answerD)

    def WinnerJudge(self,test):
        '''
        判斷勝利條件達成與否
        output : 1 - 已結束
                 2 - 尚未結束
        '''
        resultA = 0
        resultB = 0
        for i in range(4):
            if test[i] == self.AnswerList[i]:
                resultA += 1
            else:
                if test[i] in self.AnswerList:
                    resultB += 1
        if resultA + resultB > 4:
            print("!ERROR: winORnot ")
        if resultA == 4:
            return 1
        else:
            print("本次結果\t",resultA,"A",resultB,"B")
            return 0
        
    def game_blackwindow(self):
        print('歡迎來玩 1A2B')
        sleep(0.25)
        print('讓我想想四個數字')
        sleep(0.3)
        self.GenerateAnswer()
        print('好的，我想好了。請開始猜吧~\n')
        #print("答案是:",self.AnswerList)
        counter = 0
        while True:
            counter += 1
            print("****************************")
            print('第 ',counter,' 次嘗試')
            input_answer = str(input('只能輸入四個數字\n >>'))
            winKey = self.WinnerJudge(input_answer)
            if winKey == 1:
                break
        print("****************************")
        print('\n==========================================')
        print('太厲害了!! 只花',counter,'次就猜到')
        print("答案是:",self.AnswerList[0],self.AnswerList[1],self.AnswerList[2],self.AnswerList[3])

#主程式區
if __name__ == "__main__":
    box = game_1A2B()
    box.game_blackwindow()


# In[ ]:




