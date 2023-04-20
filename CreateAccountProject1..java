import java.util.ArrayList;
import java.util.Scanner;

class CreateAccount { //
        private String id;
        private String password;
        private String name;
        private String address;
        private String ccno;

        public CreateAccount(String id, String password, String name, String address, String ccno) {
                id = this.id;
                password = this.password;
                name = this.name;
                address = this.address;
                ccno = this.ccno;
        }

        public String getId() {
                return this.id;
        }
}

class Account {
        private CreateAccount c; //
        private String acType;
        private int feePending;

        public Account(CreateAccount c, int acType) { //
                

                System.out.println("Account created successfully!");

        }

        public CreateAccount getCreateAccount() { //
                return c;
        }


class Main {
        public static void main(String[] args) {

                ArrayList<Account> accountDB = new ArrayList<Account>();

                Scanner sc = new Scanner(System.in);

                System.out.print("Enter your ID: ");
                String id = sc.nextLine();

                boolean flag = false;
                while(true){
                        flag = false;
                        for(Account a: accountDB){
                                if(a.getCreateAccount().getId().equals(id)){
                                        System.out.println("ID already exists, please enter a different ID: ");
                                        id = sc.nextLine();
                                        flag = true;
                                        break;
                                }
                        }

                        if(!flag)
                                break;
                }

                System.out.print("Please enter a password : ");
                String passwordhere = sc.nextLine();
               
                
                String specialCharactersString = "!@#$%&*()'+,-./:;<=>?[]^_`{|}";
                for (int i=0; i < ((String) passwordhere).length() ; i++)
                {
                    char ch = ((String) passwordhere).charAt(i);
                    if(specialCharactersString.contains(Character.toString(ch)) && ((String) passwordhere).length() > 6) {   
                        break;
                    }    
                    else {    
                        int j =1;
                        do{
                        
                                System.out.print("Password doesn't meet requirements, try again \n");
                        System.out.print( "Enter a password You would like.\n" +
                        "Password must have; a minimum of 6 characters, at least 1 digit, a special character, and an uppercase letter \n");
                        if(specialCharactersString.contains(Character.toString(ch)) && ((String) passwordhere).length() > 6) {   
                            ;
                            j=4;
                        }
                        else
                            j++;
                        
                       
                            
                        
                    }   while (j < 3);
                    main(null); 
                }
            }





                

                System.out.print("Enter your Name: ");
                String name = sc.nextLine();

                System.out.print("Enter your Home Address: ");
                String address = sc.nextLine();

                System.out.print("Enter your Credit Card Number: ");
                String ccno = sc.nextLine();

                CreateAccount c = new CreateAccount(id, passwordhere, name, address, ccno); //

                int acType = -1;
                accountDB.add(new Account(c, acType));
             
        }
}
}
        
