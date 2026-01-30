class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()      # Keeps track of visited rooms
        queue = [0]          # Start from room 0

        while queue:
            room = queue.pop(0)

            # Skip already visited rooms
            if room in visited:
                continue

            visited.add(room)

            # Add all keys found in this room
            for key in rooms[room]:
                queue.append(key)

        # Check if all rooms are visited
        return len(visited) == len(rooms)
