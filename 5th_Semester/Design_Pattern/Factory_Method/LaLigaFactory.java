package Design_Pattern.Factory_Method;

public class LaLigaFactory extends FootballLeagueFactory{

    @Override
    public FootballLeague getLeague() {
        return new LaLiga();
    }
    
}
