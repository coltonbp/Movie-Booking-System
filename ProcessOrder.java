import java.time.Instant;
import java.util.*;
import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;
import javax.swing.*;


public class ProcessOrder
{
    String z= "yes";
    String p="Order 1 is ready";
    String p3="Order 3 is ready";
       
    public void orderedProcessed() {
        String z="yes";
        String p="Order 1 is ready";
        String p3="Order 3 is ready";
     }
     public static void main(String[] args)
     {
      
     
     
      {
         int TQ,CQ;
        int costp=0,costp2=0,salecost=0,salecost2=0,TQW=4,CQW=5;
        int scost=229;
        int pscost=190;

        int sacost=1500;
        int psacost=1200;

        int number; 
        int IDN = 123456 ;
        int OD;

        String STATUS;
        String statusCode;
        

        Scanner input = new Scanner(System.in);
        Scanner console = new Scanner(System.in);
      
        while (true) {
            System.out.println("To request order Enter a ID: ");

            number = input.nextInt();
        
            if (number == IDN ) {
                break;
            }
            else{
                System.out.println(" id not found");
                
            }
         
         
        }
        System.out.println("ID is = " + IDN);
        System.out.println("the orders under this id are:" );

        System.out.println("Order 1: Total cost = $1,958 ");
        System.out.println("Order 2: Total cost = $6,103");
        
        System.out.println("");
        System.out.println("Pick which order you want to look at ");

        OD = console.nextInt();
  
        switch (OD)
        {
        case 1 :
    

        
           System.out.println("Order 1 includes ");
           System.out.println("1.Tool Set\t Rugular Price:$ 229 \t Sale Price: $ 190 \t Milwaukee tool set, comes with a drill and an impact" );
           System.out.println("quantity :2 ");
           TQ=2;
        System.out.println("Regular price is: $"+scost*2);
        System.out.println("The sale price is : $"+pscost*2);
        System.out.println("");
        costp=scost*2;
        salecost=pscost*2;

           System.out.println("2.Computer \t Regular Price:$ 1500 \t Sale Price: $ 1200 \t Mac Laptop with M1 chip  ");
           System.out.println("quantity :1 ");
           CQ=1;
        System.out.println("Regular price is: $"+sacost*1);
        System.out.println("The sale price is : $"+psacost*1);
        System.out.println("");
        costp2=sacost*1;
        salecost2=psacost*1;

           System.out.println("total cost with sale items: $");
           System.out.println(salecost+salecost2);
           System.out.println("total cost for regular cost items: $");
           System.out.println(costp+costp2);
           

           System.out.println("Checking if the warehouse has the items in hand "+ "\n");
           if(TQ<TQW && CQ<CQW){
            System.out.println("The Tools set are ready");
            // order is ready
            STATUS= "Ready";
            System.out.println("The new warehouse quantity for the tools are"+ "\n"+(TQW-2));
            System.out.println("The Computer are ready");
            statusCode= "Ready";
            // order is ready
            System.out.println("The new warehouse quantity for the computers are"+ "\n"+(CQW-1));
            System.out.println("The items have been reserved");
            



            break;
           }
           else if(TQ<TQW && CQ>CQW){
            System.out.println("The Tools set are ready");
            statusCode= "Ready";
            System.out.println("The new warehouse quantity for the tools are"+ "\n"+(TQ-2));
            
            
            System.out.println("The Computer are not ready");
            statusCode= "Ordered";
            System.out.println("The items have been reserved");
            break;
           }

           else if (TQ>TQW && CQ<CQW){
            System.out.println("The Tools are not ready but has been ordered");
            statusCode= "Ordered";
            System.out.println("The Computer are ready");
            statusCode= "Ready";
            System.out.println("The new warehouse quantity for the computers are"+ "\n"+(CQ-1));
            break;
           }

           else if (TQ>TQW && CQ>CQW){
            System.out.println("The Tools are not ready but has been ordered");
            statusCode= "Ordered";
            System.out.println("The Computer are not ready");
            statusCode= "Ordered";     
            break;
            
        }


        case 2 :

        System.out.println("Order 2 includes ");
        System.out.println("1.Tool Set\t Rugular Price:$ 229 \t Sale Price: $ 190 \t Milwaukee tool set, comes with a drill and an impact" );
        System.out.println("quantity :7 ");
        TQ=7;
     System.out.println("Regular price is: $"+scost*7);
     System.out.println("The sale price is : $"+pscost*7);
     System.out.println("");
     costp=scost*7;
     salecost=pscost*7;

        System.out.println("2.Computer \t Regular Price:$ 1500 \t Sale Price: $ 1200 \t Mac Laptop with M1 chip  ");
        System.out.println("quantity :3 ");
        CQ=3;
     System.out.println("Regular price is: $"+sacost*3);
     System.out.println("The sale price is : $"+psacost*3);
     System.out.println("");
     costp2=sacost*3;
     salecost2=psacost*3;

        System.out.println("total cost with sale items: $");
        System.out.println(salecost+salecost2);
        System.out.println("total cost for regular cost items: $");
        System.out.println(costp+costp2);
        

        System.out.println("Checking if the warehouse has the items in hand "+ "\n");

        if(TQ<TQW && CQ<CQW){
         System.out.println("The Tools set are ready");
         statusCode= "Ready";
         System.out.println("The new warehouse quantity for the tools are"+ "\n"+(TQW-7));
         
         
         System.out.println("The Computer are ready");
         statusCode= "Ready";
         System.out.println("The new warehouse quantity for the computers are"+ "\n"+(CQW-3));

         System.out.println("The items have been reserved");
         

         break;
        }
        else if(TQ<TQW && CQ>CQW){
         System.out.println("The Tools set are ready");
         statusCode= "Ready";
         System.out.println("The new warehouse quantity for the tools are"+ "\n"+(TQW-7));
         System.out.println("The items have been reserved");
         
         System.out.println("The Computer are not ready");
         statusCode= "Ordered";
         System.out.println("The items have been reserved");
         break;
        }

        else if (TQ>TQW && CQ<CQW){
         System.out.println("The Tools are not ready but has been ordered");
         statusCode= "Ordered";
         System.out.println("The Computer are ready");
         statusCode= "Ready";
         System.out.println("The new warehouse quantity for the computers are"+ "\n"+(CQW-3));

         System.out.println("The items have been reserved");
         break;
        }

        else if (TQ>TQW && CQ>CQW){
         System.out.println("The Tools are not ready but has been ordered");
         statusCode= "Ordered";
         System.out.println("The Computer are not ready");
         statusCode= "Ordered";

         
         break;



        }
        case 3 :


        System.out.println("Order 1 includes ");
        System.out.println("1.Tool Set\t Rugular Price:$ 229 \t Sale Price: $ 190 \t Milwaukee tool set, comes with a drill and an impact" );
        System.out.println("quantity :1 ");
        TQ=2;
     System.out.println("Regular price is: $"+scost*1);
     System.out.println("The sale price is : $"+pscost*1);
     System.out.println("");
     costp=scost*1;
     salecost=pscost*1;

        System.out.println("2.Computer \t Regular Price:$ 1500 \t Sale Price: $ 1200 \t Mac Laptop with M1 chip  ");
        System.out.println("quantity :1 ");
        CQ=1;
     System.out.println("Regular price is: $"+sacost*1);
     System.out.println("The sale price is : $"+psacost*1);
     System.out.println("");
     costp2=sacost*1;
     salecost2=psacost*1;

        System.out.println("total cost with sale items: $");
        System.out.println(salecost+salecost2);
        System.out.println("total cost for regular cost items: $");
        System.out.println(costp+costp2);
        

        System.out.println("Checking if the warehouse has the items in hand "+ "\n");

        if(TQ<TQW && CQ<CQW){
         System.out.println("The Tools set are ready");
         statusCode= "Ready"; 
         System.out.println("The new warehouse quantity for the tools are"+ "\n"+(TQW-1));
         System.out.println("The Computer are ready");
         statusCode= "Ready";
         
         // order is ready
         System.out.println("The new warehouse quantity for the computers are"+ "\n"+(CQW-1));
         System.out.println("The items have been reserved");
         
         
         




         break;
        }
        else if(TQ<TQW && CQ>CQW){
         System.out.println("The Tools set are ready");
         statusCode= "Ready";
         System.out.println("The new warehouse quantity is"+ "\n"+(TQ-1));
         System.out.println("The items have been reserved");
         
         System.out.println("The Computer are not ready");
         statusCode= "Ordered";
         break;
        }

        else if (TQ>TQW && CQ<CQW){
         System.out.println("The Tools are not ready but has been ordered");
         statusCode= "Ordered";
         System.out.println("The Computer are ready");
         statusCode= "Ready";
         System.out.println("The new warehouse quantity for the computers are"+ "\n"+(CQ-1));
         break;
        }

        else if (TQ>TQW && CQ>CQW){
         System.out.println("The Tools are not ready but has been ordered");
         statusCode= "Ordered";
         System.out.println("The Computer are not ready");
         statusCode= "Ordered";


         break;
         
     }








  
           }
           System.out.println("");
    System.out.println("End of program");


}


     }
   
    

      }
