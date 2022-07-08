import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int arr[] = {1, 2, 3, 5,4};
        System.out.println(containsDuplicate(arr));

    }

    public static boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int y;
        for (int i =0; i < nums.length -1 ; i++){
            y = i + 1;
            if (nums[i] == nums[y])
                return true;
        }
        return false;
    }

}
