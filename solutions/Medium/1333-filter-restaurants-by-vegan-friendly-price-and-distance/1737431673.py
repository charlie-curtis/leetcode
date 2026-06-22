class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        out = []

        for id,rating,vegan,price,distance in restaurants:
            if veganFriendly and not vegan:
                continue
            if price > maxPrice:
                continue
            if distance > maxDistance:
                continue
            out.append((rating,id))

        out.sort(reverse=True)
        return [x[1] for x in out]
        