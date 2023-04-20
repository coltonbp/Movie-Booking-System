import java.time.Instant;
import java.util.*;
import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;
import java.io.*;
import java.util.Scanner;


public class ViewStock extends ShipOrder
{

    public static void main(String[] args)
        {
        Scanner input = new Scanner(System.in);
        Scanner console = new Scanner(System.in);
        int toolq1=2,toolq2=3,compq1=4,compq2=4;
   
           
       

        
        System.out.print("\nTo request items in stock quantities after order 1 enter (1)"+"\nTo request items in stock quantities after order 2 enter (2)"+"\nAny other key will exit: \n");
        int answer = input.nextInt();
        if (answer == 1) {
            System.out.println("option 1 was choosen"); 
            System.out.println("The stock quantities after order 1"); 
            System.out.println("Remanining TOOL Sets:" + toolq1); 
            System.out.println("Remanining Computers :" + compq1); 
            System.out.println("TOOL Sets Reserved :" + (2)); 
            System.out.println("Computers Reserved:" + (1)); 


           }
        else if  (answer == 2) {
            System.out.println("option 2"); 
            System.out.println("The stock quantities after order 2"); 
            System.out.println("Remanining TOOL Sets:" + toolq2); 
            System.out.println("Remanining Computers :" + compq2); 
            System.out.println("TOOL Sets Reserved :" + (1)); 
            System.out.println("Computers Reserved:" + (1)); 
        }
        else {
            System.out.println(0); 
          }
    
    }


}