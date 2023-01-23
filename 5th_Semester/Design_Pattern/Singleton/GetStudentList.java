import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class GetStudentList {
    public List<Students> readStudentNameFromTxt(String fileName) throws IOException { 
        System.out.println(fileName);
        List<Students> students = new ArrayList<Students>(); 
        Path pathToFile = Paths.get(fileName);

        try (BufferedReader br = Files.newBufferedReader(pathToFile, StandardCharsets.US_ASCII)) {
            String line = br.readLine();

            while (line != null) {
                String attributes[] = line.split(":"); 
                Students studentsName = createList(attributes);

                students.add(studentsName);

                line= br.readLine();
            }
        }catch (IOException ioe) {
            ioe.printStackTrace();
        }

        return students;
    }

    public static Students createList(String Data[]){
        String batch= Data[0];
        String Name= Data[1];

        return new Students(batch, Name);

    }
}
