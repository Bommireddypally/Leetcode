# Definition for a binary tree node.
import heapq
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        if root is None :
            return
        list=[]
        stack=[]
        stack.append([0,0,root])
        hash={}
        result=[]
        while stack:
            len_=len(stack)
            for i in range(len_):
                col,row,node=stack.pop(0)
                heapq.heappush(list,[col,row,node.val])
                if col not in hash:
                    hash[col]=1
                else:
                    hash[col]+=1
                if node.left:
                    stack.append([col-1,row+1,node.left])
                if node.right:
                    stack.append([col+1,row+1,node.right])
        while list:
            col,row,node=heapq.heappop(list)
            len_=hash[col]
            lisit2=[node]
            for i in range(len_-1):
                col,row,node=heapq.heappop(list)
                lisit2.append(node)
            result.append(lisit2)
        return result

                

        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
