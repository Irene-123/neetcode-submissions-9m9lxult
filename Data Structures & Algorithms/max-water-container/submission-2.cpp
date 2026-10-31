class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n = heights.size();

        int water = 0, temp_area = 0;

        int i = 0, j = n - 1;

        while (i < j) {

            water = max(water, (j-i)*min(heights[i], heights[j]));

            if (heights[i] < heights[j]) {
                i++;
            }
            else {
                j--;
            }
        }

        return water;
    }
};
