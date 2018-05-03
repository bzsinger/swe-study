// reflection

/* Using reflection in Java, instantiate an instance of a class from a String
where the String is the name of the class. */

class A1 {}

class Test {
  public static void main(String[] args) {
    try {
      A1 x = (A1)Class.forName("A1").newInstance();
    } catch (ClassCastException e) { }
      catch (ClassNotFoundException e) {}
      catch (IllegalAccessException e) {}
      catch (InstantiationException e) {}
  }
}
