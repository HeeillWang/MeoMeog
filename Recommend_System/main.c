#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>
#define NUM_OF_RESTAURANT 100

typedef enum bool {false, true} bool;
typedef enum weather {sunny, rainy, cloudy} weather; // add more weather

typedef struct location {
    float latitude;
    float longitude;
} loaction;

typedef struct inputData {
    struct location currentLocation;
    int age;
    int money;
    int temperature;
    int time;
    float foodPreference[12];
    float newPreference;
    float rangePrefernece;
    bool gender;
    char weather;
} inputData;

typedef struct restaurant {
    char name[100];
    struct location resLoc;
    float grade;
    float result;
    char kind;
} restaurant; // can change how to implement it.

void recommend(int *resNum, inputData _data, restaurant *_rest);

int main(int argc, const char * argv[]) {
    FILE *fp;
    fp = fopen("/Users/imola/MeoMeog/Recommend_System/Sample_User_Input.csv", "r"); // change directory properly
    if (fp == NULL) {
        return 1;
    }
    char temp = 0;
    inputData input;
    
    fscanf(fp, "%c", &temp);
    switch (temp) {
        case 'M':
            input.gender = false;
            break;
        case 'F':
            input.gender = true;
            break;
        default:
            return 1;
            break;
    }
    
    fscanf(fp, "%c", &temp);
    fscanf(fp, "%d", &input.age);
    
    for (int i = 0; i < 12; i++) {
        fscanf(fp, "%c", &temp);
        fscanf(fp, "%f", &input.foodPreference[i]);
    }
    
    fscanf(fp, "%c", &temp);
    fscanf(fp, "%f", &input.newPreference);
    fscanf(fp, "%c", &temp);
    fscanf(fp, "%f", &input.rangePrefernece);
    fscanf(fp, "%c", &temp);
    fscanf(fp, "%d", &input.money);
    
    fclose(fp);
    
    fopen("/Users/imola/MeoMeog/Recommend_System/Sample_Current_Data.csv", "r"); // change directory properly
    if (fp == NULL) {
        return 1;
    }
    
    fscanf(fp, "%c", &input.weather);
    fscanf(fp, "%c", &temp);
    fscanf(fp, "%d", &input.temperature);
    fscanf(fp, "%c", &temp);
    fscanf(fp, "%d", &input.time);
    fscanf(fp, "%c", &temp);
    fscanf(fp, "%f", &input.currentLocation.latitude);
    fscanf(fp, "%c", &temp);
    fscanf(fp, "%f", &input.currentLocation.longitude);
    
    fclose(fp);
    
    restaurant arr[NUM_OF_RESTAURANT];
    fopen("/Users/imola/MeoMeog/Recommend_System/Sample_Restaurant.csv", "r");
    if (fp == NULL) {
        return 1;
    }
    
    char buffer[100];
    int cnt = 0;
    
    while (!feof(fp)) {
        fgets(buffer, 100, fp);
        strcpy(arr[cnt].name, strtok(buffer, ","));
        //printf("%s", arr[cnt].name);
        arr[cnt].resLoc.latitude = atof(strtok(NULL, ","));
        arr[cnt].resLoc.longitude = atof(strtok(NULL, ","));
        arr[cnt].kind = atoi(strtok(NULL, ","));
        arr[cnt].grade = atof(strtok(NULL, ","));
        arr[cnt].result = 0;
        
        cnt++;
    }
    
    fclose(fp);
    
    int result[3];
    
    recommend(result, input, arr);
    
    return 0;
}

void recommend(int *resNum, inputData _data, restaurant *_rest) {
    return; // fill this function
}
