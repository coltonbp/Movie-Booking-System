import java.time.Instant;
import java.util.*;
import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;
import java.io.*;
import java.util.Scanner;

public class Vieworder extends ShipOrder
{

    public static void main(String[] args)
        {
        Scanner input = new Scanner(System.in);
        Scanner console = new Scanner(System.in);
        String statusCode;
        int scost=229,pscost=190,sacost=1500,psacost=1200;
        int TQ=2,CQ=1,TQ2=1,CQ2=1;
      
   
           
       

        
        System.out.print("\nTo request orders made by customer enter (1)"+"\nAny other key will exit: \n");
        int answer = input.nextInt();
        statusCode= "Shipped";
        if (answer == 1) {
            System.out.print("\nCustomer has made 2 orders choose which one you want to look at : "+"\nTo look at order1 1 enter (1)"+"\nTo look at order2 enter (2)\n");
            int answer2 = input.nextInt();
            if (answer2 == 1) {
                System.out.print("\nOrder 1 includes: "+"\nMilwakee Tool sets, Quantity= "+TQ+ "\nMacBook Computer, Quantity=" + CQ+ "\nTotal Cost of order 1= $"+((scost*TQ)+(sacost*CQ))+"\nTotal Sale Cost of order 1= $"+((pscost*TQ)+(psacost*CQ))+"\nOrder STATUS : "+statusCode) ;
            }
            else if  (answer2 == 2) {

                System.out.print("\nOrder 2 includes: "+"\nMilwakee Tool sets, Quantity= "+TQ2+ "\nMacBook Computer, Quantity=" + CQ2+"\nTotal Cost of order 2= $"+((scost*TQ2)+(sacost*CQ2))+"\nTotal Sale Cost of order 2= $"+((pscost*TQ2)+(psacost*CQ2))+ "\nOrder STATUS : "+statusCode) ;
             }


           }
    
        else {
            System.out.println("exit"); 
          }
    
    }


}