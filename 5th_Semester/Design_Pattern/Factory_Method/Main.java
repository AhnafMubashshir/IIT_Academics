package Design_Pattern.Factory_Method;

public class Main {
    public static void main(String[] args) {
        FootballLeagueFactory  fl1 = new LaLigaFactory();
        FootballLeague laLiga = fl1.getLeague();
        laLiga.displayLeague();

        FootballLeagueFactory  fl2 = new EPLFactory();
        FootballLeague epl = fl2.getLeague();
        epl.displayLeague();
    }
}
