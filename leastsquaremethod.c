#include <stdio.h>
#include "functions.c"
/*Program that outputs a line using least square method*/

/*This structure stores coordinates of the point*/
typedef struct z{
    float x;
    float y;
}pointset;

/*This function returns a set of averages of x and y coordinates*/
//WORKING
pointset mean(pointset a[100],int n){
    pointset res;
    int i;
    float sumx=0,sumy=0;
    for(i=0;i<n;i++){
        sumx+=a[i].x;
        sumy+=a[i].y;
    }
    res.x=sumx/n;
    res.y=sumy/n;
    return res;
}

//This function gives the y coordinate when x is given of a specific line
float line(float m,float c,float x){
    float y;
    y=m*x+c;
    return y;
}

int main(){
	//maximum 100 points can be plotted
    pointset a[100];
    pointset b;
    int n,i;
    float m,c;
    float sumsqr=0;
    float sumprod=0;
    char check;
    float xscale,yscale;
    printf("Enter the number of readings: ");
    scanf("%d",&n);
    if(n==1){
        printf("Invalid input!More than one reading is required.");
        return 0;
    }
	if(n>100){
		printf("Maximum 100 readings can be plotted!");
		return 0;
	}
    for(i=0;i<n;i++){
        printf("Enter the x coordinate: ");
        scanf("%f",&a[i].x);
        printf("Enter the y coordinate: ");
        scanf("%f",&a[i].y);
    }
    for(i=0;i<n;i++){
        sumsqr+=(a[i].x)*(a[i].x);
    }
    for(i=0;i<n;i++){
        sumprod+=(a[i].x)*(a[i].y);
    }
    b=mean(a,n);
    /*printf("%f",b.x);
    printf("%f",b.y);*/
    //Formula for slope(m) and x intercept(c) according to the least square method
    //This ensures equal number of points on either side of the line
    m=(sumprod-n*b.x*b.y)/(sumsqr-n*b.x*b.x);
    c=(b.y*sumsqr-b.x*sumprod)/(sumsqr-n*b.x*b.x);
    printf("y= %f x + %f",m,c);
    /*Introducing a new feature!!*/
    printf("\nNeed help plotting the graph?(y/n): ");
    scanf("%c",&check);
    scanf("%c",&check);
    if(check=='y'){
        printf("Enter the scale for x axis in units/mm: ");
        scanf("%f",&xscale);
        printf("Enter the scale for y axis in units/mm: ");
        scanf("%f",&yscale);
        printf("\nFollowing are three points on the line");
        for(i=0;i<3;i++){
            linecount(xscale*(i+1)*10,line(m,c,xscale*(i+1)*10),xscale,yscale);
        }
        check='n';
	//This is an option to print the original readings
        printf("\nPlot the readings?(y/n): ");
        scanf("%c",&check);
        scanf("%c",&check);
        if(check=='y'){
            for(i=0;i<n;i++){
                linecount(a[i].x,a[i].y,xscale,yscale);
            }
        }
    }
    return 0;
}
