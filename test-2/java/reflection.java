/* reflection */

// automatically creates an instance of class Class
class A1 { }

class T {
  public static void main(String[] args) {
    A1 x = new A1();
    A1 y = new A1();
    x == y;   // false - not a singleton

    Class c1 = A1.class;
    Class c2 = A1.class;
    c1 == c2; // true - singleton

    Class c3 = x.getClass();
    c1 == c3; // true - singleton

    Class c4 = Class.forName("A1"); // if fails - ClassNotFound exception

                  /* will call default constructor (no parameters) -
                      if A1 defined without default constructor -
                        InstantiationException */
    Object o = c4.newInstance();
                 /* if A1 is an interface or abstract class -
                      InstantiationException */
                 /* if A1 has a private constructor -
                      IllegalAccessException */

    /* Class owns method, so it can only return an Object */
    A1 z = (A1)o // need to cast to A1
          /* if o not actually an A1 -
              ClassCastException */
  }
}
