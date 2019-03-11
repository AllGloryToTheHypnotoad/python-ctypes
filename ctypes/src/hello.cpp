#include <stdio.h>
#include <math.h>

using namespace std;

class Test {
public:
    Test() {}
    void read(double a[5]){
        for (int i=0; i<5; i++) a[i] = 0.1*i;
    }
};

#ifdef __cplusplus
extern "C"  //Tells the compile to use C-linkage for the next scope.
{
#endif

Test* new_test(){return new Test();}
void read(Test* t, double a[5]){t->read(a);}





int test(int a){
    return a*a;
}

double hcos(double j){
    // return cos(j);
    double ans = 0.0;
    printf(">> %f %f\n", j, ans);
    try {
        ans = cos(j);
    }
    catch (...) {
        printf("crap\n");
    }
    // return j*j;
    return ans;
}

void testarray(double a[5]){
    for (int i=0; i<5; i++) a[i] = i*10.0;
}

#ifdef __cplusplus
}
#endif
