// abstract

// cannot make instance of class
abstract class A {
  
    // once method marked abstract, class must also
    //  be abstract
    abstract void f(long a) {} // must override


    // can include non-abstract methods in class,
    //  but discouraged
    // brittle - if you try to override with long,
    //  your new method would never get used
    void g(long a) {}         // can override


    final void h(long a) {}   // can't override
}
