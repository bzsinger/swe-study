public class Singleton {

    // Be lazy and instantiate only when first use
    private static Singleton instance = null;

    private Singleton() {}  // Do not allow outside world to instantiate

    public static Singleton getInstance() {
        if (Singleton.instance == null) {
            Singleton.instance = new Singleton();
        }

        return Singleton.instance;
    }


    public static void main(String[] args) {
        Singleton a = Singleton.getInstance();
        Singleton b = Singleton.getInstance();
        System.out.println(a == b);
    }
}
