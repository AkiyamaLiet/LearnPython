#include <iostream>

using namespace std;
template<class Type>
inline void Swap(Type &a, Type &b)
{
    Type temp = a; a = b; b = temp;
}
template<class Type>
void Perm(Type list[], int k, int m)
{
    //����list[k:m]����������
    if (k==m)
    {
        // ֻʣ��һ��Ԫ��
        for (int i=0; i<=m; i++) cout << list[i];
        cout<<endl;
    }
    else  // ���ж��Ԫ�ش����У��ݹ��������
        for (int i=k; i<=m; i++){
            Swap(list[k], list[i]);
            Perm(list, k+1, m);
            Swap(list[k], list[i]);
        }
}


int main()
{
    int a[] = {1, 2, 3, 4, 5};
    Perm(a, 0, 4);
    return 0;
}
