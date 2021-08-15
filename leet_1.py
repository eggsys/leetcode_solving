from typing import List
class Solution:
    boxes = [1,3,2,2,2,3,4,3,1]

    def __init__(self) -> None:
        self.removeBoxes(self.boxes)
    
    def removeBoxes(self, boxes: List[int]) -> int:
        result = boxes.index(3)
        count_result = boxes.count(1)
        print(result)
        print("count_result ", count_result)

        tmp_1 = ''
        tmp_2 = ''
        i = 0
        pop_list = []
        print("LEN :", len(boxes) - 1)
        print("start loop")
        for x in boxes :
            if(i < len(boxes) - 1):
                #print("I =",i)
                tmp_1 = boxes[i]
                tmp_2 = boxes[i+1] 

                if(tmp_1 == tmp_2):
                    status = '[/] Pos',i, i+1
                    print(" !!pop", tmp_1)
                    print(" !!pop", tmp_2)
                    
                    #boxes.remove(tmp_1)
                    #boxes.remove(tmp_2)
                    pop_list.append(i)
                    pop_list.append(i+1)


                else:
                    status = '[X]'

                print(tmp_1, tmp_2, status)
                
                

                i = i + 1
        print(boxes)
        print("pop list : ",pop_list)

        

        x = list(filter((2).__ne__, boxes))
        print("x list ::", x)
        
        #for x in pop_list:
            
        #    print("index : ",x,"remove ", boxes[x])
        #    boxes.remove(boxes[x])
            #print("UPDATE :>", boxes)
        #    
        
        print(boxes)

        
        
        

s = Solution()