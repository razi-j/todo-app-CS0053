/// ToDoApp.java
import java.util.ArrayList;
import java.util.Scanner;

public class ToDoApp {
    static ArrayList<String> tasks = new ArrayList<>(); // used generics for better stability

    public static void addtask(String t) {
        tasks.add(t);
        System.out.println("Task Added!!");
    }

    public static void showTasks() {
        if (tasks.isEmpty()) {
        System.out.println("No tasks yet");
        } 
        else {
            for (int i = 0; i < tasks.size(); i++) {
                System.out.println(
                (i + 1) + ". " + tasks.get(i)); // fixed because i goes up to tasks.size()
            } // fixes java.lang.IndexOutOfBoundsException
        }
  }

public static void removeTask(int n) {
        if (tasks.isEmpty()) { // checks if list is empty then prints accordingly
            System.out.println("Nothing to remove");
        } 
        else if (n > 0 && n <= tasks.size()) {
            tasks.remove(n - 1);
            System.out.println("Task removed");
        } 
        else {
            System.out.println("Invalid task number");
        }
  }

public static void main(String args[]) {
    Scanner s = new Scanner(System.in);
    boolean exit = false;
    while (!exit) {
        System.out.println("1. Add Task"); 
        System.out.println("2. Show Tasks");
        System.out.println("3. Remove Task");
        System.out.println("4. Exit");
        int choice = s.nextInt();
        s.nextLine(); 
        switch(choice) {
            case 1:
                System.out.println("Enter Task: ");
                String t = s.nextLine();
                addtask(t);
                System.out.println();
                break;
            case 2:
                showTasks();
                System.out.println();
                break;
            case 3:
                System.out.print("Enter task no to remove: ");
                int n = s.nextInt();
                removeTask(n);
                System.out.println();
            case 4:
                exit = true;
                break;
            default:
                System.out.println("Wrong Choice!!");
                System.out.println();
                break;
            }
        }
        
    }
}
