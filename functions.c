#include <stdio.h>
/*Problem statement- Write a program to output
the approximate position of a point in the graph when the scale is given*/

//This structure store original location and approximate location on graph
typedef struct location{
    float apna;
    float prev;
    float line;
}location;
//Doubt in passing pointers to structures to functions
/*struct location x;
struct location y;
struct location *px;
struct location *py;
px=&x;
py=&y;*/

/*Function outputs number of lines above/after*/
location func_lines(float p,float scale){
    float temp;
    temp=p;
    location r;
    r.apna=p;
    int i;
    for(i=0;;){
        if(temp>=10*scale){
            temp-=10*scale;
        }
        if(temp<10*scale){
            r.line=temp/scale;
            r.prev=(i+1)*scale*10;
            if(r.apna<10*scale){
                r.prev=0;
            }
            break;
        }
        i++;
    }
    return r;
}

void linecount(float x,float y,float xscale,float yscale){
    //int check=1;
    //float x,y;
    location xf,yf;
    //float xscale,yscale;
    int xline,yline;
    //int i,temp;
    /*printf("Enter the scale in units/mm for x axis: ");
    scanf("%f",&xscale);
    printf("Enter the scale in units/mm for y axis: ");
    scanf("%f",&yscale);*/
    //printf("%f %f",xscale,yscale);
    /*while(check>0){
        printf("\n\nEnter the x coordinate of given point: ");
        scanf("%f",&x);
        printf("Enter the y coordinate of given point: ");
        scanf("%f",&y);

    }*/
    xf=func_lines(x,xscale);
    yf=func_lines(y,yscale);
    printf("For x coordinate %f:%0.2f lines after %f",xf.apna,xf.line,xf.prev);
    printf("\nFor y coordinate %f:%0.2f lines above %f",yf.apna,yf.line,yf.prev);
}
