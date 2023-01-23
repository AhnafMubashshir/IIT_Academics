public class Students {
    private String name;
    private String batch;

    public Students(String batch, String name){
        this.batch= batch;
        this.name= name;
    }

    public String getBatch(){
        return batch;
    }

    public void setBatch(String batch){
        this.batch= batch;
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name= name;
    }

    @Override
    public String toString(){
        return "Batch: " + batch + "\tName: "+ name;
    }
}
