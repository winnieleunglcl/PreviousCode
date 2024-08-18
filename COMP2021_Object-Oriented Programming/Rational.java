package hk.edu.polyu.comp.comp2021.assignment2.complex;

public class Rational {

    private int numerator;
    private int denominator;

    public Rational(int numerator, int denominator) {
        this.numerator = numerator;
        this.denominator = denominator;
    }

    public Rational add(Rational other) {
        Rational sum = new Rational(1,this.denominator);
        if (this.denominator != other.denominator){
            sum.numerator = (this.numerator * other.denominator) + (other.numerator * this.denominator);
            sum.denominator *= other.denominator;
        }
        else{
            sum.numerator = this.numerator + other.numerator;
        }
        return sum;
    }

    public Rational subtract(Rational other) {
        Rational difference = new Rational(1,this.denominator);
        if (this.denominator != other.denominator){
            difference.numerator = (this.numerator * other.denominator) - (other.numerator * this.denominator);
            difference.denominator *= other.denominator;
        }
        else{
            difference.numerator = this.numerator - other.denominator;
        }
        return difference;
    }

    public Rational multiply(Rational other) {
        Rational mul = new Rational(this.numerator,this.denominator);
        mul.numerator *= other.numerator;
        mul.denominator *= other.denominator;
        return mul;
    }

    public Rational divide(Rational other) {
        Rational div = new Rational(this.numerator,this.denominator);
        div.numerator *= other.denominator;
        div.denominator *= other.numerator;
        return div;
    }

    public String toString() {
        return this.numerator+"/"+this.denominator;
    }

    public void simplify() {
        if (this.denominator < 0){
            this.numerator *= -1;
            this.denominator *= -1;
        }
        int larger = 0;
        if (this.numerator > this.denominator){
            larger = this.numerator;
        }
        else{
            larger = this.denominator;
        }
        for (int i=1; i<=larger; i++){
            if (this.numerator==0){
                this.denominator = 0;
                break;
            }
            if (this.numerator%i==0 & this.denominator%i==0){
                this.numerator /= i;
                this.denominator /= i;
                i = 1;
            }
        }
    }

    // ==================================

}
