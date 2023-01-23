import java.io.IOException;
import java.util.List;

public class Main {
    public static void main(String args[]){
        GetStudentList studentList= new GetStudentList();
        List<Students> students;

        try {
            students = studentList.readStudentNameFromTxt("bsse12.txt");
            BsseBatch b12= new BsseBatch(students);
            b12.createObject();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
