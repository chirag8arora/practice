package TechPuppies;

import java.util.ArrayList;

/**
 * Created by Xin on 5/29/2014.
 */
public class MinimumWindowSubstring {
    public boolean updateM(Integer[] m, String T, char c, int index) {
        // make sure there is no "not found" situation
        if (T.indexOf(c) == -1) return false;
        int startIndex = 0;
        int minCinSindex = Integer.MAX_VALUE;
        int minCinTindex = Integer.MAX_VALUE;
        while (T.indexOf(c, startIndex) >= 0) {
            int updateIndex = T.indexOf(c, startIndex);
            if (m[updateIndex] == null) {
                // update this
                m[updateIndex] = index;
                return true; // update successfully
            } else {
                // try next
                if (m[updateIndex] < minCinSindex) {
                    minCinSindex = m[updateIndex];
                    minCinTindex = updateIndex;
                }
            }
        }
        m[minCinTindex] = index;
        return true;
    }

    public String minWindow(String S, String T) {
        Integer[] m = new Integer[T.length()];

    }

    public static void main(String[] args) {
        MinimumWindowSubstring m = new MinimumWindowSubstring();
        System.out.println(m.minWindow("ADOBECODEBANC", "ABC"));
        System.out.println(m.minWindow("aa", "aa"));
    }
}
