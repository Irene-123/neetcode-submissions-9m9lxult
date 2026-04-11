class Solution {
    public int[] topKFrequent(int[] nums, int k) {

		Map<Integer, Integer> count = new HashMap<>();

		PriorityQueue<Map.Entry<Integer, Integer>> maxHeap = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());

		for (int num: nums){
			count.put(num, count.getOrDefault(num,0)+1);
		}

		maxHeap.addAll(count.entrySet());

		int[] result = new int[k];
		for (int i = 0; i < k; i++) {
			result[i] = maxHeap.poll().getKey();
		}

		return result;



        
    }
}
