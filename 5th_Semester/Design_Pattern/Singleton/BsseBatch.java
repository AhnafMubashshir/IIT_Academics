import java.util.List;

public class BsseBatch{
    private final List<Students> students;

    public BsseBatch(List<Students> students){
        this.students= students;
    }

    public void createObject(){
        SingleIIT single= SingleIIT.getInstance();
        single.welcome(students);
    }

}