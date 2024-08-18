package hk.edu.polyu.comp.comp2021.assignment1;

public class MiniFloat {

    public static final int MINI_FLOAT_SIZE = 8;

    public static float miniFloatFromString(String bitSequence) {
        int sign = Character.getNumericValue(bitSequence.charAt(0));   //sign = 1st bit

        int[] exponentArr = new int [4];  //exponent = 2nd to 5th bit
        for (int i=1; i<=4; i++){
            exponentArr[i-1]=Character.getNumericValue(bitSequence.charAt(i));
        }

        int[] mantissaArr = new int [3];  //mantissa = 6th to 8th bit
        for (int i=5; i<=7; i++){
            mantissaArr[i-5]=Character.getNumericValue(bitSequence.charAt(i));
        }

        double exponent = 0.0;
        double power = 0.0;
        for (int i=3; i>=0; i--){
            exponent += exponentArr[i] * Math.pow(2,power);
            power++;
        }

        double mantissa = 0.0;
        power = -1.0;
        for (int i=0; i<=2; i++){
            mantissa += mantissaArr[i] * Math.pow(2,power);
            power--;
        }

        float miniFloat = (float)((mantissa+1)*Math.pow(2,exponent));    //miniFloat = 1.mantissa x 2^exponent
        if (sign==1){
            miniFloat *= -1;    //sign bit defines the number to be positive (0) or negative (1)
        }
        return miniFloat;
    }

    public static int numIntegralMiniFloats() {
        String[] validMiniFloatSequence = getValidMiniFloatBitSequences(); //get all (256) miniFloats
        int result = 0;  //count the number of all integral miniFloat values
        for (int i=0; i< validMiniFloatSequence.length; i++){
            float x = miniFloatFromString(validMiniFloatSequence[i]);  //retrieve each miniFloat
            if (Math.ceil(x) == x){  //if it is an integral value
                result++;            //number of all integral miniFloat values + 1
            }
        }
        System.out.println(result);
        return result;
    }

    /**
     * Get all valid bit sequences for miniFloat values.
     */
    private static String[] getValidMiniFloatBitSequences(){
        int nbrValues = (int)Math.pow(2, MINI_FLOAT_SIZE);

        String[] result = new String[nbrValues];
        for(int i = 0; i < nbrValues; i++){
            result[i] = String.format("%" + MINI_FLOAT_SIZE + "s", Integer.toBinaryString(i))
                    .replace(' ', '0');
        }
        return result;
    }

    public static void main(String[] args){ numIntegralMiniFloats();
    }

}
