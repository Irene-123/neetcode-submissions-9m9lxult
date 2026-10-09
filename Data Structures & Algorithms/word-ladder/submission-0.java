

class Solution {
    public static boolean hasExactlyOneCharDifference(String s, String t) {
        if (s == null || t == null || s.length() != t.length()) {
            return false;
        }

        int diffCount = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != t.charAt(i)) {
                diffCount++;
                if (diffCount > 1) {
                    return false;
                }
            }
        }

        return diffCount == 1;
    }

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) {
            return 0;
        }

        Map<String, List<String>> map = new HashMap<>();

        record Item(String s, int w) {}

        Set<String> visited = new HashSet<>();

        // Build the graph using wordList
        for (int i = 0; i < wordList.size(); i++) {
            for (int j = i + 1; j < wordList.size(); j++) {
                String s = wordList.get(i);
                String t = wordList.get(j);

                if (hasExactlyOneCharDifference(s, t)) {
                    map.computeIfAbsent(s, k -> new ArrayList<>()).add(t);
                    map.computeIfAbsent(t, k -> new ArrayList<>()).add(s);
                }
            }
        }

        // Connect beginWord to words in wordList
        for (String word : wordList) {
            if (hasExactlyOneCharDifference(beginWord, word)) {
                map.computeIfAbsent(beginWord, k -> new ArrayList<>()).add(word);
                map.computeIfAbsent(word, k -> new ArrayList<>()).add(beginWord);
            }
        }

        // BFS
        Queue<Item> queue = new ArrayDeque<>();
        queue.add(new Item(beginWord, 1));
        visited.add(beginWord);

        while (!queue.isEmpty()) {
            Item item = queue.poll();

            if (item.s().equals(endWord)) {
                return item.w();
            }

            for (String nextString : map.getOrDefault(item.s(), List.of())) {
                if (visited.contains(nextString)) {
                    continue;
                }

                visited.add(nextString);
                queue.add(new Item(nextString, item.w() + 1));
            }
        }

        return 0;
    }
}
