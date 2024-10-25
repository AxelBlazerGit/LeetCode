class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders=set(folders)
        parents=[]
        for folder in folders:
            flag=0
            for i in range(len(folder)):
                if folder[i]=='/':
                    if folder[:i] in folders:
                        flag=1
                        break
            if not flag:
                parents.append(folder)
        return parents
