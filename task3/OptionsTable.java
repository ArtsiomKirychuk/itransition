import com.jakewharton.fliptables.FlipTable;


public class OptionsTable {
    
    public static String createTable(String [] options){
        String [] headers = new String[options.length+1];
        String [][] data = new String [options.length][options.length+1];
        headers[0] = "PC\\User";
        for(int i = 1; i <headers.length;i++ ){
            headers[i] = options[i-1];
            data[i-1][0] = options[i-1];
        }
        for(int i = 0;i<options.length;i++)
            for(int j = 1; j< options.length+1;j++){
                int compare = GameLogic.compareMoves(options,headers[j],data[i][0]);
                if(compare == 1) data[i][j] = "WIN";
                else if(compare == 0)data[i][j]="DRAW";
                else data[i][j] ="LOSE";
            }
        return FlipTable.of(headers, data);
    }     
}
