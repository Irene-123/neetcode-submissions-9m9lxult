static class Singleton {

    private Singleton() {
    }
    private String value = null;
    private static Singleton uniqueInstance = null;

    public static Singleton getInstance() {
        if (uniqueInstance == null) {
            uniqueInstance = new Singleton();
        }
        return uniqueInstance;
        

    }

    public String getValue() {
        
        return value;

    }

    public void setValue(String value) {
        this.value = value;
    }
    
}
