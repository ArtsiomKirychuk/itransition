import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;


public class GameLogic {
   
    public  static int compareMoves(String[] options, String a, String b){  
        int numberOfmoves = options.length;  
        boolean win = false;
        int index = Arrays.asList(options).indexOf(a)+1; 
        String [] cycleMoves = new String[2*numberOfmoves];
        for(int i = 0; i < 2*numberOfmoves;i++) cycleMoves[i] = options[i%numberOfmoves];
        for(int i =index; i < index+numberOfmoves/2; i++)
            if(cycleMoves[i].equals(b)){ win=true; break;}
            else win = false;
        if(a==b) return 0;
        else return win?1:-1;
    }
    
    public static void printMenu(String [] options){
        System.out.flush();
        System.out.println("Available moves");
        for(int i = 0 ; i < options.length; i++)
            System.out.format("%d - %s\n", i+1, options[i]);
        System.out.println("0 - exit");
        System.out.println("? - help");
        System.out.print("Enter your move: " );
    }  

    public static int getOption(String[]options){
        String option;
        int numberOfMoves = options.length;
        int num = -1;
        boolean valid = false;
        Scanner sc = new Scanner(System.in);
        while(valid == false){
            printMenu(options);
            option = sc.nextLine();
            try{
                num = Integer.parseInt(option);
                if(num >= 0 && num <= numberOfMoves) valid = true;
            }
            catch(NumberFormatException e){}
            if(option.equals("?")) valid = true;
        }
        return num;
    }
    
    public static boolean checkARGS(String[] args){        
        HashSet<String> argsUniq = new HashSet<String>();
        for (String s: args) argsUniq.add(s);

        boolean shutdown = false;
        if(args.length == 0){
            shutdown = true;
            System.out.println("no arguments");
        }
        if(args.length == 1){
            shutdown = true;
            System.out.println("number of moves must be >=3 ");
        }
        if(args.length %2 == 0){
            shutdown = true;
            System.out.println("even number of moves([m1,m2,m3], [m1,m2,m3,m4,m5)");

        }
        if(argsUniq.size() != args.length){
            shutdown = true;
            System.out.println("repetitive moves (1 2 3)");
        }   
        return shutdown;           
    }    
}
