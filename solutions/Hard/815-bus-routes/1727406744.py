class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:


        if source == target:
            return 0
        #buses are vertices
        #any buses that have the same stops will have an edge between them
        #do a breadth-first search. All the nodes that are initially queued are any of the buses
        #that service the source route
        #any of the destination nodes are the ones that service the target route

        #for each node, it's connected buses are the ones that share any of the same routes


        #note, everywhere that I used "route" should actually be "bus_stop"
        routes_to_buses = defaultdict(set)
        buses_to_routes = defaultdict(set)
        q = deque()
        good_buses = set()

        seen_routes = set()
        seen_buses = set()

        for bus,li in enumerate(routes):

            for r in li:
                routes_to_buses[r].add(bus)
                buses_to_routes[bus].add(r)
                if r == source:
                    q.append([bus,0])
                    seen_buses.add(bus)
                    seen_routes.add(r)
                if target == r:
                    good_buses.add(bus)


        #print(q)
        while q:
            bus, steps = q.popleft()

            steps+=1

            if bus in good_buses:
                return steps
            
            #iterate over all the routes this bus takes
            for r in buses_to_routes[bus]:
                if r in seen_routes:
                    continue
                seen_routes.add(r)
                #iterate over all the buses for this route
                for nxt_bus in routes_to_buses[r]:
                    if nxt_bus in seen_buses:
                        continue
                    seen_buses.add(nxt_bus)
                    q.append([nxt_bus, steps])


        return -1



        




        