package Design_Pattern.Factory_Method;

public class EPLFactory extends FootballLeagueFactory{

    @Override
    public FootballLeague getLeague() {
        return new EPL();
    }
    
}
