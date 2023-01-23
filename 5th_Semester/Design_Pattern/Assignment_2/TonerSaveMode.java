public class TonerSaveMode extends PrintMode {
    private double tonerSavingLevel;
    ITonerSaveAlgo tonerSaveAlgo;

    public double getTonerSavingLevel() {
        return tonerSavingLevel;
    }

    public void setTonerSavingLevel(double tonerSavingLevel, ITonerSaveAlgo tonerSaveAlgo) {
        this.tonerSavingLevel = tonerSavingLevel;
        this.tonerSaveAlgo=tonerSaveAlgo;
    }

    @Override
    public void doMode() {
        tonerSaveAlgo.algorithm(tonerSavingLevel);
        
    }

}
