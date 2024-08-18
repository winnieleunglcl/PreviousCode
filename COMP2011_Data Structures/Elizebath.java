package comp2011.ass1;

/**
 * @author yixin cao (October 6, 2020)
 * <p>
 * A simulation of the triage of the Queen Elizabeth Hospital.
 * Each patient has been assigned a urgent level.
 * <p>
 */

class Patient {
    String name;
    String urgence;

    Patient(String name, String urgence) {
        this.name = name;
        this.urgence = urgence;
    }

    public String toString() {
        return "Patient leaving: " + this.name + "\nUrgent Lv: " + this.urgence;
        // implement this.
    }
}

public class Elizebath {


    private static Patient[] patients = new Patient[100];

    public static int returnLevel(String string) {

        if (string.equals("Urgent")) {
            return 3;
        }
        if (string.equals("Semi-Urgent")) {
            return 2;
        }
        if (string.equals("Non-Urgent")) {
            return 1;
        }
        return 0;
    }

    // WAY 1: enter uses O(1) time, leave uses O(n) time
    // a new patient (with a urgent level already assigned) enters the storage.

//    static int indexForWay1 = 0;
//
//    public static void enter(Patient patient) {
//        patients[indexForWay1] = new Patient(patient.name, patient.urgence);
//        patients[indexForWay1] = patient;
//        indexForWay1++;
//    }
//
//    // returns the one with the highest urgent level,
//    // and if there are more than one patient of the highest urgent level, then first come first serve.
//    public static Patient leave() {
//        int patientLeaving = 0, patientLevel = 0;
//        Patient temp = new Patient("name", "urgence");
//        for (int j = 0; j <= indexForWay1; j++) {
//            if (patients[j] == null) break;
//            int patientInQueue = 0;
//
//                patientInQueue = returnLevel(patients[j].urgence) ;
//
//            if (patientInQueue > patientLevel) {
//                patientLevel = patientInQueue;
//                patientLeaving = j;
//                temp.urgence = patients[j].urgence;
//                temp.name = patients[j].name;
//            }
//        }
//        if (patients[patientLeaving] != null) {
//            patients[patientLeaving].name = "name";
//        }
//        if (patients[patientLeaving] != null) {
//            patients[patientLeaving].urgence = "urgence";
//        }
//        return temp;
//
//    }


    //  WAY 2: enter uses O(n) time, leave uses O(1) time
    static int indexForWay2 = 0;
    public static void enter(Patient patient) {
        Patient temp = null, temp2;
        boolean condition = false;

        int newPatientLevel = returnLevel(patient.urgence);
        if (patients[0] == null) {
            patients[0] = new Patient(patient.name, patient.urgence);
            indexForWay2++;
            return;
        }
        patients[indexForWay2] = new Patient("name", "urgence");

        for (int j = 0; j <= indexForWay2; j++) {
            int patientLevelInQueue = returnLevel(patients[j].urgence);
            if (condition) {
                temp2 = new Patient(patients[j].name, patients[j].urgence);
                patients[j].name = temp.name;
                patients[j].urgence = temp.urgence;
                temp.name = temp2.name;
                temp.urgence = temp2.urgence;
                continue;
            }
            if (patientLevelInQueue < newPatientLevel && j+1==indexForWay2){
                patients[j+1].name = patient.name;
                patients[j+1].urgence = patient.urgence;
            }
            if (patientLevelInQueue >= newPatientLevel) {
                temp = new Patient(patients[j].name, patients[j].urgence);
                patients[j].name = patient.name;
                patients[j].urgence = patient.urgence;
                condition = true;
            }
        }
        indexForWay2++;
    }

    public static Patient leave() {
        return patients[--indexForWay2];
    }

    public static void main(String[] args) {

        enter(new Patient("Peppa", "Semi-Urgent"));
        enter(new Patient("Eason", "Urgent"));
        enter(new Patient("Denise", "Urgent"));
        enter(new Patient("Jennifer", "Semi-Urgent"));
        enter(new Patient("Joey", "Non-Urgent"));
        enter(new Patient("Kay", "Urgent"));
        System.out.println(leave());
        System.out.println(leave());
        enter(new Patient("Cheung", "Semi-Urgent"));
        enter(new Patient("Winnie", "Non-Urgent"));
        enter(new Patient("Mickey", "Urgent"));
        enter(new Patient("Teddy", "Semi-Urgent"));
        enter(new Patient("Bob", "Non-Urgent"));
        enter(new Patient("Amy", "Semi-Urgent"));
        System.out.println(leave());
        System.out.println(leave());
        System.out.println(leave());
    }


}