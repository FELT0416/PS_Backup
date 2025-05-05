    import java.io.*;
    import java.util.*;

    public class Main {
        public static void main(String[] args) throws IOException {
            Scanner sc = new Scanner(System.in);
            int num = sc.nextInt();


            int check = 1;
            int count = 1;
            int step = 6;

            while (check < num) {
                check += step;
                step += 6;
                count++;
            }

            System.out.println(count);

        }


    }
