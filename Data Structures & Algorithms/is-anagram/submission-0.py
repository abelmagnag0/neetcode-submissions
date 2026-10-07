class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sOrdened = "".join(sorted(s))
        tOrdened = "".join(sorted(t))

        if len(sOrdened) != len(tOrdened):
            return False

        if sOrdened == tOrdened:
            return True

        return False