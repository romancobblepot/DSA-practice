class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False

        # Count frequency of each card
        from collections import Counter
        freq = Counter(hand)
        # Sort card values
        for card in sorted(freq):
            count = freq[card]
            freq[card]-=count
            if count > 0:
                # Try forming a sequence
                for i in range(1, groupSize):
                    if freq[card + i] <count:
                        return False
                    freq[card + i] -=count
        return True