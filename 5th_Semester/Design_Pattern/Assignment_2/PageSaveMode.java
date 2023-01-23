public class PageSaveMode extends PrintMode {
    int orientation;
    int pageNumber;

    public int getOrientation(){
        return this.orientation;
    }

    public void setOrientation(int orientation){
        this.orientation= orientation;
    }

    public int getPageNumber(){
        return this.pageNumber;
    }

    public void setPageNumber(int pageNumber){
        this.pageNumber= pageNumber;
    }

    public void doMode(){
        renderPreview();
    }

    private void renderPreview(){
        
    }
}
