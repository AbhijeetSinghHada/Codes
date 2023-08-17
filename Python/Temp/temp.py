class ListNode:
    def _init_(self, val, next):
        self.val = val
        self.next = next


def findCriticalPointsDistances(head):
    critical_points = []
    current = head

    # Find local minima and maxima
    while current and current.next:
        if (current.next.val > current.val and current.next.val > current.next.next.val) or \
           (current.next.val < current.val and current.next.val < current.next.next.val):
            critical_points.append(current)

        current = current.next

    if len(critical_points) < 2:
        return [-1, -1]

    min_distance = float('inf')
    max_distance = 0

    # Calculate distances between critical points
    for i in range(len(critical_points) - 1):
        distance = abs(critical_points[i + 1].val - critical_points[i].val)
        min_distance = min(min_distance, distance)
        max_distance = max(max_distance, distance)

    return [min_distance, max_distance]


# Example usage:
# Example 1
head1 = ListNode(3, next=None)
result1 = findCriticalPointsDistances(head1)
print(result1)  # Output: [-1, -1]

# Example 2
head2 = ListNode(5, ListNode(3, ListNode(
    1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))
result2 = findCriticalPointsDistances(head2)
print(result2)  # Output: [1, 3]
