import java.net.*;
public class IpAddy {
    public static void main(String[] args) {
        try{
            InetAddress ip = InetAddress.getLocalHost();
            System.out.println("IP Address: " + ip.getHostAddress());
        } catch (UnknownHostException e) {
            System.out.println("Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
