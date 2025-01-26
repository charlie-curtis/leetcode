class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:

        for i,li in enumerate(events):
            type,time,other = li
            tmp = []
            if type == "MESSAGE":
                tmp.append(1)
            else:
                tmp.append(0)
            tmp.append(int(time))
            if type == "MESSAGE":
                if other in ["ALL", "HERE"]:
                    tmp.append(other)
                else:
                    ids = other.split(" ")
                    tmp.append([int(x[2:]) for x in ids])
            else:
                tmp.append(int(other))

            events[i] = tmp
        
        events.sort(key= lambda x: (x[1], x[0]))
        offlineTime = [0]*n

        out = [0]*n
        for type, time, other in events:
            if type == 1:
                message = other
                if message == "ALL":
                    for i in range(n):
                        out[i]+=1
                elif message == "HERE":
                    for i in range(n):
                        if offlineTime[i] <= time:
                            out[i]+=1
                else:
                    users = other
                    for i in users:
                        out[i]+=1
            else:
                id = other
                offlineTime[id] = time + 60
        return out
