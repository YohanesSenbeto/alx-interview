#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened or not.

        Args:
                boxes (list): A list of lists where each sublist represents a box and
                                      contains the indices of the boxes it can unlock.
                                          '''
    length = len(boxes)
    opened_boxes = {0}  # Start with the first box opened
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        opened_boxes.add(key)
        keys.update(set(boxes[key]) - opened_boxes)

        result = len(opened_boxes) == length
        print(result)

        if __name__ == "__main__":

            boxes1 = [[1], [2], [3], [4], []]
            canUnlockAll(boxes1)

            boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
            canUnlockAll(boxes2)

            boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
            canUnlockAll(boxes3)
