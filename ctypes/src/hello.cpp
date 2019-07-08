#include <stdio.h>
#include <math.h>

using namespace std;

/*
Create a simple class
*/
class Test {
public:
    Test() {
        key = 25;
        for (int i=0; i<10; i++) buffer[i] = 20;
        for (int i=0; i<10; i++) printf("oo %f ", buffer[i]);
        printf("\n");
    }
    void read(double a[5]){
        printf(">> c++ read()\n");
        for (int i=0; i<5; i++) a[i] = 0.1*i;
        for (int i=0; i<5; i++) printf("++ %f ", a[i]);
        printf("\n");
    }
    // double* readprotected(){
    void readprotected(){
        printf(">> c+ readprotected\n");
        // for (int i=0; i<10; i++) printf("-> %d %f\n", i, buffer[i]);
        // for (int i=0; i<10; i++) printf("- %d \n", ibuf[i]);
        printf("hi\n");
        // for (int i=0; i<10; i++) buffer[i] = 20.0*i;
        // for (int i=0; i<10; i++) printf("| %f ", buffer[i]);
        printf("ho\n");
        printf("key: %d\n", key);
        // return buffer;
    }

protected:
    double buffer[10];
    int ibuf[10];
    int key;
};

#ifdef __cplusplus
extern "C"  //Tells the compile to use C-linkage for the next scope.
{
#endif

// C++ class w/ python
// simple c bindings for python/c integration
Test* new_test(){return new Test();}
void read(Test* t, double a[5]){t->read(a);}
// double* readprotected(Test* t){return t->readprotected();}
void readprotected(void* ptr){
    Test* t = reinterpret_cast<Test*>(ptr);
    t->readprotected();
}

///////////////////////////////////////////////////////////

int test(int a){
    return a*a;
}

double hcos(double j){
    double ans = 0.0;
    printf(">> %f %f\n", j, ans);
    try {
        ans = cos(j);
    }
    catch (...) {
        printf("crap\n");
    }
    return ans;
}

void testarray(double a[5]){
    for (int i=0; i<5; i++) a[i] = i*10.0;
}

#ifdef __cplusplus
}
#endif
