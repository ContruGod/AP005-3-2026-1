#include <iostream>
using namespace std;

void duplicar(int *p){ // resibe una direccion a un entero
    if(p != NULL){ ///verifica qu el puntero sea valido
     *p = (*p) * 2;//duplica el valor almacenado en la direccion apuntada
    }
}   
        
void intercambiar(int *a, int *b){ //recibe dos direcciones de enteros
    if (a == NULL || b == NULL){ ///verifica que ambas direcciones sean validas
    return;
    }
 
    int temp = *a; // guarda temporalmente el contenido el contenido apuntado en a
    *a = *b; //copia en a el contenido apuntado por b
    *b = temp; //copia en b el valor temporalmente
}
    void analizarNumeros(int a, int b, int c, int *sumar, int *mayor, int *menor){ 
    if(sumar == NULL || mayor == NULL || menor == NULL){ // verifica direcciones
    return; 
}
        *sumar = a + b + c;//escribe la suma en la direccion recibida
        
        *mayor = a;// supone inicialmente que a es mayor
        if(b > *mayor){ //compara b con el mayor actual
            *mayor =b; // actualuza el mayor si b es mas grande
        }
        
        if (c > *mayor){//compara c con el mayor actualuza
        *mayor = c; // actualuza el amyor si c es mas grande
        }
        
        *menor = a;//supone inicialmenteque a es el menor
        if (b < *menor){ ///compara b con el menor actualuza
        *menor = b; //actualiza el menor si b es mas pequeño
        }
        
        if(c < *menor){ //compara c con el menor actual
        *menor = c; ///actualiza el menor si c es mas pequeño
}
}
int main() {
        int x = 10; // primera variable original
        int y = 20; // segunda variable original
        int z = 5;// tercer variable original
        
        int *px = &x; //px guarda la direccion en x
        
        int sumar;//variable donde se escribira la sumar
        int mayor;//variable donde se escribira el mayor
        int menor;//variable donde se escribira el  menor
        int opcion; //opcion seleccionada por el usuario
        
        do {//ciclo
        
        cout<<"========== MENU CORTO DE PUNTEROS ==============="<<endl;
        cout<<"1. Mostrar x, &x, px y *px"<<endl;
        cout<<"2. Duplicar x usando el puntero px"<<endl;
        cout<<"3. Intercambiar x e y usando punteros"<<endl;
        cout<<"4. Analizar x, y, z usando punteros de salida"<<endl;
        cout<<"0. Salir"<<endl;
        
        cin>> opcion; // leer opcion
        
    switch(opcion){ //decide que accion ejecutar
        case 1:
            cout<<"x = "<<x<<endl;
            cout<<"&x = "<<&x<<endl;
            cout<<"px = "<<px<<endl;
            cout<<"*px = "<<*px<<endl;
            break;
            
        case 2:
            cout<<"Antes x = "<<x<<endl;
            duplicar(px);//modificaa x usando su direccion
            cout<<"despues x = "<<x<<endl;
            break;
            
        case 3:
        cout<<"Antes x = "<<x<<", y = "<<y<<endl;
        intercambiar(&x, &y); //encia direcciones x e mayor
        cout<<"Despues x = "<<x<<", y = "<<y<<endl;
        break;
        
        case 4:
        analizarNumeros(x,y,z, &sumar, &mayor, &menor);
        cout<<"suma = "<<sumar<<endl;
        cout<<"mayor = "<<mayor<<endl;
        cout<<"menor = "<<menor<<endl;
        break;
        
        case 0:
            cout<<"fin del programa "<<endl;
            break;
            
            default:
            cout<<"Opcion no valida"<<endl;
            break;
    }
        } while (opcion != 0); ///repite mientras no se seleccione Salir
        return 0;
}
