//Conditional Statement Using if...else in C

#include <stdio.h>

/*
 Systolic <= 120 AND Diastolic <=80 --> NORMAL
 Systolic in(120 ... 139) OR Diastolic in (80,89) --> PreHypertension
 Systolic in(140 ... 159) OR Diastolic in (90,99), --> Hypertension Stage 1
 Systolic in(160 ... 180) OR Diastolic in (100,110) --> Hypertension Stage 2
 Systolic over 180 OR Diastolic OVER 110 --> CRISIS - Call 911
*/
void CheckHighBloodPressure(int Systolic, int Diastolic)
{
    printf("If your blood pressure resluts are between %d / %d... \n", Systolic, Diastolic);
    if (Systolic <= 120 && Diastolic <= 80)
    {
        //NORMAL
        printf("Your Blood Pressure is NORMAL \n");
        printf("Congragtulations!\n\n");
    }
    else if ((Systolic >= 120 && Systolic <= 139) || (Diastolic >= 80 && Diastolic <= 89))
    {
        //Prehypertension
        printf("You are prehypertensive. \n");
        printf("Looking good champ!\n\n");
    }
    else if ((Systolic >= 140 && Systolic <= 159) || (Diastolic >= 90 && Diastolic <= 99))
    {
        //Stage 1
        printf("You have hypertension Stage 1 \n");
        printf("Not bad!\n\n");
    }
    else if ((Systolic >= 160 && Systolic <= 180) || (Diastolic >= 100 && Diastolic <= 110))
    {
        //Stage 2
        printf("You have hypertension Stage 2 \n");
        printf("Danger! Danger!\n\n");
    }
    else if ((Systolic >= 180) || (Diastolic >= 110))
    {
        //Hypertension
        printf("You have hypertension! Call a doctor!!! \n");
        printf("EEEEEKKKK!\n");
        if (Systolic > 200)
            printf("CALL 911\n");
    }
}

void main()

{
    CheckHighBloodPressure(120, 80);
    CheckHighBloodPressure(129,88);
    CheckHighBloodPressure(139, 98);
    CheckHighBloodPressure(149, 108);
    CheckHighBloodPressure(169, 118);
}   