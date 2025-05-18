import java.util.Scanner;

public class Main {
    public static int cho (int[] value ){
        Scanner scanner = new Scanner(System.in);

        int endCho = (int)(value[0]*13+value[1]*7+value[2]*5+value[3]*3+value[4]*3+value[5]*2);

        return endCho;
    }
    public static double han (double[] value){
        Scanner scanner = new Scanner(System.in);

        double endHan = (double)(value[0]*13+value[1]*7+value[2]*5+value[3]*3+value[4]*3+value[5]*2+1.5);

        return endHan;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] choValue = new int[6];
        double[] hanValue = new double[6];
        for (int i=0; i<choValue.length; i++){
            choValue[i] = scanner.nextInt();
        }
        for (int i=0; i<hanValue.length; i++){
            hanValue[i] = scanner.nextInt();
        }
        int choResult = cho(choValue);
        double hanResult = han(hanValue);
        String choWin = "cocjr0208";
        String hanWin = "ekwoo";
        if(choResult>hanResult){
            System.out.println(choWin);
        }else {
            System.out.println(hanWin);
        }

    }
}