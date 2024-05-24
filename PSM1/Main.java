import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to Sine Calculator");
        System.out.println("===========================");
        System.out.print("Enter the value of x in radians: ");
        double x = scanner.nextDouble();


        double precision = x * Math.PI / 180.0;

        double sineApprox1 = computeSin(precision);
        double sineApprox = computeSine(x);

        System.out.println("\nResult:");
        System.out.println("-------");
        System.out.printf("sin(%.2f) ≈ %.11f\n", x, sineApprox1);
        System.out.printf("sin(%.2f) ≈ %.11f\n", x, sineApprox);

        scanner.close();
    }

    public static double computeSin(double x) {
        double sine = 0;
        int precision = 10;
        for (int i = 0; i < precision; i++) {
            double term = Math.pow(-1, i) * Math.pow(x, 2 * i + 1) / factorial(2 * i + 1);
            sine += term;
        }
        return sine;
    }
    public static double computeSine(double x) {
        double sine = 0;
        int precision = 10;

        x = x % (2 * Math.PI);
        for (int i = 0; i < precision; i++) {
            double term = Math.pow(-1, i) * Math.pow(x, 2 * i + 1) / factorial(2 * i + 1);
            sine += term;
        }
        return sine;
    }

    private static long factorial(int number) {
        if (number <= 1)
            return 1;
        else
            return number * factorial(number - 1);
    }
}
