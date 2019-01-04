#include <stdio.h>
/*Problem statement- Write a program to output
the approximate position of a point in the graph when the scale is given*/

//This structure store original location and approximate location on graph
typedef struct location{
    float apna;
    float prev;
    float line;
}location;

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
    location xf,yf;
    int xline,yline;
    xf=func_lines(x,xscale);
    yf=func_lines(y,yscale);
    printf("\nFor x coordinate %f:%0.2f lines after %f",xf.apna,xf.line,xf.prev);
    printf("\nFor y coordinate %f:%0.2f lines above %f",yf.apna,yf.line,yf.prev);
}
