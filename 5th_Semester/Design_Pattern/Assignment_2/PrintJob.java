public class PrintJob{
    PrintRequest [] printRequests;
    PrioritySetting prioritySetting;

    public void pullJob(){

    }
    
}

class PrintRequest{
    PrintMode printMode;

    public PrintRequest(PrintMode printMode){
        this.printMode = printMode;
    }

}

class PrioritySetting{
    //black sheep
    public void changePriority(){

    }
}
