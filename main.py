from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # 지금까지 나온 숫자들을 저장할 딕셔너리
    num_dict = {}

    for i in range(len(nums)):
        num = nums[i]
        diff = target - num

        # 만약 차이가 이미 나온 숫자라면 정답
        if diff in num_dict:
            return [num_dict[diff], i]

        # 아직 정답이 아니면 딕셔너리에 저장
        num_dict[num] = i

    # 문제 조건상 무조건 정답이 있다고 했음
    return []


