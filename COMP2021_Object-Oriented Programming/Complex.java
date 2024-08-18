package hk.edu.polyu.comp.comp2021.assignment2.complex;
import hk.edu.polyu.comp.comp2021.assignment2.complex.Rational;

public class Complex {

    private Rational real;
    private Rational imag;

    public Complex(Rational real, Rational imag) {
        this.real = real;
        this.imag = imag;
    }

    public Complex add(Complex other) {
        Complex sum = new Complex(this.real.add(other.real),this.imag.add(other.imag));
        return sum;
    }

    public Complex subtract(Complex other) {
        Complex difference = new Complex(this.real.subtract(other.real),this.imag.subtract(other.imag));
        return difference;
    }

    public Complex multiply(Complex other) {
        Rational mulReal;
        mulReal = this.real.multiply(other.real).subtract(this.imag.multiply(other.imag));
        Rational mulImag;
        mulImag = this.imag.multiply(other.real).add(other.imag.multiply(this.real));
        Complex mul = new Complex(mulReal,mulImag);
        return mul;
    }

    public Complex divide(Complex other) {
        Rational handleImag = new Rational(-1,1);
        handleImag = handleImag.multiply(other.imag);
        Complex conjugate = new Complex(other.real,handleImag);

        Complex divNumerator = this.multiply(conjugate);
        Complex divDenominator = other.multiply(conjugate);
        Complex div = new Complex(divNumerator.real.divide(divDenominator.real), divNumerator.imag.divide(divDenominator.real));
        return div;
    }

    public void simplify() {
       this.real.simplify();
       this.imag.simplify();
    }

    public String toString() {
        return "("+this.real+","+this.imag+")";
    }

    // ==================================

}
