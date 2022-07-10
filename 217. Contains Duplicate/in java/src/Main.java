import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int arr[] = {1, 2, 3, 0,5,4};
        MERGE_SORT(arr, 0, arr.length);
        System.out.println(Arrays.toString(arr));

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
    public static void MERGE_SORT(int[] arr, int p, int r){
        if (p < r){
           int q = ((p + r)/2);
           MERGE_SORT(arr, p, q);
           MERGE_SORT(arr, q + 1, r);
           MERGE(arr, p ,q, r);
        }

    }
    public static void MERGE(int arr[], int p, int q, int r){
        int n1 = q -p + 1;
        int n2 = r - q;
        int left[] = {n1 + 1};
        int right[] = {n2 + 1};
        left[n1] = Integer.MAX_VALUE;
        right[n2] = Integer.MAX_VALUE;
        int i = 0, j = 0;
        for (int k = p; k < r; k++) {
            if (left[i] <= right[j]){
                arr[k] = left[i];
                i++;
            }else {
                arr[k] = right[j];
                j++;
            }

        }
    }

}
