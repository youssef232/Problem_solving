import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        int []nums1 = {1,2,2,1};
        int [] nums2 = {2, 2};
        System.out.println(Arrays.toString(intersect(nums1, nums2)));

    }

    public static int[] intersect(int[] nums1, int[] nums2) {
        int [] arr = new int[1001];
        List<Integer> output = new ArrayList<>();
        for (int j : nums1) {
            arr[j]++;
        }
        for(int i : nums2){
            if (arr[i] > 0){
                output.add(i);
                arr[i]--;
            }
        }
        int [] temp = new int[output.size()];
        for (int i = 0; i < output.size(); i++) {
            temp[i] = output.get(i);
        }

        return temp;

    }
}
