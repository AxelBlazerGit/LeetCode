class Solution:
    
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        now=min(x for x,y in tasks)
        tasks = [(ptime, i, etime) for i, (etime, ptime) in enumerate(tasks)]
        order=[]
        n=len(tasks)
        heapq.heapify(tasks)
        
        wait=[]
        
        while len(order)!=n:
            temp=len(order)
            # if wait:
                # w=HP(wait)
                # print("wait heap: ",end="")
                # w.show()
            # else:
                # print(f"wait={wait}")
            if not tasks:
                tasks=[(p,i,e) for e,p,i in wait]
                wait=[]
                heapq.heapify(tasks)
                now=min(e for p,i,e in tasks)
            ptime,i,etime=heapq.heappop(tasks)
            # print(f"ptime={ptime} i={i} etime={etime} now={now}")
            if etime>now:
                # print(f"etime={etime} > now={now}")
                heapq.heappush(wait,(etime,ptime,i))
                # print(f"pushing ({etime},{ptime},{i}) (epi) into wait")
            else:
                # print(f"we are doing task {i}")
                now+=ptime
                order.append(i)
                # og.remove([ptime,i,etime])
                # for p,i,e in og:
                    # print(f"[{p},{i},{e}]",end="\t")
                # print("\n")
                # print("order: " , order)
                while wait and wait[0][0]<=now:
                    e,p,idx=heapq.heappop(wait)
                    # print(f"top of wait is: {e} {p} {idx}")
                    heapq.heappush(tasks,(p,idx,e))
            # if len(order)==temp:
                # print("nothign pushed")
                # now=min(e for e,p,i in wait)
                # tasks=[(p,i,e) for e,p,i in wait]
                # heapq.heapify(tasks)
                # wait=[]
            # print("\n\nloopover\n\n")
        return order
