package hk.edu.polyu.comp.comp2021.assignment3.employee;

/**
 * Levels of salary.
 */
enum SalaryLevel {
    ENTRY(1), JUNIOR(1.25), SENIOR(1.5), EXECUTIVE(2);
    private final double level;
    private SalaryLevel(double level) { this.level = level; }
    public double getScale() { return level; }
}