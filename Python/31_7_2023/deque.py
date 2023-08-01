from collections import deque

friends = deque(('Rolf','Charlie','Jen','Anna'))

friends.append('Jose')
friends.appendleft('Anthony')

print(friends)
friends.pop()
print(friends)
friends.popleft()
print(friends)