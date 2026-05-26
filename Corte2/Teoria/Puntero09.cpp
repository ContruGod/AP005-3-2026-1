#include <iostream>
using namespace std;

int sumar(int a, int b){ //reciben 2 enteros como entrada
    
    return a + b;  //devuelve un solo resultado
}
int main()
{
        int resultado = sumar(4,7); //llama la funcion y guarda el valor retornado
        
        
        cout<<"Resultado = "<<resultado<<endl; //muestra el resultado  
        
    return 0;
}
