public class Program{
    public static void main (String args[])
    {   
        for(String str: args)
            System.out.println(str);
        if(GameLogic.checkARGS(args)) System.exit(1);
        KeyGenerator random = new KeyGenerator();
        String pcMove=random.generatePCmove(args);
        random.generateHMAC();
        String HMAC = random.getHMAC();
        System.out.println("HMAC: "+HMAC);

        int option = GameLogic.getOption(args);
        while(option==-1){
            System.out.println(OptionsTable.createTable(args));            
            option = GameLogic.getOption(args);
        }
        if(option == 0) System.exit(0);
        String userMove = args[option-1]; 
        System.out.println("Your move: "+ userMove);
        System.out.println("PC move: "+ pcMove);

        int result = GameLogic.compareMoves(args, userMove, pcMove);
        if(result == 1) System.out.println("You win :)");
        else if(result == -1) System.out.println("You lose :-(");
        else System.out.println("Draw :-|");
        
        System.out.println("Key: "+random.getKey());    
    }
}