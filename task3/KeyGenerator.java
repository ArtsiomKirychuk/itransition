import java.security.SecureRandom;
import org.bouncycastle.jcajce.provider.digest.*;
import org.bouncycastle.util.encoders.Hex;


public class KeyGenerator{

    private String key="";

    private String HMAC="";

    private String move="";

    public String getHMAC(){return HMAC;}

    public String getKey(){return key;}

    public  KeyGenerator(){
        SecureRandom random = new SecureRandom();
        byte[] bytes = new byte[16];
        random.nextBytes(bytes);
        key = Hex.toHexString(bytes);
    }

    public String generatePCmove(String[] options){
        SecureRandom random =new SecureRandom();
        int randomInt = random.nextInt(options.length);
        move = options[randomInt];
        return move;
    }

    public void generateHMAC(){
        SHA3.Digest256 digestSHA3 = new SHA3.Digest256();
        String movePlusKey = move+key;
        byte[] bytes = digestSHA3.digest(movePlusKey.getBytes());
        HMAC = Hex.toHexString(bytes);     
    }
}