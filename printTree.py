# printTree.py
#
# print tree structures on console
#
# example:
#
#                 05                
#   ______________|______________   
#  |              |              |  
#  02             04             06 
#  |    __________|_________        
#  01  |      |     |   |   |       
#      01     02    09  08  02      
#            _|_                    
#           |   |                   
#           03  06
# usage:
#
#  printTree(root,getNodeInfo)
#
#     root:        is the top node of the tree
#     getNodeInfo: is a lambda or function that takes a node and returns a tuple
#                  with the label to print and the list of children
#
#
# For example:
#
#     printTree(root,lambda n:(n.label,n.children))
#
#     Assuming the class is defined as (i.e. has .label and .children attributes):
#
#     class TreeNode:
#        def __init__(self,label,parent=None):
#            self.label    = label
#            self.children = []
#            if parent: parent.children.append(self)


def treeLines(node,getInfo):
    nodeId,nodeChildren = getInfo(node)
    subNodes   = [treeLines(child,getInfo) for child in nodeChildren]
    widths     = [ len(childText[0]) for childText in subNodes ]
    totalWidth = sum(widths) + 2*len(widths) - 1
    totalWidth = max(totalWidth,len(nodeId))
    nodeLine   = nodeId.center(totalWidth," ")
    result     = [nodeLine]
    if not nodeChildren: return result
    linksLine   = "  ".join("|".center(width," ") for width in widths)
    linksLine   = linksLine.center(totalWidth," ")
    leftIndent  = linksLine.index("|") + 1
    rightIndent = linksLine[::-1].index("|") + 1
    spanWidth   = totalWidth - leftIndent - rightIndent - 1
    leftSpan    = nodeLine.index(nodeId)-leftIndent+(len(nodeId)-1)//2
    rightSpan   = spanWidth - leftSpan   
    spanLine    = " "*leftIndent + "_"*leftSpan + "|" + "_"*rightSpan + " "*rightIndent
    if len(nodeChildren) > 1 : result.append(spanLine)
    result.append(linksLine)
    maxHeight   = max(len(subNode) for subNode in subNodes)
    subNodes    = [ subNode + [" "*len(subNode[0])]*(maxHeight-len(subNode)) for subNode in subNodes ]
    result     += ["  ".join([subNode[i] for subNode in subNodes]).center(totalWidth," ") for i in range(maxHeight) ]
    return result  

def printTree(node,getInfo):
    for line in treeLines(node,getInfo):
        print(line)

if __name__ == "__main__":
    
    class TreeNode:
        def __init__(self,label,parent=None):
            self.label    = label
            self.children = []
            if parent: parent.children.append(self)

    root = TreeNode("05")
    n02  = TreeNode("02",root)
    n04  = TreeNode("04",root)
    n06  = TreeNode("06",root)
    TreeNode("01",n02)
    TreeNode("01",n04)
    n02 = TreeNode("02",n04)
    TreeNode("09",n04)
    TreeNode("08",n04)
    TreeNode("02",n04)
    TreeNode("03",n02)
    TreeNode("06",n02)

    printTree(root,lambda n:(n.label,n.children)) 
 
