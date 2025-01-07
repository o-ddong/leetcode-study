"""
TC - O(n)
    ㄴ 주어진 배열을 끝까지 탐색하므로 O(n * k log k)이라고 생각합니다.
SC - O(1)
    ㄴ 추가적으로 사용하는 공간이 O(n(리스트) * k(튜플))이라고 생각합니다.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for string in strs:
            key = tuple(sorted(string))

            if key not in anagram:
                anagram[key] = []
            
            anagram[key].append(string)

        return list(anagram.values())
