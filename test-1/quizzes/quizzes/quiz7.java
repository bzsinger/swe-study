// what is the output of the following?

class Test1 {
    public static void test () {
        String s = new String("abc");
        String t = new String("abc");
        System.out.print(s == t);
        System.out.print(" ");
        System.out.println(s.equals(t));}}

// what is the output of the following?

class A
    {}

class Test2 {
    public static void test () {
        A x = new A();
        A y = new A();
        System.out.print(x == y);
        System.out.print(" ");
        System.out.println(x.equals(y));}}
