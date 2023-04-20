import java.util.Scanner;
public class LogOn
{
    int loginv;
    public static void main(String args[])
    {
        String username, password, securityquestion;
        Scanner s = new Scanner(System.in);

        System.out.print("Enter username (correct - Student):");    
        username = s.nextLine();
        System.out.print("Enter password (correct - Tech) :");   
        password = s.nextLine();
        if(username.equals("Student") && password.equals("Tech"))
        {
            System.out.print("Security question - Where is Texas Tech located? (correct - Lubbock) :");   
            securityquestion = s.nextLine();
           if(securityquestion.equals("Lubbock"))
        {
            System.out.println(" Welcome ");
            int loginv =1; // this will help with the preconditions of the next classes
        }
        else
        {
            System.out.println(" Wrong answer ");
        }
        }
        else
        {
            System.out.println("Authentication Failed");
            
        }
        
    }
}