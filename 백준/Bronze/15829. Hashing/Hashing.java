    import java.io.*;
    import java.util.*;
    public class Main {
        public static void main(String[] args) throws IOException {
            Scanner sc = new Scanner(System.in);
            int len = Integer.parseInt(sc.nextLine());
            int[] chars = new int[len];
            String str = sc.nextLine();
            for (int i = 0; i < len; i++) {
                chars[i] = (int)str.charAt(i)-96;
            }
            int times = 0;
            double hash =0;
            for (int toHash:chars){
                double toMult = 1;
                 for (int i = 0; i < times; i++) {
                     toMult *= 31;
                     toMult %=1234567891;
                 }
                 hash+=toMult*toHash;
                 times++;
            }
            hash%=1234567891;
            System.out.println((int)hash);
        }
    }
