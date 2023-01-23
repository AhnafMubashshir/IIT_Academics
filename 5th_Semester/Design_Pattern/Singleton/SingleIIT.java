import java.util.List;

public class SingleIIT {
    private SingleIIT (){

    }

    private static SingleIIT s= null;

    public static SingleIIT getInstance(){
        if(s==null){
            s= new SingleIIT();
        }
        return s;
    }

    public void welcome(List<Students> students){
        System.out.println("-----Welcome to IIT-----.\nNew Students are: \n");

        for (Students s : students) { 
            System.out.println(s);
        }
        System.out.println("");
        
    }
}
