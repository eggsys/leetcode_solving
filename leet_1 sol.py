from typing import List
class Solution:
    #boxes = [1,3,2,2,2,3,4,3,1]
    boxes = [1,3,3,4,3,1]

    def __init__(self) -> None:
        self.removeBoxes(self.boxes)
    
    def removeBoxes(self, boxes: List[int]) -> int:
       


        while True :
            print("Current boxes ", boxes)
            con_box = []
            for i in range(len(boxes)-1):
                if(boxes[i] == boxes[i+1]):
                    print("President {}:{} ==> {}:{}".format( i, i + 1 , boxes[i], boxes[i+1]))

                    con_box = self.isExist(con_box, i)
                    con_box = self.isExist(con_box, i+1)              


            res_list = self.popout(boxes[i], boxes)                      
            print("[con_box] =>", con_box)
            result = self.score_box(con_box)        
            print("+ score :", result)
            print("+ res list :",res_list)
            print("========================")

            boxes = res_list

      

    def isContinuous(self,index_a, index_b) -> int:
        print(index_a, index_b)
        if(index_a == index_b):
            print(index_a, " ==", index_b)



    def popout(self, rm_num:int, boxes: List[int] )-> None:
        print("RM_NUM :", rm_num)
        print("RM", boxes[rm_num])
        result_list  = list(filter((boxes[rm_num]).__ne__, boxes))
        return result_list

    def isExist(self, list:List[int], index):
        if list == None:
            list = []       

        if(index in list):
            print("PASS")
            pass
        else:
            list.append(index)
            #print(list)

        return list

    def score_box(self, input_no):
        con_count =len(input_no)
        print("score cal :", con_count, "*", con_count)
        score = con_count * con_count
        return score
        
        
        





if __name__ == "__main__":
    Solution()